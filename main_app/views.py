from django.shortcuts import render
from django.http import HttpResponse

from .models import Cat

# Create your views here.
def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})



def home(request):
    return render(request, 'home.html')
 

def cats_details(request, cat_id):
    cats = Cat.objects.get(id=cat_id)
    return render(request, 'cats/details.html', {'cats': cats})