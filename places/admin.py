from django.contrib import admin
from .models import Sight, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(Sight)
class SightAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]
    list_display = ('title', )
    fieldsets = (
        (None, {
            'fields': (
                ('title', 'place_id'),
                'description_short',
                'description_long',
                ('longtitude', 'latitude'),
            )
        }),
    )
    save_on_top = True


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_filter = ('sight__place_id', )
