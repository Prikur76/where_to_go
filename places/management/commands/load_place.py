import os
import urllib

import requests
from django.core.management.base import BaseCommand
from places.get_images import download_image_from_url
from places.models import Place, Image
from slugify import slugify


class Command(BaseCommand):
    help = 'Загружает описание экскурсии из файла'

    def add_arguments(self, parser):
        parser.add_argument(
            'link', type=str,
            help='Ссылка на файл .json с описанием экскурсии'
        )

    def handle(self, *args, **kwargs):
        link = kwargs['link']
        response = requests.get(link)
        response.raise_for_status()
        place = response.json()
        created_place, status = Place.objects.get_or_create(
            title=place['title'],
            defaults={
                'slug': slugify(place['title']),
                'description_short': place['description_short'],
                'description_long': place['description_long'],
                'latitude': place['coordinates']['lat'],
                'longtitude': place['coordinates']['lng']
            }
        )
        if status:
            self.stdout.write(
                self.style.SUCCESS(
                    f'Экскурсия {created_place.title} c ID '
                    f'{created_place.id} создана!'
                )
            )

        for num, img_url in enumerate(place['imgs'], start=1):
            image_name = os.path.basename(
                urllib.parse.urlsplit(img_url).path)
            download_image_from_url(
                img_url,
                os.path.join('media', created_place.slug),
                image_name
            )
            created_image, img_status = Image.objects.get_or_create(
                photo=os.path.join(created_place.slug, image_name),
                defaults={
                    'place': created_place,
                    'order': num,
                }
            )
            if img_status:
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Фото {image_name} создано!'
                    )
                )
