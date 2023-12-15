from django.contrib import admin
from.models import Index, Menu


class IndexAdmin(admin.ModelAdmin):
    list_display = ('about', 'service', 'booking', 'team', 'testimonial', 'contact',)

    


admin.site.register(Index, IndexAdmin)
admin.site.register(Menu)
