from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Vehiculo
from .serializers import VehiculoSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView

class vehiculo_create(APIView):
    def post(self, request, format=None):
        serializer = VehiculoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class vehiculo_update(APIView):
    def put(self, request, format=None):
        serializer = VehiculoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def vehiculo_read(request, id):
    if request.method == 'GET':
        objeto = get_object_or_404(Vehiculo, patente=id)
        serializer = VehiculoSerializer(objeto)
        return Response(serializer.data)

@api_view(['GET'])
def vehiculo_read_all(request):
    if request.method == 'GET':
        list = Vehiculo.objects.all()
        serializer = VehiculoSerializer(list, many=True)
        return Response(serializer.data)

@api_view(['DELETE'])
def vehiculo_delete(request, id):
    if request.method == 'DELETE':
        try:
            Vehiculo.objects.get(patente=id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Vehiculo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
