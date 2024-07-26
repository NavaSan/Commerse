from django.contrib.auth.models import AbstractUser
from django.db import models


import datetime


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=150)
    imageUrl = models.CharField(max_length=350)
    bid = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")
    dateCreation = models.DateTimeField(default=datetime.datetime.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Watchlist(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    id_listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing")
