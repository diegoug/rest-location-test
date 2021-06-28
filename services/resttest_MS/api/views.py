import json
from datetime import datetime

from django.db import connection
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView


class ServiceView(APIView):
    def get(self, request, date):
        raw_query = """SELECT "api_service"."id", "api_service"."workshop_id", "api_service"."date", "api_service"."latitude", "api_service"."longitude" FROM "api_service" WHERE ("api_service"."date" AT TIME ZONE \'UTC\')::date = %s"""
        date_query = datetime.strptime(date, "%d-%m-%Y")
        cursor = connection.cursor()
        usable_sql = cursor.mogrify(raw_query, (date_query,))
        cursor.execute(usable_sql)
        data = cursor.fetchall()
        json_obj = list(data)
        return Response(json_obj)
    
    def post(self, request):
        return Response({'some': 'data'})

class DriverView(APIView):
    def get(self, request):
        return Response({'some': 'data'})
