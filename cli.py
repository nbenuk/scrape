import sitemap
import country

print('\n---------------Welcome------------------------------Welcome------------------------------Welcome---------------\n')
args=[]
for arg in ((input('Enter a command: ').split(' '))):
    args.append(arg)
while (args[0] != 'q'):
    if args[0] == 'build':
        sitemap.sitemap()
    elif args[0] == 'load':
        pass
    else:
        try:
            if args[0] == 'print':
                pass
            elif args[0] == 'find':
                pass
        except:
            print ('invalid input')         
    args = []
    for arg in ((input('Enter a command: ').split(' '))):
        args.append(arg)