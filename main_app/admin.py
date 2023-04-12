from django.contrib import admin

from .models import Cat, Appointment, Play_Date
# Register your models here.
admin.site.register(Cat)
admin.site.register(Appointment)
admin.site.register(Play_Date)