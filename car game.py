start = 1
stop = 1
while True:
    operation = input('>').upper( )
    if operation == 'HELP':
        print('''
start - to start the car
stop - to stop the car
quit - to exit''')
    elif operation == 'START':
        if start == 1:
            print('Car start,readly to go!')
        elif start == 0 :
            print('car already start!')
        stop = 1
        start = 0
    elif operation == 'STOP':
        if stop == 1:
            print('Car stopped!')
        elif stop == 0 :
            print('car already stop!')
        start = 1
        stop = 0
    elif operation == 'QUIT':
        break
    else:
        print("I don't understand!")