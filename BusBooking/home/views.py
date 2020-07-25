from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BusInfo, BookingDetails
import datetime
from django.contrib import messages
from .resources import BusInfoResources
from tablib import Dataset


def import_file(request):
    if request.method == 'POST':
        busresources = BusInfoResources()
        dataset = Dataset()
        new_bus = request.FILES['myfile']
        if not new_bus.name.endswith('xlsx'):
            messages.info(request, "Wrong format")
            return render(request, 'home/import_file.html')
        imported_data =dataset.load(new_bus.read(), format='xlsx')
        for data in imported_data:
            value = BusInfo(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
            )
            value.save()
            messages.success(request, "Uploaded file")
    return render(request, 'home/import_file.html')


def home(request):
    businfo = BusInfo.objects.filter(date=datetime.datetime.now().strftime("%Y-%m-%d"))
    if businfo:
        return render(request, 'home/home.html', {'businfo': businfo})
    else:
        return render(request, 'home/home.html')


def Bookings(request):
    if request.method == "POST":
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        # print(date)
        bus_id = request.POST.get('bus_id')
        no_seats = 1
        # print(no_seats)
        bus = BusInfo.objects.get(id=bus_id)
        if bus:
            if date == datetime.datetime.now().strftime("%Y-%m-%d"):
                name = request.user.username
                source = bus.source
                destination = bus.destination
                startTime = bus.startTime
                price = bus.price
                rem_seats = bus.rem_seats - int(no_seats)
                BusInfo.objects.filter(id=bus_id).update(rem_seats=rem_seats)
                book = BookingDetails.objects.create(name=name, source=source, bus_id=bus_id, startTime=startTime,
                                                     destination=destination, price=price, date=date,
                                                     number_of_seats=no_seats,
                                                     status='BOOKED')
                book.save()
                return render(request, 'home/bookings.html', locals())
            else:
                # print(bus.date)
                # print(datetime.datetime.now().strftime("%Y-%m-%d"))
                return HttpResponse("Enter Today date")
    return render(request, 'home/home.html')


def AmountPay(request):
    messages.success(request, "Payment successfully")
    return redirect("home:home")
