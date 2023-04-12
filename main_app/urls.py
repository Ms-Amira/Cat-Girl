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
    path('cats/<int:cat_id>/assoc_date/<int:date_id>/', views.assoc_date, name='assoc_date'),
    path('play/', views.PlayList.as_view(), name='play_index'),
    path('play/<int:pk>/', views.PlayDetail.as_view(), name='play_detail'),
    path('play/create/', views.PlayCreate.as_view(), name='play_create'),
    path('play/<int:pk>/update/', views.PlayUpdate.as_view(), name='play_update'),
    path('play/<int:pk>/delete/', views.PlayDelete.as_view(), name='play_delete'),
]