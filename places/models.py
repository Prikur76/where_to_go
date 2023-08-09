import re

from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField


def image_directory_path(instance, filename):
    slug = instance.place.slug
    return '{0}/{1}'.format(slug, filename)


class Place(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='название')
    slug = models.SlugField(
        max_length=100,
        verbose_name='slug',
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
        ordering = ['order']
        verbose_name = 'экскурсия'
        verbose_name_plural = 'экскурсии'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('places:detail',
                       args=[self.id])

    @property
    def short_title(self):
        """Возвращает короткое название экскурсии"""
        if '«' in self.title:
            pattern = r'«([А-ЯЁа-яёA-Za-z0-9\.\s\-\„\“]+)»'
            return re.search(pattern, self.title)[1]
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='экскурсия',
        related_name='images')
    order = models.PositiveIntegerField(
        verbose_name='порядковый номер',
        blank=True, null=True)
    photo = models.ImageField(
        verbose_name='фото',
        upload_to=image_directory_path)

    class Meta:
        ordering = ['order']
        verbose_name = 'фото'
        verbose_name_plural = 'фото'

    def __str__(self):
        return f'{self.order} {self.place.title}'
