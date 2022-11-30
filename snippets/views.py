from django.shortcuts import render
from django.http import HttpResponse
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
#for function base apiView
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
def create_api(request):
    if request.method == 'GET':
        id= request.data.get('id')
        if id is not None:
            snippets = Snippet.objects.get(id=id)
            serializer = SnippetSerializer(data=snippets)
            return Response(serializer.data)
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = request.data
        serializer = SnippetSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data saved'})
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = request.data.get('id')
        stu = Snippet.objects.get(pk=id)
        serializer = SnippetSerializer(stu, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data Update'})
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Snippet.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'data delete'})


