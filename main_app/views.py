from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.http import HttpResponse

from .models import Cat, Play_Date

from .forms import AppointmentForm

# Create your views here.

class CreateCat(CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']
    success_url = '/cats/'

class UpdateCat(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']

class DeleteCat(DeleteView):
    model = Cat
    success_url = '/cats/'

def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})



def home(request):
    return render(request, 'home.html')
 

def cats_details(request, cat_id):
    cats = Cat.objects.get(id=cat_id)
    no_play_date = Play_Date.objects.exclude(id__in = cats.play.all().values_list('id'))
    appointment_form = AppointmentForm()
    return render(request, 'cats/details.html', {'cats': cats, 'appointment_form': appointment_form, 'play': no_play_date})

def add_appointment(request, cat_id):
    form = AppointmentForm(request.POST)
    if form.is_valid():
        new_appointment = form.save(commit=False)
        new_appointment.cat_id = cat_id
        new_appointment.save()
    return redirect('details', cat_id=cat_id)

def assoc_date(request, cat_id, date_id):
    Cat.objects.get(id=cat_id).play.add(date_id)
    return redirect('details', cat_id=cat_id)

class PlayList(ListView):
    model = Play_Date


class PlayDetail(DetailView):
    model = Play_Date


class PlayCreate(CreateView):
    model = Play_Date
    fields = '__all__'


class PlayUpdate(UpdateView):
    model = Play_Date
    fields = ['name']


class PlayDelete(DeleteView):
    model = Play_Date
    success_url = '/play/'