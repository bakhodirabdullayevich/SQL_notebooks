from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Organization, Object, ObjectType, FlowMeterType, Meter, FlowMeterSertificate


class ObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'object_type', 'region', 'address')
    list_filter = ('organization', 'object_type', 'region')
    search_fields = ('name', 'address')


class MeterAdmin(admin.ModelAdmin):
    list_display = ('meter_id', 'object', 'name', 'diameter', 'flow_meter_type')
    list_filter = ('organization', 'flow_meter_type', 'contractor')
    search_fields = ('object', 'name', 'owner')


class FlowMeterSertificateAdmin(admin.ModelAdmin):
    list_display = ('meter', 'number', 'date_start', 'url_sertificate', 'is_active')
    list_filter = ('date_start', 'is_active')
    search_fields = ('meter', 'number', 'date_start')



admin.site.register(Organization)
admin.site.register(ObjectType)
admin.site.register(Object, ObjectAdmin)
admin.site.register(FlowMeterType)
admin.site.register(Meter, MeterAdmin)
admin.site.register(FlowMeterSertificate, FlowMeterSertificateAdmin)

