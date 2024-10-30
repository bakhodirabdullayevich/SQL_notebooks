from django.contrib import admin

from restored_volume.models import Volume, Period


# Register your models here.
class VolumeAdmin(admin.ModelAdmin):
    list_display = ('meter', 'month', 'flowmeter_volume', 'restored_volume')
    list_filter = ('month', )
    search_fields = ('meter', )


class PeriodAdmin(admin.ModelAdmin):
    list_display = ('organization', 'date')
    list_filter = ('date', )


admin.site.register(Volume, VolumeAdmin)
admin.site.register(Period, PeriodAdmin)
