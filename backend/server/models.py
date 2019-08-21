from datetime import datetime

from django.db import models

# Create your models here.
class ShoppingMall(models.Model):
    name = models.CharField(max_length=50, unique=True)
    label = models.CharField(max_length=50)

    def __str__(self):
        return f"<ShoppingMall {self.name} (a.k.a {self.label})>"

class Category(models.Model):
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"<Category {self.name}>"

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

    def __str__(self):
        return "<Item %r>" % (self.name)
        