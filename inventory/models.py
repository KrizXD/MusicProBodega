from django.db import models
from faker import Faker
import random

fake = Faker()

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    brand = models.CharField(default='', max_length=50)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    description = models.TextField(default='')
    is_deleted = models.BooleanField(default=False)

    def generate_fake_data(self):
        unique_name = fake.word() + str(random.randint(1, 1000))
        while Stock.objects.filter(name=unique_name).exists():
            unique_name = fake.word() + str(random.randint(1, 1000))
        self.name = unique_name
        self.brand = fake.company()
        self.quantity = fake.random_int(min=1, max=100)
        self.price = fake.random_int(min=1, max=1000)
        self.description = fake.paragraph()

    def __str__(self):
        return self.name