from django.shortcuts import render
from django.http import HttResponse

# Create your views here.
def home(request):
    return HttResponse('Vamo Dale')