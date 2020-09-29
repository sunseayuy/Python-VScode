from pathlib import Path

#绝对路径
#c:\Program files\Microsoft
#相对路径
#path = Path("ecommerce")
#print(path.exists())#路径是否存在
#path = Path("emails")
#path.mkdir() #创建文件夹
#path.rmdir()#删除文件夹
path = Path()
for fail in path.glob('*'):#寻找目录下的文件
    print(fail)
