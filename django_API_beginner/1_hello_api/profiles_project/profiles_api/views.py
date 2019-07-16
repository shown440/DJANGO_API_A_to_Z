from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers


# Create your views here.
class HelloApiView(APIView):
    """ Test Api View. """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of APIView features. """

        an_apiview = [
            'Use HTTP methods as functon (get, post, patch, put, delete)',
            'It is similer to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({"message": "Hello!", "an_apiview": an_apiview})

    def post(self, request):
        """ Post / Create a hello message with our name. """

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {0}".format(name)

            return Response({"message": message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, pk=None):
        """ PUT is for Updating an object. """

        return Response({"method": "put"})

    def patch(self, request, pk=None):
        """ PATCH request, Only update the provided fields on the request. """

        return Response({"method": "patch"})

    def delete(self, request, pk=None):
        """ DELETE is used for delete an object """

        return Response({"method": "delete"})



class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ This list will Return a hello message. """

        a_viewst = [
            'Uses action (list, create, retrive, update, partial_update)',
            'Automatically maps to URLs using Routers.',
            'Provides more functionality with less code.'
        ]

        return Response({"message": "Hello!", "a_viewset": a_viewst})

    def create(self, request):
        """ Create a new Hello message. """

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get("name")
            message = "Hello {0}".format(name)

            return Response({"message": message, "http_method": "POST"})
        return Response({"http_method": "POST", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ Handles getting a object by its ID. """

        return Response({"http_method": "GET"})

    def update(self, request, pk=None):
        """ Handle updating an object. """

        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """ handle updating part of a object. """

        return Response({"http_method": "PATCH"})

    def destroy(self, request, pk=None):
        """ handle deleting/ destroying an object. """

        return Response({"http_method": "DELETE"})
    

    