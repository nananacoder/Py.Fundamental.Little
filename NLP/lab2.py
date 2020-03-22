#!/usr/local/bin/python3.6
# -*- coding: utf-8 -*-


import os
import sys
sys.setrecursionlimit(1000000)
from pickle import dump, load
import nltk
from nltk.corpus import brown
from nltk.tag import tnt, crf
from nltk.metrics.scores import precision, recall,f_measure


def unigram_tag(train_):
    unig_tagger = nltk.UnigramTagger(train_)
    return unig_tagger


def tnt_tag(train_):
    # initializing tagger
    tnt_tagger = tnt.TnT()
    tnt_tagger.train(train_)
    return tnt_tagger


def perceptron_tag(train_):
    perc_tagger = nltk.PerceptronTagger(load=False)
    perc_tagger.train(train_)
    return perc_tagger


def crf_tag(train_):
    crf_tagger = crf.CRFTagger()
    crf_tagger.train(train_, 'model.crf.tagger')
    return crf_tagger


def store_pickle(tagger_object):
    # Q3 train all of the taggers
    # and store the trained model as a pickle file.
    file_name = "{}_Tagger.pkl".format(str(tagger_object).split()[0])
    output = open(file_name, 'wb')
    dump(tagger_object, output, -1)
    output.close()


def retrieve_pickle(file_):
    # Q4
    input_ = open(file_, 'rb')
    ldd_model = load(input_)
    input_.close()
    return ldd_model


def find_freq_words():
    with open("news10.txt") as fl:
        sentences_lst = fl.readlines()
        sen_res = [sentence.split() for sentence in sentences_lst if sentence]
        words_lst = list()
        [words_lst.extend(each) for each in sen_res]
        tnt_tagger = retrieve_pickle('Tnt_Tagger.pkl')
        result_tokens = tnt_tagger.tag(words_lst)
        word_fd = nltk.FreqDist(tag for (word, tag) in result_tokens if tag[0] == 'N')
        print(word_fd.most_common())


def main():
    brown_tagged_sents = brown.tagged_sents(categories='news')
    size = int(len(brown_tagged_sents) * 0.8)
    train_data = brown_tagged_sents[:size]
    test_data = brown_tagged_sents[size:]

    # store pickle file
    if not (os.path.isfile('UnigramTagger.pkl') and os.path.isfile('Tnt_Tagger.pkl')
            and os.path.isfile('PerceptronTagger.pkl')):
        unigram_tagger = unigram_tag(train_data)
        tnt_tagger = tnt_tag(train_data)
        perc_tagger = perceptron_tag(train_data)

        [store_pickle(each_) for each_ in [unigram_tagger, tnt_tagger, perc_tagger]]

    # load pickle file and get each model file with a tuple
    models_files_tuple = [(each_.split('.')[0], retrieve_pickle(each_)) for each_ in
                    ['UnigramTagger.pkl', 'PerceptronTagger.pkl', 'Tnt_Tagger.pkl']]

    # test the loaded models on test data
    print("TESTING LOADED MODELS")
    for tagg_name, tagg_mode in models_files_tuple:
        print("Loaded {tag_name} evaluation results: {evaluate_res}".format(tag_name=tagg_name,
                                                                            evaluate_res=tagg_mode.evaluate(test_data)))

    # Tabulate and calculate accuracies, choose best one based on F1 value
    reference_sentences_lists = [list(map(lambda pair_: pair_[1], each)) for each in test_data]
    test_sentences_lists = [list(map(lambda pair_: pair_[0], each)) for each in test_data]

    reference_lst = list()
    test_lst = list()
    [reference_lst.extend(each_lst) for each_lst in reference_sentences_lists[:1000]]
    [test_lst.extend(each_lst) for each_lst in test_sentences_lists[:1000]]

    for tagg_name, tagger_mod in models_files_tuple:

        if tagg_name == "Tnt_Tagger":
            reference_lst = reference_lst[:700]
            test_lst = test_lst[:700]
        result_tokens = tagger_mod.tag(test_lst)

        result_tokens__ = list(map(lambda pair: 'UNKNOWN' if pair[1] is None else pair[1], result_tokens))

        print("{} Evaluation Results".format(tagg_name))
        print("Precision: ", precision(set(reference_lst), set(result_tokens__)))
        print("Recall: ", recall(set(reference_lst), set(result_tokens__)))
        print("F measure: ", f_measure(set(reference_lst), set(result_tokens__)))


if __name__ == '__main__':
    main()
    find_freq_words()


# Result
# TESTING LOADED MODELS
# Loaded UnigramTagger evaluation results: 0.8026879907509996
# Loaded Tnt_Tagger evaluation results: 0.8327472421600269
# Loaded PerceptronTagger evaluation results: 0.9163254492027554