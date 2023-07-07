from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableTabularInline, SortableAdminMixin

from .models import Place, Image


class ImageTabularInline(SortableTabularInline):
    model = Image
    extra = 0
    fields = ['upload', 'get_preview']
    readonly_fields = ['get_preview']
    raw_id_fields = ['place']

    def get_preview(self, obj):
        if obj.upload:
            return mark_safe('<img src="%s" width="100"/>' % obj.upload.url)

    get_preview.short_description = 'миниатюра'


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin,admin.ModelAdmin):
    inlines = [
        ImageTabularInline
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
    fields = ['place', 'upload', 'order_id']
    list_display = ['id', 'place', 'preview', 'order_id' ]
    list_filter = ('place__place_en', )
    list_display_links = ['id', 'preview']
    readonly_fields = ['preview',]

    def preview(self, obj):
        if obj.upload:
            return mark_safe('<img src="%s" width="200"/>' % obj.upload.url)

    preview.short_description = 'миниатюра'
