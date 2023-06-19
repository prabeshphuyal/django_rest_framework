from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import status
from rest_framework import api_view

@api_view(['GET','POST'])
def snippet_list(request):
    if request.method == 'GET': #GET method is used to retrieve data from server
        snippets = Snippet.objects.all() #assigning models objects to a snippets variable
        serializer = SnippetSerializer(snippets, many=True) #Serializing the snippets variable,which contain Snippets model object and many=true means a model contains multiple of objects and it is also used for validation
        return JsonResponse(serializer.data, safe=False) #returning a response of a request
    elif request.method == 'POST': #POST is used for sending data to the server.
        data = JSONParser().parse(request) #Parsing a requested data to be send in a server,parsing data into python data structure such as list,dict
        serializer = SnippetSerializer(data=data) # creating instance of SnippetSerializer which is responsible for validating the data received from the request.
        if serializer.is_valid(): #Checking if the data passed to the serializer is valid
            serializer.save() #if it is valid saving data using serializer.it creates a new object instance or updates an existing one in the database.
            return  JsonResponse(serializer.data, status=201) #returns a JSON response containing the serialized data from the serializer.
        return JsonResponse(serializer.errors,status=400) #returns a JSON response containing the errors from the serializer.
    
@csrf_exempt
def snippet_details(request,pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if  serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)