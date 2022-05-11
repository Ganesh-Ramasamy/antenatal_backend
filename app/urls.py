from django.urls import path, include
from django.contrib import admin

from . import views


urlpatterns = [
    path('end-point', views.api_end_point),
    path('authenticated-end-point', views.authenticated_end_point),

]