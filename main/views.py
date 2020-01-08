from django.shortcuts import render
from goorm.models import Tobacco, Brand
# Create your views here.

def home(request):
    brands = Brand.objects.all()

    return render(request, 'home.html', {"brands":brands})