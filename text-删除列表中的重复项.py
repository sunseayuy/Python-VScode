numbers = [1, 4, 1, 2, 3, 4, 5, 6, 5]
numbers2 = []
for number in numbers:
    print(number)
    if number not in numbers2:
        print(number)
        numbers2.append(number)

print(numbers2)   
