for x in range(4):
    for y in range(3):
        print(f'({x},{y})')
numbers = [5,2,5,2,2]
for number in numbers:
    print('X'*number)
for number in numbers:
    output = ''
    for i in range(number):
        output +='X'
    print(output)
print("                         ")
numbers2 = [2,2,2,2,5]
for number in numbers2:
    output = ''
    for i in range(number):
        output +='X'
    print(output)