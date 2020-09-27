number = 9
abc = 1
while abc <= 3:
    abc = abc+1
    guess = int(input('Gusess: '))
    if guess == number:
        print('You win!')
        break
else:
    print('You failed!') 