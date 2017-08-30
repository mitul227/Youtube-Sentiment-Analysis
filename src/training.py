__author__ = 'user'

import nltk
import random
import pickle
import os.path
from nltk.corpus import movie_reviews


word_features = []


def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


def train_classifier():
    if(os.path.isfile("classifier.pickle")):
        return

    documents = []
    for category in movie_reviews.categories():
        for fileid in movie_reviews.fileids(category):
            documents.append((list(movie_reviews.words(fileid)),category))

    #random.shuffle(documents)

    all_words = []
    for w in movie_reviews.words():
        all_words.append(w.lower())

    all_words = nltk.FreqDist(all_words)

    for w in all_words.most_common(9000):
        if(len(w[0]) >= 3):
            word_features.append(w[0])

    feature_sets = [(find_features(rev), category) for (rev, category) in documents]

    random.shuffle(feature_sets)

    #classifier = nltk.NaiveBayesClassifier.train(feature_sets[:2000])
    classifier = nltk.NaiveBayesClassifier.train(feature_sets[:2000])

    #print(nltk.classify.accuracy(classifier,feature_sets[1500:])*100)

    save_classifier = open("classifier.pickle","wb")
    pickle.dump(classifier,save_classifier)
    save_classifier.close()

