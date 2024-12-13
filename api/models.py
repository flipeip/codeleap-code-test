from django.db import models


class Post(models.Model):
    MAX_POST_TITLE_LENGHT = 128
    USERNAME_MAX_LENGHT = 64

    username = models.CharField(max_length=USERNAME_MAX_LENGHT, null=False, blank=False)
    created_datetime = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    title = models.CharField(max_length=MAX_POST_TITLE_LENGHT, null=False, blank=False)
    content = models.TextField(null=False)