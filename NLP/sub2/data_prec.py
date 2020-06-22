#!/usr/local/bin/python3.6
# -*- coding: utf-8 -*-
import os
import re
# import xml
# import json
from xml.dom.minidom import parse
from string import punctuation
import nltk
# nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
from nltk.corpus import wordnet
# from nltk import RegexpTokenizer
from textblob import TextBlob
# from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from textblob import Word
from nltk.probability import FreqDist
# from xml.parsers.expat import ExpatError
import pandas as pd
from threading import Thread
from time import sleep
from shutil import copyfile
import pytest

class MakeDemographics():
    """
    You have to determine the type of demographics for each xml file before initailize this object
    """
    def __init__(self, dir_path):
        Thread.__init__(self)
        self.dir_path = dir_path
        self.males_files_path = list()
        self.females_files_path = list()
        self.age_young_files_path = list()
        self.age_old_files_path = list()
        self.everyone_files_path = list()
        self.assign_files()
        print(len(self.males_files_path),
              len(self.females_files_path), len(self.age_old_files_path), len(self.age_young_files_path))

        print(len(self.everyone_files_path))

    def assign_files(self):
        for each_file in os.listdir(self.dir_path):
            each_file_path = os.path.join(self.dir_path, each_file)
            self.everyone_files_path.append(each_file_path)
            file_name = os.path.basename(each_file)
            file_features = file_name.split('.')

            gender_ = file_features[1]
            age_ = file_features[2]
            if gender_ == "male":
                self.males_files_path.append(each_file_path)
            elif gender_ == "female":
                self.females_files_path.append(each_file_path)
            else:
                continue

            if int(age_) <= 20:
                self.age_young_files_path.append(each_file_path)
            else:
                self.age_old_files_path.append(each_file_path)

    def run(self, files_path, demo="male"):
        for each_path in files_path:
            try:

                file_name = os.path.basename(each_path)[0:-4]
                cre_file_path = "./%s/%s.txt" % (demo, file_name)
                if os.path.exists(cre_file_path):
                    print("已存在..")
                    continue
                print(file_name)
                dc = DataCleaning(each_path)
                each_words_lst = dc.main()
                words_str = " ".join(each_words_lst)
                with open(cre_file_path, "w") as f:
                    f.write(words_str)
            except:
                print("ERROR!")
                print(each_path)
            sleep(1)


def devid(dir_path):
    for each_file in os.listdir(dir_path):
        each_file_path = os.path.join(dir_path, each_file)
        file_name = os.path.basename(each_file)
        file_features = file_name.split('.')
        age_ = file_features[2]
        # import pytest
        # pytest.set_trace()
        if int(age_) <= 20:
            des_path = "./young/%s" % each_file
        else:
            des_path = "./old/%s" % each_file
        copyfile(each_file_path, des_path)

def male_pro():
    mm = MakeDemographics("/Users/yanganqi/AUT/TextMining/TM_sub2/new_blogs")
    male_files_path = mm.males_files_path
    length = len(male_files_path)
    t1 = Thread(target=mm.run, args=(male_files_path[:length],))
    t2 = Thread(target=mm.run, args=(male_files_path[length:],))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

def female_pro():
    mm = MakeDemographics("/Users/yanganqi/AUT/TextMining/TM_sub2/new_blogs")
    female_files_path = mm.females_files_path
    length = len(female_files_path)
    t1 = Thread(target=mm.run, args=(female_files_path[:length],"female"))
    t2 = Thread(target=mm.run, args=(female_files_path[length:],"female"))
    t1.start()
    t2.start()
    t1.join()
    t2.join()



def deal_xml(dir_path):
    for each_file in os.listdir(dir_path):
        each_file_path = os.path.join(dir_path, each_file)
        file_name = os.path.basename(each_file)
        print(file_name)
        with open(each_file_path, 'rb') as f:
            st = f.readlines()
            new_lines = list()
            for i in st:
                try:
                    i = i.decode('utf8')
                except:
                    continue
                i = i.replace('\n', '')
                i = i.strip()
                i = i.replace("&", " ")
                if i:
                    new_lines.append(i+'\n')
        fw = open('new_blogs/%s' % file_name, 'w')
        fw.writelines(new_lines)
        fw.close()


