import csv
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def getLink(i):
    with open('cUrls.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data[i]

def index():
    # this will open the file
    file = open('country.csv', encoding='utf8')
    read = file.read()
    file.seek(0)
    read

    # to obtain the
    # number of lines
    # in file
    line = 1
    for word in read:
        if word == '\n':
            line += 1
    print("Number of lines in file is: ", line)

    # create a list to
    # store each line as
    # an element of list
    array = []
    for i in range(line):
        array.append(file.readline())

    array
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for ele in read:
        if ele in punc:
            read = read.replace(ele, " ")
            
    read
    # #############################Case sensitive
    # to maintain uniformity
    # read=read.lower()					
    read
    from nltk.tokenize import word_tokenize
    import nltk
    from nltk.corpus import stopwords
    nltk.download('stopwords')

    for i in range(1):
        # this will convert
        # the word into tokens
        text_tokens = word_tokenize(read)

    tokens_without_sw = [
        word for word in text_tokens if not word in stopwords.words()]

    print(tokens_without_sw)
    dict = {}

    for i in range(line):
        check = array[i]
        for item in tokens_without_sw:

            if item in check:
                if item not in dict:
                    dict[item] = []

                if item in dict:
                    dict[item].append(i+1)
    # print(dict)
    dict


    # creawl first website
    # crawl next website in queue
    # check if ok to crawl
    # fetch and download
    # parse for new url
    # add url to queue
    # politeness policy



    # save inverted index
    # move this out of here 
    args = []
    for arg in ((input('Enter a command: ').split(' '))):
        args.append(arg)
    while (args[0] != 'q'):
        if len(args) == 0:
            pass
        elif len(args) == 1:
            print(args[0])
            [res] = [val for key, val in dict.items() if args[0] in key]
            res = list(dict.fromkeys(res))
            for i in res:
                print(getLink(i))
            pass
        elif len(args)==2:
            [res] = [val for key, val in dict.items() if args[0] in key]
            [res2] = [val for key, val in dict.items() if args[1] in key]
            mylist=(intersection(res,res2))
            mylist = list(dict.fromkeys(mylist))
            for i in mylist:
                print(getLink(i))
            # print(str(res))

        args = []
        for arg in ((input('Enter a command: ').split(' '))):
            args.append(arg)
index()