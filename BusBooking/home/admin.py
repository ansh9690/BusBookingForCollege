from django.contrib import admin
from .models import BusInfo, BookingDetails
from import_export.admin import ImportExportModelAdmin

admin.site.register(BookingDetails)


@admin.register(BusInfo)
class BusInfoAdmin(ImportExportModelAdmin):
    list_display = ('id', 'source', 'destination', 'startTime', 'price', 'duration', 'total_seats', 'rem_seats', 'date')
