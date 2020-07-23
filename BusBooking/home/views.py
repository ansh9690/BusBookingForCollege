from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BusInfo, BookingDetails
import datetime
from django.contrib import messages

def home(request):
    businfo = BusInfo.objects.filter(date=datetime.datetime.now().strftime("%Y-%m-%d"))
    if businfo:
        return render(request, 'home/home.html', {'businfo': businfo})
    else:
        return render(request, 'home/home.html')
    
def Bookings(request):
    if request.method == "POST":
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        print(date)
        bus_id = request.POST.get('bus_id')
        no_seats = 1
        print(no_seats)
        bus = BusInfo.objects.get(sno=bus_id)
        if bus:
            if date==datetime.datetime.now().strftime("%Y-%m-%d"):
                name = request.user.username
                source = bus.source
                destination = bus.destination
                startTime = bus.startTime
                price = bus.price
                rem_seats = bus.rem_seats - int(no_seats)
                BusInfo.objects.filter(sno=bus_id).update(rem_seats=rem_seats)
                book = BookingDetails.objects.create(name=name, source=source, bus_id=bus_id, startTime=startTime,
                                            destination=destination, price=price, date=date, number_of_seats = no_seats,
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