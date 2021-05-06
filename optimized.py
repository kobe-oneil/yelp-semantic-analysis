import nltk
from nltk.corpus import stopwords

import glob
import math

from string import punctuation

from collections import Counter

def cleaningTXTFile(text, f):
    with open(f) as file:
        text = file.read()
    text = text.split(' ')
    stop_words = set(stopwords.words('english'))
    text = [w for w in text if not w in stop_words]
    return text

def readingYelpReviews(path, f, v):
    review = path
    for newline in glob.glob(review):
        text = cleaningTXTFile(newline, review)
        v.update(text)

def testingPath(path):
    positive_indice = 0
    positive_precision = 0
    positive_summation = 0

    negative_indice = 0
    negative_precision = 0
    negative_summation = 0

    test_sets = path
    for newline in glob.glob(test_sets):
        readTXT = cleaningTXTFile(newline, test_sets)
        for metric in readTXT:
            if metric not in positiveSet:
                continue
            else:
                positive_precision += 1
                positive_indice += 1
                stars = [3.6, 4.0, 4.5, 5.0]
        for metric in readTXT:
            if metric not in negativeSet:
                continue
            else:
                negative_precision += 1
                negative_indice += 1
                stars = [1.0, 2.0, 3.0, 3.5]
        if positive_precision < negative_precision:
            negative_indice += 1
        else:
            positive_indice += 1
    return positive_indice, negative_indice

if __name__ == '__main__':
    neg = "negative-words.txt"
    pos = "positive-words.txt"

    with open(pos) as file:
        lines = file.readlines()
    lines = [character.strip( ) for character in lines]
    pw = [character for character in lines if not character.startswith(";")]

    with open(neg) as file:
        lines = file.readlines()
    lines = [character.strip( ) for character in lines]
    nw = [character for character in lines if not character.startswith(";")]

    DictionaritemPos = Counter()
    DictionaritemNeg = Counter()

    readingYelpReviews("yelp_reviews/all_reviews.txt", "negative-words.txt", DictionaritemPos) # change paths if needed
    readingYelpReviews("yelp_reviews/all_reviews.txt", "positive-words.txt", DictionaritemNeg) # change paths if needed

    positiveSet = [character for character, item in DictionaritemPos.items() if item > 1]
    negativeSet = [character for character, item in DictionaritemNeg.items() if item > 1]

    positiveSet = [metric for metric in positiveSet if metric in pw]
    negativeSet = [metric for metric in negativeSet if metric in nw]

    positive_indice, negative_indice = testingPath("yelp_reviews/all_reviews.txt") # change paths if needed

    correct = positive_indice
    total = positive_indice + negative_indice

    true_positive = positive_indice
    false_negative = negative_indice
    false_positive = abs(true_positive - false_negative)

    correct += negative_indice
    total += positive_indice + negative_indice

    r = true_positive / (true_positive + false_negative)
    p = true_positive / (true_positive + false_positive)
    a = correct / total

    print ("Accuracy:  " + str(a))
    print ("Precision: " + str(p))
    print ("Recall: " + str(r))
