from django.contrib import admin
from .models import User, Ngo, Donor
# Register your models here.
admin.site.register(User)
admin.site.register(Ngo)
admin.site.register(Donor)