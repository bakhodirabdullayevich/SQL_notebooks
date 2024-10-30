from django.contrib import admin

from orifice_plate.models import OrificePlate


# Register your models here.
class OrificePlateAdmin(admin.ModelAdmin):
    list_display = ('number', 'd20', 'pressure', 'temperature', 'installed_date', 'installed')
    list_filter = ('meter', 'installed', 'p_unit', 'dp_unit')
    search_fields = ('number', 'd20', 'pressure', 'temperature')
    date_hierarchy = 'installed_date'


admin.site.register(OrificePlate, OrificePlateAdmin)