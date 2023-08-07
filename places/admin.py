from adminsortable2.admin import SortableTabularInline, SortableAdminMixin
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.safestring import mark_safe, format_html

from .models import Place, Image


class ManagerAdminSite(AdminSite):
    site_header = 'Manager admin'


class ImageTabularInline(SortableTabularInline):
    model = Image
    extra = 0
    fields = ['image', 'get_preview']
    readonly_fields = ['get_preview']
    raw_id_fields = ['place']

    def get_preview(self, obj):
        if obj.upload:
            return format_html('<img src="{}" width="100"/>',
                               mark_safe(obj.upload.url))

    get_preview.short_description = 'миниатюра'


class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [
        ImageTabularInline
    ]
    list_display = ['title', 'slug', 'latitude', 'longtitude']
    search_fields = ['title',]
    list_filter = ('slug', )
    list_editable = ['latitude', 'longtitude']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': (
                ('title', 'slug'),
                'description_short',
                'description_long',
                ('latitude', 'longtitude'),
            )
        }),
    )
    save_on_top = True


class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'place', 'image',
                    'preview', 'order_number']
    list_filter = ('place__slug', )
    list_display_links = ['id', 'preview']
    readonly_fields = ['preview', ]

    def preview(self, obj):
        if obj.upload:
            return format_html('<img src="{}" width="200"/>',
                               mark_safe(obj.upload.url))

    preview.short_description = 'миниатюра'

format_html("{} <b>{}</b> {}",
            mark_safe(some_html), some_text, some_other_text)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Image, ImageAdmin)

manageradmin = ManagerAdminSite(name='manageradmin')
manageradmin.register(Place, PlaceAdmin)
