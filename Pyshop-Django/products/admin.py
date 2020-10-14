from django.contrib import admin
#在管理员界面添加产品模型
from .models import Product,Offer
# Register your models here.

#如何在管理区域中定制这个产品的表格

#ModelAdmin提供了管理区域中管理模型的所有通用功能
#我们可以修改和覆盖其中的一些功能
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price', 'stock')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

#在管理员界面添加产品模型
#site属性中有register方法
admin.site.register(Product,ProductAdmin)
admin.site.register(Offer,OfferAdmin)