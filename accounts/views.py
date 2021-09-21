from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes

# Create your views here.

def home(request):
<<<<<<< Updated upstream
	return render(request, 'accounts/dashboard.html')

def products(request):
	return render(request, 'accounts/products.html')

def customer(request):
	return render(request, 'accounts/customer.html')
=======
	return render( request, 'accounts/dashboard.html' )


def products(request):
	return render( request, 'accounts/products.html' )


def customer(request):
	return render( request, 'accounts/customer.html' )
>>>>>>> Stashed changes
