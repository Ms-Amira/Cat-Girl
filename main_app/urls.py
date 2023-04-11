from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cats/', views.cats_index, name='index'),
    path('cats/<int:cat_id>/', views.cats_details, name='details'),
    path('cats/create/', views.CreateCat.as_view(), name='create_cat'),
    path('cats/<int:pk>/update/', views.UpdateCat.as_view(), name='cats_update'),
    path('cats/<int:pk>/delete/', views.DeleteCat.as_view(), name='cats_delete'),
    path('cats/<int:cat_id>/add_appointment/', views.add_appointment, name='add_appointment'),

]