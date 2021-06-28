import json
from datetime import datetime

from django.db import connection

from rest_framework.response import Response
from rest_framework.views import APIView


class ServiceView(APIView):
    def get(self, request, date, driver):
        date_query = datetime.strptime(date, "%d-%m-%Y")
        cursor = connection.cursor()

        if driver == 'all':
            raw_query = """SELECT "api_service"."id", "api_service"."workshop_id", "api_service"."date", "api_service"."latitude", "api_service"."longitude" FROM "api_service" WHERE ("api_service"."date" AT TIME ZONE \'UTC\')::date = %s"""
            usable_sql = cursor.mogrify(raw_query, (date_query,))
        else:
            raw_query = """SELECT "api_service"."id", "api_service"."workshop_id", "api_service"."date", "api_service"."latitude", "api_service"."longitude" FROM "api_service" INNER JOIN "api_driver_services" ON ("api_service"."id" = "api_driver_services"."service_id") INNER JOIN "api_driver" ON ("api_driver_services"."driver_id" = "api_driver"."id") WHERE (("api_service"."date" AT TIME ZONE \'UTC\')::date = %s AND "api_driver"."name" = %s)"""
            usable_sql = cursor.mogrify(raw_query, (date_query, driver))
        
        cursor.execute(usable_sql)
        data = cursor.fetchall()
        json_obj = list(data)
        return Response(json_obj)
    
    def post(self, request):
        return Response({'some': 'data'})

class DriverView(APIView):
    def get(self, request):
        return Response({'some': 'data'})
