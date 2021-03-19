
from django.contrib.auth.forms import UserCreationForm

from .models import Ngo, Donor, User
from django import forms


class DonorSignUpForm(UserCreationForm):
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    phone_number = forms.CharField(required = True)

    #class Meta(UserCreationForm):
       # model = User
        #fields = '__all__'
        

    #@transaction.atomic
    #def data_save(self):
        #user = super().save(commit=False)
        #user.is_student = True
        #user.first_name = self.cleaned_data.get('first_name')
        #user.last_name = self.cleaned_data.get('last_name')
        #user.save()
        #student = Student.objects.create(user=user)
        #student.phone_number = self.cleaned_data.get('phone_number')
        #student.save()
        #return user


class NgoSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    faculty_id = forms.CharField(required=True)
 
    #class Meta(UserCreationForm):
        #model = User
        #fields = '__all__'
    
    #@transaction.atomic
    #def data_save(self):
        #user = super().save(commit=False)
        #user.is_faculty = True
        #user.is_staff = True
        #user.first_name = self.cleaned_data.get('first_name')
        #user.last_name = self.cleaned_data.get('last_name')
        #user.save()
        #faculty = Faculty.objects.create(user=user)
        #faculty_phone_number = self.cleaned_data.get('phone_number')
        #faculty_id = self.cleaned_data.get('faculty')
        #faculty.save()
        #return user