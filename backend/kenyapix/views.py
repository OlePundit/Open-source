from django.shortcuts import render
from rest_framework import generics

from .models import *
from .serializer import *

class CreatorView(generics.ListCreateAPIView):
    queryset = Creators.objects.all()
    serializer_class = CreatorSerializer

# Create your views here.
