from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'places'

urlpatterns = [
    path('', views.index, name='index'),
    path('places/<int:id>/', views.place_detail, name='detail'),
    path('json/<int:id>/', views.get_json, name='json'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)