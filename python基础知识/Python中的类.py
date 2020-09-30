class Point:# 类的命名规范单词首字母大写，多个单词连着写 如：EmailClient
    def __init__(self,x ,y ):#用于构建或创造一个对象
        self.x = x
        self.y = y

    def move(self):# 类中定义方法
        print("move")
    def draw(self):
        print("draw")

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi I am {self.name}")


john= Person("John Smith")
print(john.name)
john.talk()


print1 = Point(10,20)
#print1.x = 30 #在程序的任何地方设置属性
print(print1.x)
print1.draw()