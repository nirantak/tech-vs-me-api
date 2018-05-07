from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Posts, Authors
# from api.serializers import PostSerializer, AuthorSerializer


@api_view(['GET'])
def index(request):
    '''
    Index View with Metadata
    '''
    data = {}

    data['url'] = f'{settings.BASE_URL}/'
    data['web'] = 'https://techversus.me/'
    data['creator'] = 'Nirantak Raghav'
    data['endpoints'] = {
        'Posts': f'{settings.BASE_URL}/posts/',
        'Post': f'{settings.BASE_URL}/posts/<id:int>/',
        'Authors': f'{settings.BASE_URL}/authors/',
        'Author': f'{settings.BASE_URL}/authors/<id:int>/',
    }
    data['post_count'] = Posts.objects.all().count()
    data['author_count'] = Authors.objects.all().count()
    data['source'] = 'https://techversus.me/feed.xml'

    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def posts(request):
    '''
    List all available posts
    '''
    data = {}

    posts = Posts.objects.all()

    for post in posts:
        data[post.id] = {
            'title': post.title,
            'url': f'{settings.BASE_URL}/posts/{post.id}'
        }

    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def post(request, id):
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
        'url': f'{settings.BASE_URL}/authors/{author.id}/'
    }
    data['category'] = post.category
    data['summary'] = post.summary
    data['published'] = post.published
    data['updated'] = post.updated

    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def authors(request):
    '''
    List all authors
    '''
    data = {}

    authors = Authors.objects.all()

    for author in authors:
        data[author.id] = {
            'username': author.username,
            'url': f'{settings.BASE_URL}/authors/{author.id}'
        }

    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def author(request, id):
    '''
    Show individual author by id
    '''
    data = {}

    author = get_object_or_404(Authors, id=id)

    data['username'] = author.username
    data['name'] = author.name
    data['social'] = author.social
    data['post_count'] = author.post_count()
    data['posts'] = [
        f'{settings.BASE_URL}/posts/{p}' for p in author.post_list()]

    return Response(data, status=status.HTTP_200_OK)