class DataCleaning():

    def __init__(self, file_path):
        self.file_path = file_path
        self.punc = punctuation
        self.synonyms_ = None
        self.stop = None
        self.syno_map()
        self.new_punc()
        self.stop_words()


    def new_punc(self):
        p = punctuation.replace(",", "")
        p = p.replace(".", "")
        p = p.replace("!", "")
        p = p.replace(";", "")
        self.punc = p

    def stop_words(self):
        # Declaring additional stopwords based on text content and context
        stopwords_ = ['article', 'Articles', 'page', 'wikipedia', 'talk', 'edit', 'one', 'make', 'please', 'like',
                      'see', 'think', 'urllink', 'nbsp', 'so', 'today', 'tomorrow', 'stuff',
                      'know', 'source', 'go', 'also', 'time', 'add', 'people', 'user', 'well', 'need', 'block', 'may',
                      'want', 'link', 'image',
                      'good', 'name', 'delete', 'find', 'look', 'thanks', 'work', 'remove', 'even', 'comment', 'help',
                      'write', 'information',
                      'change', 'way', 'list', 'give', 'deletion', 'editor', 'question', 'section', 'point', 'thing',
                      'try', 'wiki',
                      'first', 'wp', 'new', 'fact', 'seem', 'state', 'read', 'reference', 'discussion', 'right',
                      'thank', 'many', 'place', 'much',
                      'ask', 'revert', 'really', 'mean', 'reason', 'call', 'include', 'sinc', 'edits', 'create', 'word',
                      'back', 'note', 'tag',
                      'post', 'someone', 'policy', 'wiki', 'show', 'leave', 'issue', 'two', 'year', 'still', 'stop',
                      'content', 'hi', 'case', 'consider', 'something', 'keep', 'claim', 'http', 'mention', 'without',
                      'problem', 'let', 'day', 'person', 'utc', 'request', 'welcome', 'believe', 'anoth', 'might',
                      'subject', 'feel', 'part', 'free', 'start', 'however', 'sure', 'never', 'tell', 'book', 'view',
                      'copyright', 'actually', 'anything', 'follow', 'agree', 'regard', 'continue', 'best', 'hope',
                      'understand',
                      'site', 'long', 'provide', 'already', 'term', 'great', 'move', 'com', 'nothing', 'review',
                      'though',
                      'notice', 'little', 'explain', 'message', 'last', 'anyone', 'must', 'others', 'contribution',
                      'speedy',
                      'example', 'number', 'account', 'style', 'text', 'bad', 'title', 'sorry', 'appear', 'rather',
                      'fair', 'different', 'ip', 'matter', 'life', 'non', 'cite', 'suggest', 'report', 'template',
                      'guideline',
                      'correct', 'statement', 'old', 'lot', 'address', 'original', 'probably', 'language', 'everi',
                      'material',
                      'top', 'simply', 'consensus', 'hello', 'either', 'live', 'interest', 'far', 'least', 'notable',
                      'yes', 'date',
                      'enough', 'etc', 'idea', 'base', 'around', 'admin', 'ban', 'real', 'version', 'www', 'website',
                      'yet', 'evidence',
                      'clear', 'encyclopedia', 'quote', 'end', 'research', 'topic', 'picture', 'clearly', 'medium',
                      'ever', 'file',
                      'maybe', 'exist', 'instead', 'country', 'org', 'pov', 'criterion', 'important', 'true', 'oh',
                      'always',
                      'happen', 'perhaps', 'quite', 'whether', 'care', 'big', 'lead', 'bit', 'administrator',
                      'contribute', 'sign',
                      'citation', 'answer', 'allow', 'second', 'sentence', 'three', 'line', 'several', 'hey', 'high',
                      'man',
                      'argument', 'project', 'current', 'kind', 'redirect', 'action', 'general', 'refer', 'common',
                      'mind',
                      'summary', 'concern', 'course', 'discuss', 'present', 'result', 'possible', 'main', 'accept',
                      'test', 'learn',
                      'order', 'play', 'type', 'less', 'dont', 'jpg', 'en', 'member', 'attempt', 'ok', 'sense', 'party',
                      'week',
                      'form', 'info', 'notability', 'position', 'act', 'side', 'contribs', 'company', 'city', 'entry',
                      'warn', 'four',
                      'specific', 'news', 'publish', 'appropriate', 'standard', 'single', 'detail', 'anyway', 'open',
                      'reply', 'cause',
                      'fix', 'meet', 'next', 'describe', 'system', 'film', 'copy', 'full', 'although', 'per', 'upload',
                      'relevant',
                      'away', 'lol', 'stay', 'record', 'large', 'speak', 'recent', 'band', 'search', 'run', 'official',
                      'process', 'public',
                      'month', 'area', 'response', 'currently', 'everyone', 'especially', 'later', 'release', 'able',
                      'propose',
                      'check', 'paragraph', 'web', 'otherwise', 'generally']
        punc = list(self.punc) + ['..', '...']
        pron = ['it', 'him', 'they', 'we', 'us', 'them', 'i', 'he', 'she', 'let', ]
        generic = ["'d", "co", "ed", "put", "say", "get", "can", "become",
                   "los", "sta", "la", "use", "else", "could", "would", "come", "take", 'th', 's']
        self.stop = stopwords.words('english') + punc + pron + generic + stopwords_

    def syno_map(self):
        self.synonyms_ = {"aren't": "are not", "can't": "cannot", "couldn't": "could not",
                     "didn't": "did not", "doesn't": "does not", "don't": "do not",
                     "hadn't": "had not", "hasn't": "has not", "haven't": "have not",
                     "he'd": "he would", "he'll": "he will", "he's": "he is",
                     "i'd": "I had", "i'll": "I will", "i'm": "I am", "isn't": "is not",
                     "it's": "it is", "it'll": "it will", "i've": "I have", "let's": "let us",
                     "mightn't": "might not", "mustn't": "must not", "shan't": "shall not",
                     "she'd": "she would", "she'll": "she will", "she's": "she is",
                     "shouldn't": "should not", "that's": "that is", "there's": "there is",
                     "they'd": "they would", "they'll": "they will", "they're": "they are",
                     "they've": "they have", "we'd": "we would", "we're": "we are",
                     "weren't": "were not", "we've": "we have", "what'll": "what will",
                     "what're": "what are", "what's": "what is", "what've": "what have",
                     "where's": "where is", "who'd": "who would", "who'll": "who will",
                     "who're": "who are", "who's": "who is", "who've": "who have",
                     "won't": "will not", "wouldn't": "would not", "you'd": "you would",
                     "you'll": "you will", "you're": "you are", "you've": "you have",
                     "'re": " are", "wasn't": "was not", "we'll": " will", "tryin'": "trying", "thank": "thanks"}
        pass
    def preprocessing(self, text):
        word_tokens = nltk.word_tokenize(text)
        word_tokens = [word.lower() for word in word_tokens if (word != "th") \
                       and ("''" != word) and ("``" != word) \
                       and (word != "'s") and not word.isnumeric()]

        for i in range(len(word_tokens)):
            if word_tokens[i] in self.synonyms_:
                word_tokens[i] = self.synonyms_[word_tokens[i]]

        filtered_terms = [word for word in word_tokens if (word not in self.stop) and \
                          (len(word) > 2) and (not word.replace('.', '', 1).isnumeric()) \
                          and (not word.replace("'", '', 2).isnumeric())]

        # Lemmatization & Stemming - Stemming with WordNet POS
        tagged_tokens = nltk.pos_tag(filtered_terms, lang='eng')
        # Stemming with for terms without WordNet POS
        stemmer = SnowballStemmer("english")
        wordnet_tags = {'N': wordnet.NOUN,
                        'J': wordnet.ADJ,
                        'V': wordnet.VERB,
                        'R': wordnet.ADV}
        wordnetlem = WordNetLemmatizer()
        stemmed_tokens = []
        for tagged_token in tagged_tokens:
            term = tagged_token[0]
            pos = tagged_token[1]
            pos = pos[0]
            try:
                pos = wordnet_tags[pos]
                lemma_token = wordnetlem.lemmatize(term, pos=pos)
                if lemma_token not in self.stop:
                    stemmed_tokens.append(lemma_token)
            except:
                lemma_token = stemmer.stem(term)
                if lemma_token not in self.stop:
                    stemmed_tokens.append(lemma_token)
        # pytest.set_trace()
        return stemmed_tokens

        # 4. remove numberic
        # text_ = re.sub(r'\d+', '', text)


        # new_lst = list()
        # for i in word_tokens:
        #     # 1. lower casing
        #     w = i.lower()
        #     # 2. remove punctuations
        #     w = re.sub('[%s]' % re.escape(self.punc), '', w)
        #
        #     # 3. remove stop words
        #     if w in self.stop:
        #         continue
        #     # 9. remove short word
        #     if len(w) < 3:
        #         continue
        #
        #     # 7 spelling correction
        #     # print(time.time())
        #     # w = str(TextBlob(w).correct())
        #     # print(time.time())
        #     # if not w.isalpha():
        #     #     continue
        #     # if w in words:
        #     new_lst.append(w)

        # new_lst_2 = list()
        # frequency = pd.Series(new_lst).value_counts()[:20]
        # rarely_words = frequency[frequency.values < 2].index
        # for word in new_lst:
        #     # 5. frequent word removal from the text
        #     # 6. remove rare words
        #     if word in frequency :
        #         continue
        #     if word in rarely_words:
        #         continue
        #     new_lst_2.append(word)

            # 8. lemmatization
        # new_text = self.lemmatization(" ".join(new_lst))
        return new_text


    @staticmethod
    def rm_stopwords(text):
        """ remove stopwords from a list of words for the specified language (e.g. 'english') """
        stop_words_lst = stopwords.words('english')
        text_lst = text.split()
        new_text_lst = [word for word in text_lst if word not in stop_words_lst]
        # text['text'] = text['text'].apply(lambda t: " ".join(word for word in t.split()
        #                                                      if word not in stop_words_lst))
        # return [w for w in tokens if not w in stopwords.words(lang)]
        return " ".join(new_text_lst)

    @staticmethod
    def remove_punctuation(text):
        new_sen_lst = [re.sub('[%s]' % re.escape(punctuation), '', i) for i in text.split()]
        new_sentence = ' '.join(new_sen_lst)
        # pytest.set_trace()
        # tokenizer = nltk.RegexpTokenizer(r"\w+")
        # new_words = tokenizer.tokenize(text)
        return new_sentence
        # return filter(lambda w: w not in punctuation, tokens)
        # return tokens.translate(str.maketrans('', '', punctuation))

    @staticmethod
    def lower(text):
        t_lst = [w.lower() for w in text.split()]
        return " ".join(t_lst)

    @staticmethod
    def rm_fre_words(text):
        """Remove frequent words — Apart from stop words, there are some other words also present in the text which occur more frequently than others.
        :return:
        """
        # The intuition here is if some words are occurring in all the instances of text
        # then they are not contributing to our classification task (if this is what you are doing).
        # If the same thing is present in all the instances then it can’t be used for differentiating among classes.
        # The frequent occurring word can be seen on the left.
        # To remove these words, first, we will take whole text and split into words and then calculate their frequency.
        # Then we can select how many words we want to remove and filter them out.
        frequency = pd.Series(text.split()).value_counts()[:20]

        new_text = [word for word in text.split() if word not in frequency]
        return " ".join(new_text)

    @staticmethod
    def rm_rare_words(text):
        """Remove rarely occurring words
        :return:
        """
        # Rarely occurring words are the words which occur only a few times in the whole dataset.
        all_words_lst = text.split()
        rarely = pd.Series(all_words_lst).value_counts()
        rarely.sort_values()
        rarely_words = rarely[rarely.values < 2].index
        new_words_lst = [word for word in all_words_lst if word not in rarely_words]

        return " ".join(new_words_lst)

    @staticmethod
    def rm_numeric(text):

        return re.sub(r'\d+', '', text)

    @staticmethod
    def spelling_mistaken(text):
        # a powerful python based library TextBlob
        text_lst = text.split()
        new_text_lst = [str(TextBlob(word).correct()) for word in text_lst]
        return " ".join(new_text_lst)
        pass

    def lemmatization(self, text):
        # norm_words = set(nltk.corpus.words.words())
        # text_lst = text.split()
        # new_text_lst = [Word(word).lemmatize() for word in text_lst]
        # pytest.set_trace()
        # return " ".join(new_text_lst)
        # 获取单词在句子中的词性
        tokens = word_tokenize(text)
        tagged_sent = nltk.pos_tag(tokens)
        # 对每个单词进行词性转换
        wnl = WordNetLemmatizer()
        lemmas_sent = list()
        for word, tag in tagged_sent:
            if self.get_wordnet_pos(tag):
                word_pos = self.get_wordnet_pos(tag)
                lemmas_sent.append(wnl.lemmatize(word, pos=word_pos))
            else:
                lemmas_sent.append(word)
        return " ".join(lemmas_sent)

    @staticmethod
    def remove_shortwords(text, l):
        """ remove tokens whose length is lower than specified maximal length """
        return [w for w in text.split() if len(w) >= l]

    def get_wordnet_pos(self, tag):
        if tag.startswith('J'):
            return wordnet.ADJ
        elif tag.startswith('V'):
            return wordnet.VERB
        elif tag.startswith('N'):
            return wordnet.NOUN
        elif tag.startswith('R'):
            return wordnet.ADV
        else:
            return None

    def main(self):
        all_sentences = ""
        domTree = parse(self.file_path)
        post_lst = domTree.documentElement.getElementsByTagName('post')
        for i, each_post in enumerate(post_lst):
            each_content = each_post.childNodes[0].data
            each_content = ''.join(each_content.split('\n'))
            each_content = each_content.strip()
            if not each_content:
                continue

            each_content = self.preprocessing(each_content)
            each_content = "%s." %each_content
            all_sentences = "%s %s" %(all_sentences, each_content)

        # blog_content = " ".join(all_sentences_lst)
        #
        # cleaned_data = self.preprocessing(blog_content)
        # print(cleaned_data.split('.'))
        return all_sentences
        # # 1. lower casing
        # text_n = self.lower(blog_content)
        # # 2. remove punctuations
        # text_nn = self.remove_punctuation(text_n)
        # # 3. remove stop words
        # text3 = self.rm_stopwords(text_nn)
        #
        # # 4. remove numberic
        #
        # text4 = self.rm_numeric(text3)
        #
        # # 5. frequent word removal from the text
        # text5 = self.rm_fre_words(text4)
        # # 6. remove rare words
        # text6 = self.rm_rare_words(text5)
        # # 7. Spelling correction
        #
        # text7 = self.spelling_mistaken(text6)
        # # 8. lemmatization
        # text8 = self.lemmatization(text7)
        # # 9. remove short word
        # text9 = self.remove_shortwords(text8, 3)
        # return text9
        # # Bad of words


