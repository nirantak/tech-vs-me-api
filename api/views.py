import os

from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from api.models import Authors, Posts
from api.scripts import atom_feed

# from api.serializers import PostSerializer, AuthorSerializer
WEB_URL = "https://tvm.nirantak.com/"
FEED_URL = "https://tvm.nirantak.com/feed.xml"


@api_view(["GET"])
def index(request, format=None):
    """
    Index View with Metadata
    """
    data = {}

    data["url"] = reverse("index", request=request)
    data["web"] = WEB_URL
    data["creator"] = "Nirantak Raghav"
    data["endpoints"] = {
        "Posts": reverse("posts", request=request),
        "Post": reverse("post", args=[Posts.objects.earliest().id], request=request),
        "Authors": reverse("authors", request=request),
        "Author": reverse(
            "author", args=[Authors.objects.earliest().id], request=request
        ),
    }
    data["post_count"] = Posts.objects.all().count()
    data["author_count"] = Authors.objects.all().count()
    data["source"] = FEED_URL

    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET"])
def posts(request, format=None):
    """
    List all available posts
    """
    data = {}

    posts = Posts.objects.all()

    for post in posts:
        data[post.id] = {
            "title": post.title,
            "url": reverse("post", args=[post.id], request=request),
        }

    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET"])
def post(request, id, format=None):
    """
    Show individual post by id
    """
    data = {}

    post = get_object_or_404(Posts, id=id)
    author = get_object_or_404(Authors, name=post.author)

    data["title"] = post.title
    data["url"] = post.url
    data["author"] = {
        "name": post.author,
        "url": reverse("author", args=[author.id], request=request),
    }
    data["category"] = post.category
    data["summary"] = post.summary
    data["published"] = post.published
    data["updated"] = post.updated

    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET"])
def authors(request, format=None):
    """
    List all authors
    """
    data = {}

    authors = Authors.objects.all()

    for author in authors:
        data[author.id] = {
            "name": author.name,
            "url": reverse("author", args=[author.id], request=request),
        }

    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET"])
def author(request, id, format=None):
    """
    Show individual author by id
    """
    data = {}

    author = get_object_or_404(Authors, id=id)

    data["username"] = author.username
    data["name"] = author.name
    data["social"] = author.social
    data["post_count"] = author.post_count()
    data["posts"] = [
        reverse("post", args=[p], request=request) for p in author.post_list()
    ]

    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def update(request, format=None):
    if request.method == "GET":
        data = {}
        posts = Posts.objects.all()
        if posts:
            data["last_update"] = timezone.localtime(posts[0].updated)
        data["num_posts"] = len(posts)
        return Response(data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        if request.POST["key"] == os.environ["UPDATE_KEY"]:
            count = atom_feed.get_feed(FEED_URL)
            return Response({"posts_added": count}, status=status.HTTP_201_CREATED)
        return Response(
            {"error": "You are not authorized to do this!"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
