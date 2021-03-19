from django.shortcuts import render, HttpResponse
from datetime import datetime
#from home.models import Contact
from django.contrib import messages
# Create your views here.
def front(request):
    context={
        'variable': "this is sent"
    }
    
    return render(request, 'front.html', context)
def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is About page")

    #return HttpResponse("this is Services page")
def Contact(request):
    
    return render(request, 'Contact.html')
    #return HttpResponse("this is Contact page")
