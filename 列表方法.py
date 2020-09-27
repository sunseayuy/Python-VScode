numbers = [5, 2, 1, 5, 7, 4]
print(numbers)
numbers.append(10)
print(numbers)
numbers.insert(0, 12)
print(numbers)
numbers.pop()
print(numbers)
numbers.remove(2)
print(numbers)

print(numbers.index(7))#7的索引
print(7 in numbers)

print(numbers.count(5))#5的个数

numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
print(numbers2)

numbers.clear()
print(numbers)