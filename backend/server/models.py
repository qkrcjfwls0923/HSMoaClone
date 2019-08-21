from datetime import datetime

from django.db import models

# Create your models here.
class ShoppingMall(models.Model):
    name = models.CharField(max_length=50)
    label = models.CharField(max_length=50)

    def __str__(self):
        return "<ShoppingMall %r" % (self.name)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "<Category %r" % (self.name)

class Item(models.Model):
    name = models.CharField(max_length=255)
    mall = models.ForeignKey(ShoppingMall, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    url = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    org_price = models.CharField(max_length=255)

    def __init__(self, id=None, name=None, mall=None, date=None, start_time=None, end_time=None, category=None, 
            url=None, img=None, price=None, org_price=None):
        self.name = name
        self.mall = mall
        date_ = datetime.strptime(date, "%Y%m%d")

        offset = len(start_time)-2
        hour = int(start_time[:offset]) if start_time[:offset] else 0
        minute = int(start_time[offset:]) if start_time[offset:] else 0
        self.start_time = datetime(year = date_.year, month=date_.month, day=date_.day, hour=hour, minute=minute)

        offset = len(end_time)-2
        hour = int(end_time[:offset]) if end_time[:offset] else 0
        minute = int(end_time[offset:]) if end_time[offset:] else 0
        self.end_time = datetime(year = date_.year, month=date_.month, day=date_.day, hour=hour, minute=minute)

        self.category = category
        self.url = url
        self.img = img
        self.price = price
        self.org_price = org_price

    def __str__(self):
        return "<Item %r>" % (self.name)
        