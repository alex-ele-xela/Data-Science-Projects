from googleapiclient.discovery import build
import pandas as pd
import IPython.display as display
import re

from . import constants


class Channel:
    def __init__(self, youtube, search: str) -> None:
        items = get_channel_details(youtube, search)
        self._channel_name = items["snippet"]["title"]
        self._thumbnail = items["snippet"]["thumbnails"]["default"]["url"]
        self._subscriberCount = int(items["statistics"]["subscriberCount"])
        self._viewCount = int(items["statistics"]["viewCount"])
        self._videoCount = int(items["statistics"]["videoCount"])

        self._playlist_id = items["contentDetails"]["relatedPlaylists"]["uploads"]
        self._video_ids = get_video_ids(youtube, self._playlist_id)

        self._videos = get_video_details(youtube, self._video_ids)

    def get_stats(self) -> dict:
        stats = dict(
            ChannelName=self._channel_name,
            Thumbnail=self._thumbnail,
            Subscribers=self._subscriberCount,
            Views=self._viewCount,
            Videos=self._videoCount,
        )
        return stats

    def get_videos(self) -> pd.DataFrame:
        return self._videos


def create_youtube_api(api_key, api_service_name, api_version):
    return build(api_service_name, api_version, developerKey=api_key)


def get_channel_details(youtube, search) -> dict:
    username, channel_id = None, search

    username_pattern = "\.com\/@(.+)$"
    results  = re.findall(username_pattern, search)
    if len(results):
        username  = results[0]

    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        forUsername=username,
        id=channel_id
    )
    return request.execute()["items"][0]


def get_video_ids(youtube, playlist_id: str) -> list[str]:
    video_ids = []

    next_page_token = None
    more_pages = True
    while more_pages:
        request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token,
        )
        response = request.execute()

        for i in range(len(response["items"])):
            video_ids.append(response["items"][i]["contentDetails"]["videoId"])

        next_page_token = response.get("nextPageToken")

        if not next_page_token:
            more_pages = False

    return video_ids


def get_video_details(youtube, video_ids) -> pd.DataFrame:
    video_stats = []

    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part="snippet,statistics", id=",".join(video_ids[i : i + 50])
        )
        response = request.execute()

        for num, video in enumerate(response["items"]):
            stats = dict(
                Title=video["snippet"]["title"],
                Published_date=video["snippet"]["publishedAt"],
                Views=int(video["statistics"]["viewCount"]),
                Likes=int(video["statistics"].get("likeCount", 0)),
                Comments=int(video["statistics"].get("commentCount", 0)),
                ID=video_ids[i+num]
            )
            video_stats.append(stats)

    video_stats = pd.DataFrame(video_stats)
    video_stats['Time'] = pd.to_datetime(video_stats['Published_date']).dt.strftime('%X')
    video_stats['Day'] = pd.to_datetime(video_stats['Published_date']).dt.strftime('%d')
    video_stats['Month'] = pd.to_datetime(video_stats['Published_date']).dt.strftime('%B')
    video_stats['Year'] = pd.to_datetime(video_stats['Published_date']).dt.strftime('%Y')
    video_stats['DayOfWeek'] = pd.to_datetime(video_stats['Published_date']).dt.strftime('%A')
    video_stats.drop('Published_date', inplace=True, axis=1)

    return video_stats


def get_channel(youtube, search):
    return Channel(youtube, search)





def main():
    youtube = create_youtube_api(
        constants.API_KEY, constants.API_SERVICE_NAME, constants.API_VERSION
    )
    channel = get_channel(youtube, "UCiT9RITQ9PW6BhXK0y2jaeg")
    print(channel.get_stats())
    print(channel._video_ids)

    print(channel._videos)


if __name__ == "__main__":
    main()
