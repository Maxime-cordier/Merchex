from django.shortcuts import render
from django.http import HttpResponse
from listing.models import Band, Listing

def hello_world(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})

def about(request):
    return render(request, 'listings/about.html')

def listings(request):
    listing = Listing.objects.all()
    return render(request, 'listings/listings.html', {'listings': listing})

def contact(request):
    return render(request, 'listings/contact.html')

