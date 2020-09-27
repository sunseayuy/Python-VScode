def greet_user(first_name,last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start")
greet_user("John","Smith")
greet_user(last_name="Smith",first_name="John") #增加代码可读性
greet_user("John",last_name="Smith")#关键词参数只能位于位置参数之后
print("Finish")