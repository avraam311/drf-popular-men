from django.forms import model_to_dict
from django.shortcuts import render

from rest_framework import generics, viewsets, mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import MenSerializer
from .models import Men, Category


class MenViewSet(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.ListModelMixin,
                 GenericViewSet):
    # queryset = Men.objects.all()
    serializer_class = MenSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Men.objects.all()[:3]
        
        return Men.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})


# class MenAPIList(generics.ListCreateAPIView):
#     queryset = Men.objects.all()
#     serializer_class = MenSerializer


# class MenAPIUpdate(generics.UpdateAPIView):
#     queryset = Men.objects.all()
#     serializer_class = MenSerializer


# class MenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Men.objects.all()
#     serializer_class = MenSerializer
