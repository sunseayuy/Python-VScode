name = input('Please set up your name: ')
namelen=len(name)
if namelen < 3:
    print('name mast be at least 3 characters')
elif namelen >50:
    print('name mast be a maxmum of 50 characters')
else :
    print("It's a good name!")