from django.contrib import admin
from django.urls import path,include
from backend.views import *
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('', index, name='index'),
    path('post/', ocr_endpoint, name='ocr_endpoint'),
    path('getall/', getData, name='getData'),
    path('get/<str:pk>/', get_result, name='get_result'),
    path('update/<str:pk>/', update_result, name='update_result'),
    path('delete/<str:pk>/', csrf_exempt(delete_result), name='delete_result')
]