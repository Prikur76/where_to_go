from django.db import models


# Create your models here.
class Sight(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='название')
    description_short = models.TextField(
        verbose_name='краткое описание')
    description_long = models.TextField(
        verbose_name='описание')
    longtitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')
    imgs = models.ImageField(
        upload_to='images/',
        verbose_name='Фото', blank=True, null=True)

    class Meta:
        verbose_name = 'достопримечательность'
        verbose_name_plural = 'достопримечательности'
    def __str__(self):
        return self.title
