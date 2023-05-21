from django.urls import path
from . import views


urlpatterns = [
    path('status/', views.status_check, name='status_check'),
    path('status/get_result/', views.get_result, name='get_result'),
    ]