from django.shortcuts import render
from django.utils import timezone

from links.serializer import LinkSerializer
from .models import link
from .serializer import LinkSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from rest_framework.views import APIView
from . import models 
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

import datetime 

# Create your views here.
class PostListApi(ListAPIView):
    queryset = link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostDetailApi(RetrieveAPIView):
    queryset = link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostUpdateApi(UpdateAPIView):
    queryset = link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostDeleteApi(DestroyAPIView):
    queryset = link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostCreateApi(CreateAPIView):
    queryset = link.objects.filter(active = True)
    serializer_class = LinkSerializer

class ActiveLinkView(APIView):
    """
    Returns a list of all active (publicly accessible) links
    """
    def get(self, request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        qs = models.Link.public.all()
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    
class RecentLinkView(APIView):
    """
    Returns a list of recently created active links
    """
    def get(self, request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        seven_days_ago = timezone.now() - datetime.timedelta(days=7)
        qs = models.Link.public.filter(created_date__gte=seven_days_ago)
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)

