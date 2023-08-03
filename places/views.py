from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import Place
from .services import get_short_title


def index(request):
    places = Place.objects.all()
    features = []
    for place in places:
        features.append(
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.longtitude, place.latitude]
                },
                'properties': {
                    'title': get_short_title(place.title),
                    'placeId': place.id,
                    'detailsUrl': f'/json/{place.id}/',
                }
            }
        )

    context = {
      'type': 'FeatureCollection',
      'features': features
    }
    return render(request,
                  'places/index.html',
                  context={'value': context})


def place_detail(request, id):
    place = get_object_or_404(Place, pk=id)
    return render(request,
                  'places/place/detail.html',
                  {'place': place})


def get_json(request, id):
    place = get_object_or_404(Place, pk=id)
    place_detail = {
        'title': place.title,
        'imgs': [(settings.MEDIA_URL + i['upload'])
                 for i in list(place.images.all().values())],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.longtitude,
            'lat': place.latitude
        }
    }
    return JsonResponse(place_detail,
                        safe=False,
                        json_dumps_params={
                            'ensure_ascii': False,
                            'indent': 2,
                        })
