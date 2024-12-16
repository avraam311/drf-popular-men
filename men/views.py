from django.forms import model_to_dict
from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import MenSerializer
from .models import Men


class MenAPIView(APIView):
    def get(self, request):
        m = Men.objects.all()
        return Response({'posts': MenSerializer(m, many=True).data})
    
    def post(self, request):
        serializer = MenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Men.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id'],
        )

        return Response({'post': MenSerializer(post_new).data})


# class MenAPIView(generics.ListAPIView):
#     queryset = Men.objects.all()   
#     serializer_class = MenSerializer
