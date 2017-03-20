from django.contrib import admin

from .models import Poll, Location, SelectedLocations, Choice

admin.site.register(Poll)
admin.site.register(Location)
admin.site.register(SelectedLocations)
admin.site.register(Choice)
