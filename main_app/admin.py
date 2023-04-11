from django.contrib import admin

from .models import Cat, Appointment
# Register your models here.
admin.site.register(Cat)
admin.site.register(Appointment)