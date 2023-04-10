from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponse

from .models import Cat

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
    return render(request, 'cats/details.html', {'cats': cats})