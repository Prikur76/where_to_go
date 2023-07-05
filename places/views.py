from django.shortcuts import render, get_object_or_404
from .models import Sight


def index(request):
    places = Sight.objects.all()
    places_details = []
    for place in places:
        places_details.append(
          {
            'title': place.title,
            'imgs': [('media/' + i) for i in place.images.all().values_list('upload', flat=True)],
            'description_short': place.description_short,
            'description_long': place.description_long,
            'coordinates': {
                'lat': place.latitude,
                'lng': place.longtitude,
            }
          }
        )
    context = {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.62, 55.793676]
          },
          "properties": {
            "title": "«Легенды Москвы",
            "placeId": "moscow_legends",
            "detailsUrl": "./places/static/moscow_legends.json"
          },
        },
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.64, 55.753676]
          },
          "properties": {
            "title": "Крыши24.рф",
            "placeId": "roofs24",
            "detailsUrl": "./places/static/roofs24.json"
          }
        }
      ]
    }

    return render(request,
                  'places/index.html',
                  context={'value': context})
