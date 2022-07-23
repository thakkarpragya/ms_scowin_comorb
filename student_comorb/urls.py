from django.urls import path
#from django import views
from .views import *

urlpatterns = [
    path('studentvaccinationreaction', StudentsVacReact.as_view()),
    path('studentvaccinationreaction/<int:pk>', StudentsVacReact.as_view()),
]