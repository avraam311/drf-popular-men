from django.forms import model_to_dict
from django.shortcuts import render

from rest_framework import generics, viewsets, mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .serializers import MenSerializer
from .models import Men, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


class MenAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 2


class MenAPIList(generics.ListCreateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = MenAPIListPagination


class MenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)


class MenAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAdminOrReadOnly,)
