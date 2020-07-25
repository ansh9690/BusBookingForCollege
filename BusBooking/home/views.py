from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BusInfo, BookingDetails
import datetime
from django.contrib import messages
from tablib import Dataset
from django.contrib.auth.decorators import login_required
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum

MERCHANT_KEY = 'kbzk1DSbJiV_O3p5'


@login_required(login_url='/accounts/login/')
def import_file(request):
    buses = BusInfo.objects.all()
    if request.method == 'POST':
        dataset = Dataset()
        new_bus = request.FILES['myfile']
        if not new_bus.name.endswith('xlsx'):
            messages.info(request, "Wrong format")
            return render(request, 'home/import_file.html')
        imported_data = dataset.load(new_bus.read(), format='xlsx')
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
    return render(request, 'home/import_file.html', {'buses': buses})


def home(request):
    businfo = BusInfo.objects.filter(date=date.today())
    if businfo:
        return render(request, 'home/home.html', {'businfo': businfo})
    else:
        return render(request, 'home/home.html')


@login_required(login_url='/accounts/login/')
def Bookings(request):
    if request.method == "POST":
        date = datetime.date.today()
        bus_id = request.POST.get('bus_id')
        no_seats = 1
        bus = BusInfo.objects.get(id=bus_id)
        if bus:
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
            email = request.user.email
            id = book.id
            param_dict = {
                'MID': 'WorldP64425807474247',
                'ORDER_ID': str(id),
                'TXN_AMOUNT': str(price),
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',

            }
            param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
            return render(request, 'home/paytm.html', {'param_dict': param_dict})
    return render(request, 'home/home.html')


@csrf_exempt
def HandleRequest(request):

    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            messages.success(request, "order success")
        else:
            messages.info(request, response_dict['RESPMSG'])
    return render(request, 'home/paymentstatus.html', {'response': response_dict})
