from django.urls import path
from . import views


urlpatterns = [
   
    path('', views.home, name='home'),
    path('student/', views.student_view, name='student_view'),
    path('contact/', views.contact_view, name='contact_view'),
    path('contacte/', views.contacte_view, name='contacte_view'),
   
]