from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


class Posts(models.Model):
    title = models.CharField("title", max_length=250)
    link = models.URLField("link", unique=True, error_messages={
        'unique': "This link already exists!"})
    author = models.CharField("author", max_length=250,
                              default="Nirantak Raghav")
    category = models.CharField("category", max_length=250)
    summary = models.TextField("summary")
    published = models.DateTimeField("published", auto_now_add=True)
    updated = models.DateTimeField("updated", auto_now=True)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return f"{self.title}"
