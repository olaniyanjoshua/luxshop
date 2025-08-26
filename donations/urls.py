from django.urls import path
from . import views


app_name = 'donations'

urlpatterns = [
    path('donate/', views.make_donation, name='make_donation'),
    path('verify/', views.verify_donation, name='verify_donation'),
]
