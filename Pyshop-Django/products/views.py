from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
# Create your views here.

#/products -> index
# Uniform Resource Locator(Address)统一的方法定位器

#主页上的内容

'''如何将数据库中的表显示出来
第一步:将产品存储在数据库中，使用HTML模板进行格式化
第二步:创建一个HTML模板将列表呈现给用户，然后返回到
产品应用内的项目面板
'''
def index(request):
    products = Product.objects.all()#objects中有各种获取数据的方法
    # return HttpResponse('Hello World!')
    return render(request,#请求对象
    'index.html',
    {'products':products}#传递给该模板的数据字典
    ) 

def new(request):
    return HttpResponse('New Products')

    