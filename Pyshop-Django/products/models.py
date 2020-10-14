from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)#表示可以包含一段文本数据的字段
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=25)
    discount = models.FloatField()

#迁移python manage.py makemigrations
#    python manage.py migrate