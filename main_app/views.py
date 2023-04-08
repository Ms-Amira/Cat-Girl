from django.shortcuts import render
from django.http import HttpResponse


class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age


cats = [
    Cat('Luna', 'Snow Bengal', 'Bengals are a mix of an Asian Leopard cat with a tabby cat', 8),
    Cat('Mr Noodles', 'Scottish Fold', 'Scottish Folds are a mix between British Shorthairs and a tabby cat', 2),
    Cat('The Void', 'Black American Cat', 'Black American cats can be mixed breed, a specific breed, or no particular breed at all', 4),
    Cat('Japudji', 'Selkirk Rex', 'Selkrir Rex cats are a gene mutation from a cat of an unknown mix of breeds', 1)
]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    return render(request, 'cats/index.html', {'cats': cats})