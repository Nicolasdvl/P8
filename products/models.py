from django.db import models

class Category(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    NUTRISCORE = [('A','A'), ('B','B'), ('C','C'), ('D','D'), ('E','E'), ('null', 'unknow')]

    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    nutriscore = models.CharField(max_length=4, choices=NUTRISCORE, default='null')
    image = models.CharField(max_length=200)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

