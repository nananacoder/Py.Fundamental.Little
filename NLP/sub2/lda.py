#!/usr/local/bin/python3.6
# -*- coding: utf-8 -*-
import nltk
import os
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from data_prec import DataCleaning
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pytest

def lda():
    # corpus = ['This is the first document.',
    #           'This document is the second document.',
    #           'And this is the third one.',
    #           'Is this the first document?']
    corpus = data_ga("../test")
    # pytest.set_trace()

    # the vectorizer object will be used to transform text to vector form
    vectorizer = CountVectorizer(max_df=1.9, min_df=10)

    # apply transformation
    tf = vectorizer.fit_transform(corpus).toarray()

    # tf_feature_names tells us what word each column in the matric represents
    tf_feature_names = vectorizer.get_feature_names()

    number_of_topics = 1

    model = LatentDirichletAllocation(n_components=number_of_topics, random_state=42)

    model.fit(tf)

    no_top_words = 10
    draw(model, tf_feature_names, 25)
    # re = display_topics(model, tf_feature_names, no_top_words)
    # re = print_top_words(model, tf_feature_names, no_top_words

    # print(re)

def draw(lda, terms, terms_count):
    for idx, topic in enumerate(lda.components_):
        print('Topic# ', idx + 1)
        abs_topic = abs(topic)
        topic_terms = [[terms[i], topic[i]] for i in abs_topic.argsort()[:-terms_count - 1:-1]]
        topic_terms_sorted = [[terms[i], topic[i]] for i in abs_topic.argsort()[:-terms_count - 1:-1]]
        topic_words = []
        for i in range(terms_count):
            topic_words.append(topic_terms_sorted[i][0])
        print(','.join(word for word in topic_words))
        print("")
        dict_word_frequency = {}

        for i in range(terms_count):
            dict_word_frequency[topic_terms_sorted[i][0]] = topic_terms_sorted[i][1]
        wcloud = WordCloud(background_color="white", mask=None, max_words=100, \
                           max_font_size=60, min_font_size=10, prefer_horizontal=0.9,
                           contour_width=3, contour_color='black')
        wcloud.generate_from_frequencies(dict_word_frequency)
        plt.imshow(wcloud, interpolation='bilinear')
        plt.axis("off")
        plt.savefig("Topic#" + str(idx + 1), format="png")
        plt.show()

def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        message = "Topic #%d: " % topic_idx
        message += " ".join([feature_names[i]
                             for i in topic.argsort()[:-n_top_words - 1:-1]])
        print(message)


def display_topics(model, feature_names, no_top_words):
    topic_dict = {}
    for topic_idx, topic in enumerate(model.components_):
        topic_dict["Topic %d words" % (topic_idx)]= ['{}'.format(feature_names[i])
                        for i in topic.argsort()[:-no_top_words - 1:-1]]
        topic_dict["Topic %d weights" % (topic_idx)]= ['{:.1f}'.format(topic[i])
                        for i in topic.argsort()[:-no_top_words - 1:-1]]
    return pd.DataFrame(topic_dict)


def data_ga(dir_path):
    sentences_lst = list()
    for file_name in os.listdir(dir_path):
        each_file_path = os.path.join(dir_path, file_name)
        try:
            dc = DataCleaning(each_file_path)
            sentences_lst.append(dc.main())
        except:
            pass
        # print(dc.main())
    return sentences_lst

if __name__ == '__main__':
    # data_ga("../test")
    lda()
    pass
