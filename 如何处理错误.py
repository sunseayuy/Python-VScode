try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age can't be 0!")
except ValueError:#会捕捉到错误
    print('Please input number!')