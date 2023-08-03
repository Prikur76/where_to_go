import os

from django.core.management.base import BaseCommand
from places.models import Place, Image
from places.services import download_image_from_url, get_place_from_link


class Command(BaseCommand):
    help = 'Загружает описание экскурсии из файла'

    def add_arguments(self, parser):
        parser.add_argument(
            'link', type=str,
            help='Ссылка на файл .json с описанием экскурсии'
        )

    def handle(self, *args, **kwargs):
        link = kwargs['link']
        place = get_place_from_link(link)
        created_place, status = Place.objects.get_or_create(
            title=place['title'],
            slug=place['slug'],
            description_short=place['description_short'],
            description_long=place['description_long'],
            latitude=place['coordinates']['lat'],
            longtitude=place['coordinates']['lng']
        )
        if status:
            self.stdout.write(
                self.style.SUCCESS(
                    f'Экскурсия {created_place.title} c ID {created_place.id} создана!'
                )
            )

        for num, img_url in enumerate(place['imgs'], start=1):
            image_name = download_image_from_url(
                img_url,
                os.path.join('media', created_place.slug)
            )
            created_image, img_status = Image.objects.get_or_create(
                place=created_place,
                order_id=num,
                upload=os.path.join(created_place.slug, image_name)
            )
            if img_status:
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Фото {image_name} создано!'
                    )
                )
