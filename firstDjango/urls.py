from django.urls import path
from .import views


urlpatterns = [
    path('',views.City , name='city-home'),
    path('home/', views.home, name='home'),         
    path('create-city/', views.createCity, name='create-city'),

   
    # City CRUD
    path('city/', views.fetchAllCity, name='fetchAll'),
    path('city/<int:pk>/', views.City_detail, name='city-detail'),
    path('city/<int:pk>/edit/', views.updateCity, name='update-city'),
    path('city/<int:pk>/delete/', views.deleteCity, name='delete-city'),
]
