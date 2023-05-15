from django.contrib import admin

from .models import controlModel

class controlAdmin(admin.ModelAdmin):
    #fields = ['ppta, fecha, aspirante', 'categoria']
    list_display = ["ppta", "fecha", "aspirante", "categoria"]
    search_fields = ["ppta", "aspirante", "propone"]

admin.site.register(controlModel, controlAdmin)
