from django.db import models


# Create your models here.
class Sight(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='название')
    placeId = models.CharField(
        max_length=255,
        verbose_name='placeId'
    )
    short_description = models.TextField(
        verbose_name='краткое описание')
    long_description = models.TextField(
        verbose_name='описание')
    longtitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')

    class Meta:
        verbose_name = 'экскурсия'
        verbose_name_plural = 'экскурсии'

    def __str__(self):
        return self.title


class Image(models.Model):
    def image_directory_path(self, filename):
        return 'images/{0}/{1}'.format(
            self.sight.id,
            filename)

    sight = models.ForeignKey(
        Sight,
        on_delete=models.CASCADE,
        verbose_name='экскурсия',
        related_name='images'
    )
    order_id = models.PositiveIntegerField(
        verbose_name='порядок'
    )
    upload = models.ImageField(
        upload_to=image_directory_path,
        verbose_name='загрука фото'
        )
    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'фото'

    def __str__(self):
        return f'{self.order_id} {self.sight.title}'
