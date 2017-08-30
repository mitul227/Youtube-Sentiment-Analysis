__author__ = 'user'


from googleapiclient.discovery import build

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
DEVELOPER_KEY = "AIzaSyDhWZjOQ_lCKHbJJnE14fKx1Vor8dCBBFI"


def get_likes_dislikes(video_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    results = youtube.videos().list(
        part = "statistics",
        id = video_id,
    ).execute()

    likes = int(results["items"][0]["statistics"]["likeCount"])
    dislikes = int(results["items"][0]["statistics"]["dislikeCount"])

    return likes,dislikes
