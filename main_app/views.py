from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponse

from .models import Cat

from .forms import AppointmentForm

# Create your views here.

class CreateCat(CreateView):
    model = Cat
    fields = '__all__'
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
    print(cats.appointment_set.all())
    appointment_form = AppointmentForm()
    return render(request, 'cats/details.html', {'cats': cats, 'appointment_form': appointment_form})

def add_appointment(request, cat_id):
    form = AppointmentForm(request.POST)
    if form.is_valid():
        new_appointment = form.save(commit=False)
        new_appointment.cat_id = cat_id
        new_appointment.save()
    return redirect('details', cat_id=cat_id)