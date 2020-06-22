#!/usr/local/bin/python3.6
# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from nltk.corpus import stopwords
# def idf(corpus):
#     idfs = {}
#     d = 0.0
#
#     # 统计词出现次数
#     for doc in corpus:
#         d += 1
#         counted = []
#         for word in doc:
#             if not word in counted:
#                 counted.append(word)
#                 if word in idfs:
#                     idfs[word] += 1
#                 else:
#                     idfs[word] = 1
#
#     # 计算每个词逆文档值
#     for word in idfs:
#         idfs[word] = math.log(d / float(idfs[word]))
#
#     return idfs



def tfidf():
    corpus = ['This is the first document.',
              'This document is the second document.',
              'And this is the third one.',
              'Is this the first document?']

    # cv = CountVectorizer(max_df=0.85, stop_words=stopwords, max_features=10000)
    # word_count_vector = cv.fit_transform(corpus)
    # print(list(cv.vocabulary_.keys())[:10])

    tfidf_transformer = TfidfVectorizer(max_df=.65, min_df=1, stop_words=None, use_idf=True, norm=None)
    transformed_documents = tfidf_transformer.fit_transform(corpus)
    # print(tfidf_transformer.get_feature_names())
    transformed_documents_as_array = transformed_documents.toarray()


def extract_topn_from_vector(feature_names, sorted_items, topn=10):
    """get the feature names and tf-idf score of top n items"""

    # use only topn items from vector
    sorted_items = sorted_items[:topn]

    score_vals = []
    feature_vals = []

    # word index and corresponding tf-idf score
    for idx, score in sorted_items:
        # keep track of feature name and its corresponding score
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])

    # create a tuples of feature,score
    # results = zip(feature_vals,score_vals)
    results = {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]] = score_vals[idx]

    return results

if __name__ == '__main__':
    tfidf()
    pass