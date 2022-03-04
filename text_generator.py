import sys
import nltk
from nltk.tokenize import WhitespaceTokenizer
from nltk.probability import FreqDist
from collections import Counter
import random
import re


def read_from_file(f_name):
    text = ''
    f = None
    try:
        f = open(f_name, "r", encoding="utf-8")
    except FileNotFoundError:
        text = None
    else:
        text = f.read()
    finally:
        f.close()
        return text


def get_corpus(text):
    tk = WhitespaceTokenizer()
    return tk.tokenize(text)


# Commented functions for sentence generations
# based on bigrams
'''
def get_bigrams_dict(corp):
    bigr_list = list(nltk.bigrams(corp))
    bigr_dict = dict()
    for head_, tail_ in bigr_list:
        bigr_dict.setdefault(head_, []).append(tail_)
    return bigr_dict


def get_freq_dict(lst):
    return dict(Counter(lst))


def get_first_word(corp):
    while True:
        word = random.choice(corp)
        if re.match(r'^[A-Z].*[^.?!]$', word):
            return word


def get_next_word(freq_dict):
    tails_list = list(freq_dict.keys())
    weights_list = list(freq_dict.values())
    return ''.join(random.choices(tails_list, weights_list))


def sentence_generator_bigrams(corp, bigrams):
    head = get_first_word(corp)
    sent = [head]
    while True:
        freq_tail_dict = get_freq_dict(bigrams[head])
        next_word = get_next_word(freq_tail_dict)
        sent.append(next_word)
        head = next_word
        if re.match(r'.+[.?!]$', sent[-1]) and len(sent) >= 5:
            break
    return sent


def print_bigrams_statistic(bigrams):
    print(f'Number of bigrams: {len(bigrams)}')


def print_corpus_statistics(corp):
    print('Corpus statistics')
    f_dist = FreqDist(corp)
    total_tokens = f_dist.N()
    print(f'All tokens: {total_tokens}')
    unique_tokens = f_dist.B()
    print(f'Unique tokens: {unique_tokens}')
'''


def get_trigrams_dict(corp):
    trigr_list = list(nltk.ngrams(corp, 3))
    trigr_dict = dict()
    for head_1, head_2, tail in trigr_list:
        trigr_dict[(head_1, head_2)] = tail
    return trigr_dict


def get_head(trigr_dict):
    while True:
        head_ = random.choice(tuple(trigr_dict.keys()))
        if re.match(r'^[A-Z].*[^.?!]$', head_[0]):
            return head_


def sentence_generator_trigrams(trigr_dict):
    head = get_head(trigrams_dict)
    sent = list(head)
    while True:
        tail = trigr_dict[head]
        sent.append(tail)
        head = (sent[-2], sent[-1])
        if re.match(r'.+[.?!]$', sent[-1]) and len(sent) >= 5:
            break
    return sent


if __name__ == "__main__":
    filename = input()
    info = read_from_file(filename)
    if not info:
        sys.exit()
    corpus = get_corpus(info)
    trigrams_dict = get_trigrams_dict(corpus)
    for _ in range(10):
        sentence = sentence_generator_trigrams(trigrams_dict)
        print(*sentence)
