from rest_framework import routers
from django.contrib import admin
from django.urls import path
from django.conf.urls import include 
from .views import ReservationViewSet


router = routers.DefaultRouter()
router.register('', ReservationViewSet)

app_name = 'reservations'

urlpatterns = [
  path('',include(router.urls)),
]