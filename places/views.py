from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import Place


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
                    'title': place.short_title,
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


def get_json(request, id):
    place = get_object_or_404(Place, pk=id)
    place_detail = {
        'title': place.title,
        'imgs': [(settings.MEDIA_URL + i['photo'])
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
