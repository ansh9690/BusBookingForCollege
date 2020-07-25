from django.db import models


class BusInfo(models.Model):
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    startTime = models.CharField(max_length=10)
    price = models.IntegerField(default=10)
    duration = models.CharField(max_length=30)
    total_seats = models.IntegerField(default=0)
    rem_seats = models.IntegerField(default=0)
    date = models.DateField(auto_now=False)

    def __str__(self):
        return f'From {self.source} to {self.destination}'

    class Meta:
        verbose_name_plural = "Bus Information"


class BookingDetails(models.Model):
    BOOKED = 'B'

    TICKET_STATUSES = ((BOOKED, 'Booked'),)
    bus_id = models.CharField(max_length=25)
    name = models.CharField(max_length=30)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    startTime = models.CharField(max_length=10)
    number_of_seats = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    date = models.DateField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Booking Details"
