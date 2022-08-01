from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth impoprt User
import random
from .models import Name
from web.models import Name
from rest_framework import viewsets
from rest_framework import permissions
from web.serializers import NameSerializer
from web.models import Name
from rest_framework import generics

def index(request):
    r = random.randint(0,10)
    return HttpResponse(r)

def name(request):
    return HttpResponse("x")

class NameViewSet(viewsets.ModelViewSet):
    print("YEAH!")
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Name.objects.all()
    serializer_class = NameSerializer
    lookup_field = 'text'
#    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    print("YEAH!")
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = NameSerializer
#    permission_classes = [permissions.IsAuthenticated]