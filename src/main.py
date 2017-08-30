__author__ = 'user'

from src import sentiment
import re

def extract_video_id(url):
    pattern1  = "^https://www\.youtube\.com/watch\?v=.*$"
    pattern2  = "www\.youtube\.com/watch\?v=.*$"
    if re.match(pattern1,url) or re.match(pattern2,url):
        index = url.find('=')
        video_id = url[index+1:]
        return video_id
    else:
        return None


if __name__ == "__main__":
    youtube_url = input("Enter URL of youtube video : ")

    comments_ratio = float(input("Enter % (out of 100) you want to give to sentiment from comments : "))

    if comments_ratio > 100 or comments_ratio < 0:
        print("Invalid numeric")
        exit(-1)

    video_id = extract_video_id(youtube_url)

    if video_id is None:
        print("Invalid URL")

    else:
        print("Sentiment towards this video is - ",sentiment.get_sentiment(video_id,comments_ratio))
#video_id = "w3ugHP-yZXw"  #Lig_YSxRf_4 (neg) , n-y-YHVZSwk(pos), w3ugHP-yZXw(neg) , fnZ-x55tHMI (pos),N4mEzFDjqtA(pos) , zh9NgGf3cxU(mixed), ue80QwXMRHg(pos), YngbHOz--oc(neg) , mXuEoqK4bEc(pos), SQvPRb4HADE(mixed)


