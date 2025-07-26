from django.contrib import admin
from django.urls import path
from . import views

# localhost:8000/chai
urlpatterns = [
    path('',views.all_chai,name='all_chai'), # name parameter is optional
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'), # chai_id is a variable part of the URL
]