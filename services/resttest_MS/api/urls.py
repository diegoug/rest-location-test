
from django.urls import path, re_path

from .views import ServiceView, DriverView

urlpatterns = [
    re_path(
        r'^v1/services/(?P<date>[\w.@+-]+)/(?P<driver>[\w.@+-]+)/$',
        ServiceView.as_view(),
        name='service_driver_date_api'),
    path(
        'v1/driver/',
        DriverView.as_view(),
        name='driver_api'),
]
