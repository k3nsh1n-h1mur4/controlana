from django.contrib import admin

from .models import controlModel

class controlAdmin(admin.ModelAdmin):
    #fields = ['ppta, fecha, aspirante', 'categoria']
    list_display = ["n_prop", "f_prop", "n_asp", "propone", "tel", "zona", "categoria"]
    search_fields = ["n_prop", "n_asp", "propone"]

admin.site.register(controlModel, controlAdmin)
