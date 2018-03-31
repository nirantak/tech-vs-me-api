from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Posts


@api_view(['GET', 'POST'])
def index(request):
    return Response({'status': 'working...'}, status=status.HTTP_200_OK)
