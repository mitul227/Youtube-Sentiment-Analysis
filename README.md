# Sentiment-Analysis-of-Youtube-Comments
Fetches 200 top rated comments (most liked) and number of likes, dislikes from a youtube video and determines if sentiment 
towards this video is positive, negative or mixed


# Implementation

It takes the URL of the youtube video from the user and then extracts the video id from it

It also takes the weightage (out of 100) from the user which you want to give to sentiment recieved from comments

Eg - If you enter 70 that means 70% weightage will be given to sentiment obtained from youtube comments and 30% to likes/dislikes number

For downloading the youtube comments youtube comment downloader (https://github.com/egbertbouman/youtube-comment-downloader) is used

Youtube API has been used for fetching number of likes and dislikes from a video

Naive Bayes Classifier is used for determining the sentiment here


