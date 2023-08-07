from django.urls import path

from . import views


app_name = 'places'

urlpatterns = [
    path('', views.index, name='index'),
    path('json/<int:id>/', views.get_json, name='get_json'),
]
