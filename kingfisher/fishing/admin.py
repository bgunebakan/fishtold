# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from . import models
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }

class PersonnelAdmin(admin.ModelAdmin):
     list_display = ('name','surname','personnel_type')

class VesselAdmin(admin.ModelAdmin):
     list_display = ('name','hull_length')

class FishingAdmin(admin.ModelAdmin):
     list_display = ('vessel','start_date','end_date')

class BoxAdmin(admin.ModelAdmin):
     list_display = ('rfid_no','fishing','company','fish_type')

class LocationsAdmin(admin.ModelAdmin):
     list_display = ('fishing','position','created_date')

admin.site.register(models.Personnel,PersonnelAdmin)
admin.site.register(models.Vessel,VesselAdmin)
admin.site.register(models.Personnel_type)
admin.site.register(models.Fishing,FishingAdmin)
admin.site.register(models.Locations,LocationsAdmin)
admin.site.register(models.Company)
admin.site.register(models.Fish_type)
admin.site.register(models.Box,BoxAdmin)
admin.site.register(models.Box_action)
admin.site.register(models.Harbor)
admin.site.register(models.Rental,RentalAdmin)
