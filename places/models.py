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

    class Meta:
        verbose_name = 'экскурсия'
        verbose_name_plural = 'экскурсии'

    def __str__(self):
        return self.title


class Image(models.Model):
    def image_directory_path(self, filename):
        return 'images/{0}/{1}{2}'.format(
            self.sight.id,
            self.order_id,
            filename)

    sight = models.ForeignKey(
        Sight,
        on_delete=models.CASCADE,
        verbose_name='место',
        related_name='images'
    )
    order_id = models.PositiveIntegerField(
        verbose_name='порядок'
    )
    image = models.ImageField(
        upload_to=image_directory_path,
        verbose_name='фото'
        )
    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'фото'

    def __str__(self):
        return f'{self.order_id} {self.sight.title}'
