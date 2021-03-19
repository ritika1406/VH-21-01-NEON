from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import User, Ngo, Donor
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import NgoSignUpForm, DonorSignUpForm
from django.views.generic import CreateView
#from .filters import JobFilter


# Create your views here.
def register(request):
    #return render_to_response('register.html')
    
    return render(request, '../templates/register.html')

#def index(request):
   # myFilter = JobFilter(request.GET, queryset="name")
    
    #context = {'myFilter': myFilter}

    #return render(request, '../templates/index.html') 
def home(request):
    context={
        'variable': "this is sent"
    }
    
    return render(request, '../templates/home.html', context) 
        

class donor_register(CreateView):
     model = User
     form_class = DonorSignUpForm
     template_name = '../templates/donor_register.html'

     #def vaidation(self,form):
         #user= form.save()
         #login(self.request,user)
         #return redirect('#')
    

class ngo_register(CreateView):
     model = User
     form_class = NgoSignUpForm
     template_name = '../templates/ngo_register.html'