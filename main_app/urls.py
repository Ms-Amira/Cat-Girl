from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cats/', views.cats_index, name='index'),
    path('cats/<int:cat_id>/', views.cats_details, name='details')
]