from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
""""
#The SnippetList class is defined as a subclass of APIView. It represents the view for listing all snippets.
class SnippetList(APIView): 
    def get(self,request, format = None): #The get method is overridden to handle GET requests to the view.
        snippets = Snippet.objects.all() #assigning models objects to a snippets variable
        serializer = SnippetSerializer(snippets, many=True) #Serializing the snippets variable,which contain Snippets model object and many=true means a model contains multiple of objects and it is also used for validation
        return Response(serializer.data) #returning a response of a request
    def post(self,request, format=None): #The post method is overridden to handle POST requests to the view.
         serializer = SnippetSerializer(data=request.data) # creating instance of SnippetSerializer which is responsible for validating the data received from the request.
         if serializer.is_valid(): #Checking if the data passed to the serializer is valid
            serializer.save() #if it is valid saving data using serializer.it creates a new object instance or updates an existing one in the database.
            return Response(serializer.data, status=status.HTTP_201_CREATED) #returns a JSON response containing the serialized data from the serializer.
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) #returns a JSON response containing the errors from the serializer.
#The SnippetDetails class is defined as a subclass of APIView. It represents the view for retrieving, updating, and deleting a specific snippet.
class SnippetDetails(APIView):
    def get_object(self,pk):
        try:
            return Snippet.objects.get(pk=pk)

        except Snippet.DoesNotExist:
            raise Http404
    
    def get(self,request,pk, format=None): #The get method is overridden to handle GET requests to retrieve a specific snippet.
        snippet = self.get_object(pk) #calling the get_object method to retrieve the snippet object with the provided primary key.
        serializer = SnippetSerializer(snippet) #Serializing the snippet object
        return Response(serializer.data)
    
    def put(self,request,pk,format=None): #The put method is overridden to handle PUT requests to update a specific snippet.
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None): 
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
"""

#--Using mixins--

class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.create(request, *args,**kwargs)
    
class SnippetDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs    )

