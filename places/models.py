from django.db import models
from django.urls import reverse


class Place(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='название')
    place_en = models.CharField(
        max_length=255,
        verbose_name='ID места'
    )
    description_short = models.TextField(
        verbose_name='краткое описание')
    description_long = models.TextField(
        verbose_name='описание')
    latitude = models.FloatField(verbose_name='Широта')
    longtitude = models.FloatField(verbose_name='Долгота')

    class Meta:
        ordering = ['title']
        verbose_name = 'экскурсия'
        verbose_name_plural = 'экскурсии'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('places:detail', args=[self.id])


class Image(models.Model):
    def image_directory_path(self, filename):
        return '{0}/{1}'.format(
            self.place.place_en,
            filename)

    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='экскурсия',
        related_name='images'
    )
    order_id = models.PositiveIntegerField(
        verbose_name='порядок',
        default=0,
        blank=False,
        null=False
    )
    upload = models.ImageField(
        upload_to=image_directory_path,
        verbose_name='загрузка фото'
        )
    class Meta:
        ordering = ['order_id']
        verbose_name = 'фото'
        verbose_name_plural = 'фото'

    def __str__(self):
        return f'{self.order_id} {self.place.title}'
