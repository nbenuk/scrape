import csv

import pickle
from re import T


def index_save(index, name):
    with open( name+'.pickle', 'wb') as f:
        pickle.dump(index, f, pickle.HIGHEST_PROTOCOL)

def index_load(name):
    with open(name+'.pickle', 'rb') as f:

        return pickle.load(f)


def intersection(list1, list2):
    intersection = list()
    for item in list1:
        if item in list2:
            intersection.append(item)
    return intersection

def getLink(i):
    with open("country.csv", "r") as csv_file:
        link=[]
        csv_reader = csv.reader(csv_file, delimiter=',')
        for lines in csv_reader:
            if len(lines) == 2:
                link.append(lines[1])
        return link[i-2]
        # for lines in csv_reader:
        if len(csv_reader[i]) == 2:
            return(csv_reader[i][1])
            link.append(lines[1])
        else:
            return "Error"


def index():
    print('*** Building Index ***')
    # this will open the file
    file = open('country.csv', encoding='utf8')
    read = file.read()
    file.seek(0)

    # for each line/link
    array = []
    link =[]
    with open("country.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for lines in csv_reader:
            if len(lines) == 2:
                link.append(lines[1])
            array.append(lines[0])

    # remove punctuation
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for char in read:
        if read in punc:
            read = read.replace(char, " ")

    from nltk.tokenize import word_tokenize
    import nltk
    from nltk.corpus import stopwords
    nltk.download('stopwords')

    print('*** Tokenising Data ***')
    print('Please wait this will take a few minutes')

    # tokenise text

    text_tokens = word_tokenize(read)
    # remove stopwords
    tokens_no_sw = [
        word for word in text_tokens if not word in stopwords.words()]

    dict = {}
    freq={}
    print('*** Processing Data ***')
    for i in range(len(array)):
        # index docs
        check = array[i]
        for item in tokens_no_sw:
            if item in check:
                if item not in dict:
                    dict[item] = []
                if item in dict:
                    dict[item].append(i+1)
        word_count = {}

        # count freq
        tokens = word_tokenize(array[i])
        for item in tokens:
            if item not in freq:
                freq[item]=[]
            if item in word_count:
                word_count[item] += 1
            else:
                word_count[item] = 1
        for item in word_count:
            freq[item].append([i+1,word_count[item]])

    # save inverted index
    index_save(dict,'dict')
    index_save(freq,'freq')
    print('*** Index Saved ***')

    
# index()
# print (index_load())