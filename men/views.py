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
        serializer.save()

        return Response({'post': serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})
        
        try:
            instance = Men.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist'})
        
        serializer = MenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method DELETE not allowed'})

        try:
            instance = Men.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({'error': 'Object does not exist'})
              
        return Response({'post': 'delete post ' + str(pk)})


# class MenAPIView(generics.ListAPIView):
#     queryset = Men.objects.all()   
#     serializer_class = MenSerializer
