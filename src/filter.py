__author__ = 'user'

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def filter_comments(comments):
    for i in range(0,len(comments)):
        comments[i] = comments[i].strip('\ufeff')
        comments[i] = comments[i].lower()


    stop_words = set(stopwords.words('english'))
    filtered_comments = []
    for comment in comments:
        word_tokens = word_tokenize(comment)
        links = [w for w in word_tokens if w.startswith('www.') or w.startswith('http')]
        mentions = [w for w in word_tokens if w.startswith('@')]

        filter = [w for w in word_tokens if w not in stop_words and w not in links and w not in mentions]
        #filter = [w for w in word_tokens if w not in links and w not in mentions]
        filtered_comments.append(filter)

    return filtered_comments

