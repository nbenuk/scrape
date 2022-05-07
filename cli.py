import sitemap
import country
import index
print('\n---------------Welcome------------------------------Welcome------------------------------Welcome---------------\n')
args=[]
for arg in ((input('Enter a command: ').split(' '))):
    args.append(arg)
while (args[0] != 'q'):
    if args[0] == 'build':
        sitemap.crawl('http://example.python-scraping.com')
        country.build()
        index.index()
    elif args[0] == 'load':
        dict=index.index_load('dict')
        freq=index.index_load('freq')
    else:
        
        if args[0] == 'print':
            try:
                for key, val in dict.items():
                    if val == args[1] or key == args[1]:
                        val = list(dict.fromkeys(val))
                        for i in val:
                            count = 0
                            for f in freq.get(args[1]):
                                if f[0] == i:
                                    count = f[1]
                            print('Search term: \t ' + args[1] + ' \t Frequency: \t' +  str(count)+' \t URL: \t' + index.getLink(i))
            except:
                print('Error: Try loading index first')
        elif args[0] == 'find':
            if len(args) == 0:
                pass
            elif len(args) == 2:
                term = args[1]
                try:
                    for key, val in dict.items():
                        if val == term or key == term:
                            val = list(dict.fromkeys(val))
                            for i in val:
                                print(index.getLink(i))
                except:
                    print('Error: Try loading index first')
            elif len(args)==3:
                term = args[1]
                try:
                    for key, val in dict.items():
                        if val == term or key == term:
                            val2 = list(dict.fromkeys(val))
                except:
                    print('Error: Try loading index first')
                term = args[2]
                try:
                    for key, val in dict.items():
                        if val == term or key == term:
                            val1 = list(dict.fromkeys(val))
                except:
                    print('Error: Try loading index first')
                try:
                    mylist=(index.intersection(val2,val1))
                    mylist = list(dict.fromkeys(mylist))
                except:
                    print('No Results')
                for i in mylist:
                    print(index.getLink(i))      
    args = []
    for arg in ((input('Enter a command: ').split(' '))):
        args.append(arg)