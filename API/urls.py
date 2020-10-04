from django.urls import path
from . import views

urlpatterns = [
    path('', views.sparta),
    path('users/', views.users),
    path('events/', views.events),
    path('times/', views.times),
    path('write_event/', views.write_event),
    path('write_user/', views.write_user),
    path('write_time/', views.write_time),
    path('delete_event/', views.delete_event),
    path('delete_user/', views.delete_user),
    path('delete_time/', views.delete_time),
    path('update_user/', views.update_user),
    path('update_event/', views.update_event),
    path('update_time/', views.update_time),
]