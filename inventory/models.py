from django.db import models

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    brand = models.CharField(default='',max_length=50)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    description = models.TextField(default='')
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
