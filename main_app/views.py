from django.shortcuts import render
from django.http import HttpResponse


class Cat:
    def __init__(self, name, breed, description, age, id, picture):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age
        self.id = id
        self.picture = picture


cats = [
    Cat('Luna', 'Snow Bengal', 'Bengals are a mix of an Asian Leopard cat with a tabby cat', 8, 1, 'https://www.indiancreekbengals.com/img/kittens/snow/snow15.png'),
    Cat('Mr. Noodles', 'Scottish Fold', 'Scottish Folds are a mix between British Shorthairs and a tabby cat', 2, 2, 'https://cdn.shopify.com/s/files/1/0244/7851/5263/products/10_2_1_1024x.jpg?v=1665643467'),
    Cat('The Void', 'Black American Cat', 'Black American cats can be mixed breed, a specific breed, or no particular breed at all', 4, 3, 'https://www.rd.com/wp-content/uploads/2021/01/GettyImages-1175550351.jpg'),
    Cat('Japudji', 'Selkirk Rex', 'Selkrir Rex cats are a gene mutation from a cat of an unknown mix of breeds', 1, 4, 'https://i.imgur.com/lgeXd56.jpg')
]

# Create your views here.
def home(request):
    return render(request, 'home.html')
 

def cats_index(request):
    return render(request, 'cats/index.html', {'cats': cats})

def cats_id(request, id):
    def check_cat(cat):
        if cat.id == int(id):
            return True
        else:
            return False
    cat = list(filter(check_cat,cats))[0]
    return render(request, 'cats/details.html', {'cats': cat})