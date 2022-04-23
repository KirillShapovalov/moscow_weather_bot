from django.db import models


class Users(models.Model):

    login = models.CharField(max_length=50)
    chat_id = models.IntegerField()
    password = models.CharField(max_length=20)
