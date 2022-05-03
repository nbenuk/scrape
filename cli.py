import sitemap
import country
import index
print('\n---------------Welcome------------------------------Welcome------------------------------Welcome---------------\n')
args=[]
for arg in ((input('Enter a command: ').split(' '))):
    args.append(arg)
while (args[0] != 'q'):
    if args[0] == 'build':
        sitemap.sitemap()
        country.build()
        index.index()
    elif args[0] == 'load':
        index.index()
    else:
        try:
            if args[0] == 'print':
                index.index()
            elif args[0] == 'find':
                index.index()
        except:
            print ('invalid input')         
    args = []
    for arg in ((input('Enter a command: ').split(' '))):
        args.append(arg)