from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Car(models.Model):
    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    engine = models.IntegerField()

class Phone(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    ram = models.IntegerField()
    storage = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    pages = models.IntegerField()
    janr = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

    