from rest_framework import routers
from django.contrib import admin
from django.urls import path
from django.conf.urls import include 
from .views import StudentViewSet


router = routers.DefaultRouter()
router.register('', StudentViewSet)

app_name = 'student'

urlpatterns = [
  path('',include(router.urls)),
]


