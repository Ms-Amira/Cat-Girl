from django.shortcuts import render
from django.http import HttpResponse


class Cat:
    def __init__(self, name, breed, description, age, id):
        self.name = name
        self.breed = breed
        self.age = age
        self.id = id
        self.description = description


cats = [
    Cat('Luna', 'Snow Bengal', 'Bengals are a mix of an Asian Leopard cat with a tabby cat', 8, 1),
    Cat('Mr. Noodles', 'Scottish Fold', 'Scottish Folds are a mix between British Shorthairs and a tabby cat', 2, 2),
    Cat('The Void', 'Black American Cat', 'Black American cats can be mixed breed, a specific breed, or no particular breed at all', 4, 3),
    Cat('Japudji', 'Selkirk Rex', 'Selkrir Rex cats are a gene mutation from a cat of an unknown mix of breeds', 1, 4)
]

# Create your views here.
def home(request):
    return render(request, 'home.html')
 

def cats_index(request):
    return render(request, 'cats/index.html', {'cats': cats})

def cats_id(request, id):
    def check_cat(cat):
        if cat.id == int(id):
            print('cat')
            return True
        else:
            return False
    cat = list(filter(check_cat,cats))[0]
    return render(request, 'cats/details.html', {'cats': cat})