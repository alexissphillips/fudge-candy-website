'''We are importing Django's function path and 
all our views from the blog(fudgekettlesite) application '''

from django.urls import path 
from . import views

# my view name should match what the candy store app actually DOES
# the url name should decribe what the page is 
urlpatterns = [
    path('', views.candylist, name='candylist'),
]




























