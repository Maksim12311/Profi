# https://docs.djangoproject.com/en/5.1/ref/models/fields/

from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Profile(models.Model):
    pass


class Category(models.Model):
    pass
