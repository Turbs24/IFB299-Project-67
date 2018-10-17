from django.shortcuts import render
from django.http import HttpResponse,Http404

from crcapp.models import Car
from crcapp.models import Orders
from crcapp.models import Store

def home(request):
	cars = Car.objects.all()
	return render(request, 'home.html',{'cars': cars})

	
def car_details(request, id):
	try:
		car = Car.objects.get(Car_ID=id)
	except Car.DoesNotExist:
		raise Http404('Car not found')
	return render(request, 'car_details.html', {'car':car})
	
def vehicles(request):
	cars = Car.objects.all()
	return render(request, 'vehicles.html',{'cars': cars})

def locations(request):
	Storelist = Store.objects.all()
	# Orderslist = Orderslist.order_by('Order_ReturnDate')
	return render(request, 'location.html',{'store': Storelist})