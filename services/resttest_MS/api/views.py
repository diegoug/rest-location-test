import json
from math import radians, cos, sin, asin, sqrt
from datetime import datetime

from django.db import connection

from rest_framework.response import Response
from rest_framework.views import APIView

def get_distance(pint_a, point_b):
    lat1 = float(pint_a['latitude'])
    lon1 = float(pint_a['longitude'])
    lat2 = float(point_b['latitude'])
    lon2 = float(point_b['longitude'])
    distance = 0.0
    if lat1 != lat2 and lon1 != lon2:
        # calculation
        try:
            # convert decimal degrees to radians
            rlon1, rlat1, rlon2, rlat2 = map(radians, [lon1, lat1, lon2, lat2])
            # haversine formula
            dlon = rlon2 - rlon1
            dlat = rlat2 - rlat1
            a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
            c = 2 * asin(sqrt(a))
            distance = 6367 * c
        except:
            pass
    return distance

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
        cursor.close()
        json_obj = list(data)
        return Response(json_obj)
    
    def post(self, request):
        return Response({'some': 'data'})

class DriverView(APIView):
    def get(self, request):
        query_location = {
            'latitude': request.query_params['latitude'],
            'longitude': request.query_params['longitude']}
        near_service = tuple()
        near_driver = tuple()
        near_service_distance = 0.0
        date_query = datetime.strptime(request.query_params['date'], "%d-%m-%Y")
        raw_query = """SELECT "api_driver"."id", "api_driver"."name" FROM "api_driver" INNER JOIN "api_driver_services" ON ("api_driver"."id" = "api_driver_services"."driver_id") INNER JOIN "api_service" ON ("api_driver_services"."service_id" = "api_service"."id") WHERE ("api_service"."date" AT TIME ZONE \'UTC\')::date = %s"""
        cursor = connection.cursor()
        usable_sql = cursor.mogrify(raw_query, (date_query,))
        cursor.execute(usable_sql)
        data = cursor.fetchall()
        cursor.close()
        for driver in data:
            raw_query = """SELECT "api_service"."id", "api_service"."workshop_id", "api_service"."date", "api_service"."latitude", "api_service"."longitude" FROM "api_service" WHERE "api_service"."id" = %s"""
            cursor = connection.cursor()
            second_usable_sql = cursor.mogrify(raw_query, (driver[0],))
            cursor.execute(second_usable_sql)
            services = cursor.fetchall()
            for service in services:
                if not near_service:
                    near_service = service
                    near_driver = driver
                    point = {
                        'latitude': service[3],
                        'longitude': service[4]}
                    near_service_distance = get_distance(query_location, point)
                else:
                    point = {
                        'latitude': service[3],
                        'longitude': service[4]}
                    service_distance = get_distance(query_location, point)
                    if service_distance < near_service_distance:
                        near_service = service
                        near_driver = driver
            cursor.close()
        json_obj = list(near_driver)
        return Response(json_obj)
