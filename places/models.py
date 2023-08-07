from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField


def image_directory_path(instance, filename):
    return '{0}/{1}'.format(
        instance.place.slug, filename)

class Place(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='название')
    slug = models.SlugField(
        max_length=100,
        verbose_name='ID места',
        unique=True)
    description_short = models.TextField(
        verbose_name='краткое описание',
        null=True, blank=True)
    description_long = HTMLField(
        verbose_name='описание',
        null=True, blank=True)
    latitude = models.FloatField(verbose_name='Широта')
    longtitude = models.FloatField(verbose_name='Долгота')
    order = models.PositiveIntegerField(
        verbose_name='порядок',
        blank=True, null=True)

    class Meta:
        ordering = ['my_order']
        verbose_name = 'экскурсия'
        verbose_name_plural = 'экскурсии'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('places:detail',
                       args=[self.id])


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='экскурсия',
        related_name='images')
    order_number = models.PositiveIntegerField(
        verbose_name='порядковый номер',
        blank=True, null=True)
    image = models.ImageField(
        upload_to=image_directory_path,
        verbose_name='загрузка фото')

    class Meta:
        ordering = ['order_id']
        verbose_name = 'фото'
        verbose_name_plural = 'фото'

    def __str__(self):
        return f'{self.order_id} {self.place.title}'
