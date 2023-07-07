from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
    fields = ['upload', 'get_preview', 'order_id']
    readonly_fields = ['get_preview']

    def get_preview(self, obj):
        if obj.upload:
            return mark_safe('<img src="%s" width="100"/>' % obj.upload.url)

    get_preview.short_description = 'миниатюра'


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
    readonly_fields = ['preview',]

    def preview(self, obj):
        if obj.upload:
            return mark_safe('<img src="%s" width="200"/>' % obj.upload.url)

    preview.short_description = 'миниатюра'
