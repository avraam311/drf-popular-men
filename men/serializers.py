import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Men


# class MenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class MenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()
            

# def encode():
#     model = MenModel('Brad Pitt', 'conten: Brad Pitt')
#     model_sr = MenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)


# def decode():
#     stream = io.BytesIO(b'{"title": "Brad Pitt","content":"Content: Brad Pitt"}')
#     data = JSONParser().parse(stream)
#     serializer = MenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
    