def combine_context(dir_path):
    import nltk
    words = set(nltk.corpus.words.words())

    demo = dir_path.split('/')[-1]
    all_content = list()
    for file in os.listdir(dir_path):
        each_file_path = os.path.join(dir_path, file)
        with open(each_file_path,'rb') as f:
            content = f.readline().decode('utf8')
            content = " ".join(w for w in nltk.wordpunct_tokenize(content)
                               if w.lower() in words or not w.isalpha())
            all_content.append("%s" % content)

    with open("all_%s.txt" % demo, 'w') as wf:
        wf.writelines(all_content)


def get_frequency(demo_file_path):
    words_lst = list()
    with open(demo_file_path, 'r') as f:
        content_lst = f.readlines()
        # for sentence in content_lst:
        #     sentence = sentence.strip()
    content_str = " ".join(content_lst)
    words_lst = content_str.split()
    fdist = FreqDist(words_lst)
    import pytest
    pytest.set_trace()
    print(fdist.tabulate(40, cumulative=True))


if __name__ == '__main__':
    # rm_stopwords()
    # deal_xml("../blogs")
    # deal_file("new_blogs/5114.male.25.indUnk.Scorpio.xml")
    # deal_file("7596.male.26.Internet.Scorpio.xml")
    # dc = DataCleaning("../new_blogs/3489929.female.25.Student.Cancer.xml")
    # dc.main()
    # male_pro()
    # combine_context("../blogcontent/everyone")
    get_frequency("all_everyone.txt")

