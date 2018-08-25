from api.models import Authors, Posts
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# from api.serializers import PostSerializer, AuthorSerializer


@api_view(['GET'])
def index(request, format=None):
    '''
    Index View with Metadata
    '''
    data = {}

    data['url'] = reverse('index', request=request)
    data['web'] = 'https://tvm.nirantak.com/'
    data['creator'] = 'Nirantak Raghav'
    data['endpoints'] = {
        'Posts': reverse('posts', request=request),
        'Post': reverse('post', args=[Posts.objects.earliest().id], request=request),
        'Authors': reverse('authors', request=request),
        'Author': reverse('author', args=[Authors.objects.earliest().id], request=request),
    }
    data['post_count'] = Posts.objects.all().count()
    data['author_count'] = Authors.objects.all().count()
    data['source'] = 'https://tvm.nirantak.com/feed.xml'

    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def posts(request, format=None):
    '''
    List all available posts
    '''
    data = {}

    posts = Posts.objects.all()

    for post in posts:
        data[post.id] = {
            'title': post.title,
            'url': reverse('post', args=[post.id], request=request),
        }

    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def post(request, id, format=None):
    '''
    Show individual post by id
    '''
    data = {}

    post = get_object_or_404(Posts, id=id)
    author = get_object_or_404(Authors, username=post.author)

    data['title'] = post.title
    data['url'] = post.url
    data['author'] = {
        'username': post.author,
        'url': reverse('author', args=[author.id], request=request),
    }
    data['category'] = post.category
    data['summary'] = post.summary
    data['published'] = post.published
    data['updated'] = post.updated

    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def authors(request, format=None):
    '''
    List all authors
    '''
    data = {}

    authors = Authors.objects.all()

    for author in authors:
        data[author.id] = {
            'username': author.username,
            'url': reverse('author', args=[author.id], request=request),
        }

    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def author(request, id, format=None):
    '''
    Show individual author by id
    '''
    data = {}

    author = get_object_or_404(Authors, id=id)

    data['username'] = author.username
    data['name'] = author.name
    data['social'] = author.social
    data['post_count'] = author.post_count()
    data['posts'] = [reverse('post', args=[p], request=request)
                     for p in author.post_list()]

    return Response(data, status=status.HTTP_200_OK)
