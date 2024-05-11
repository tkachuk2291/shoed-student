from django.shortcuts import render
from rest_framework import generics, status

from users.models import Author, Client
from users.serializers import AuthorSerializer, ClientSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class AuthorView(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class ClientView(generics.ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
