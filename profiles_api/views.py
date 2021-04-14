from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from rest_framework import status
from profiles_api import serializers
from rest_framework  import viewsets
class HelloApiView(APIView):

    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def put(self, request, pk=None):
        """handle and the updating"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """update partially the fields in the object, will modify only specific part of object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """viewsets representation"""
    serializer_class = serializers.HelloSerializer 
    def list(self, request):
        """return a hello message"""
        a_viewset =[
                'users action (lists,Create,retrive,update,partial_update)',
                'AUtomatically maps to urls using routers',
                'provides more funtionality then apiview with very shortcode',
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
    def retrive(self,request,pk=None):
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        return Response({'http_method':'UPDATE'})

    def partial_update(self,request,pk=None):
        return Response({'http_method':'PARTIAL_UPDATE(PATCH)'})
    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})

