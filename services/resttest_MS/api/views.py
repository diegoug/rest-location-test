from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class ServiceView(APIView):
    def get(self, request):
        return Response({'some': 'data'})
    
    def post(self, request):
        return Response({'some': 'data'})

class DriverView(APIView):
    def get(self, request):
        return Response({'some': 'data'})
