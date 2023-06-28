from django.contrib import admin
from .models import Sight


# Register your models here.
@admin.register(Sight)
class SightAdmin(admin.ModelAdmin):
    list_display = ('title', )
    fieldsets = (
        (None, {
            'fields': (
                'title',
                'description_short',
                'description_long',
                ('longtitude', 'latitude'),
                'imgs')
        }),
    )
