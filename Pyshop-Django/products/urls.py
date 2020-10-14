from django.urls import path
from . import views

#/products
urlpatterns = [
    path('',views.index ),#''中的是地址，后面是引用的函数
    path('new',views.new )
]
