from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import User, Ngo, Donor
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import NgoSignUpForm, DonorSignUpForm
from django.views.generic import CreateView
from .form import ProfileUpdateForm

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


#create delete post.
#def register(request):
    #if(request.method == 'POST'):
        ##form = RegisterForm(request.POST)
        #if form.is_valid():
            #form.save()
            #messages.success(request, f'Account Created.')
            #return redirect ('login')
    #else:
         #form = UserCreationForm()
    #return render (request, '..templates/register.html',{'form': form})

@login_required
def profile(request):
    return render(request,'../templates/profile.html')


def profileUpdate(request):
    if(request.method=='POST'):
        pform=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if pform.is_valid:
            pform.save()
            return redirect('profile')

    else:
        pform=ProfileUpdateForm(instance=request.user.profile)

    return render(request,'../templates/profileupdate.html',{'pform':pform})
