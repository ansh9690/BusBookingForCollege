from django.contrib import admin
from .models import BusInfo, BookingDetails
from import_export.admin import ImportExportModelAdmin


@admin.register(BusInfo)
class BusInfoAdmin(ImportExportModelAdmin):
    pass
    # list_display = ('id', 'source', 'destination', 'startTime',
    #                 'price', 'duration', 'total_seats', 'rem_seats', 'date')


@admin.register(BookingDetails)
class BookingDetailsAdmin(ImportExportModelAdmin):
    pass
    # list_display = ('name',)
