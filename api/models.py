from django.db import models
from django.utils import timezone

# from django.contrib.auth.models import User


class Posts(models.Model):
    title = models.CharField("title", max_length=250)
    url = models.URLField(
        "url",
        unique=True,
        error_messages={"unique": "This link already exists!"},
    )
    author = models.CharField("author", max_length=250, default="nirantak")
    category = models.CharField("category", max_length=250)
    summary = models.TextField("summary")
    published = models.DateTimeField("published", default=timezone.now)
    updated = models.DateTimeField("updated", default=timezone.now)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        get_latest_by = ["updated", "published"]
        ordering = ["-updated", "-published"]

    def __str__(self):
        return f"{self.title}"


class Authors(models.Model):
    username = models.CharField(
        "username",
        max_length=100,
        unique=True,
        error_messages={"unique": "This username already exists!"},
    )
    name = models.CharField("name", max_length=100)
    social = models.URLField(
        "social",
        max_length=255,
        unique=True,
        error_messages={"unique": "This link already exists!"},
    )
    posts = models.CharField("posts", max_length=250)

    def post_list(self):
        """
        Returns a list of all post ids by author
        """
        return [int(p.strip()) for p in self.posts.split(",")]

    def post_count(self):
        """
        Returns the number of posts by author
        """
        return len(self.posts.split(","))

    class Meta:
        verbose_name = "author"
        verbose_name_plural = "authors"
        get_latest_by = ["id"]
        ordering = ["id"]

    def __str__(self):
        return f"{self.username}"
