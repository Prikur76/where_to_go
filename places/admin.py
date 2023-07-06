from django.contrib import admin
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]
    list_display = ('title', )
    fieldsets = (
        (None, {
            'fields': (
                ('title', 'place_en'),
                'description_short',
                'description_long',
                ('latitude', 'longtitude'),
            )
        }),
    )
    save_on_top = True


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_filter = ('place__place_en', )
