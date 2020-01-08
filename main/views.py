from django.shortcuts import render
from goorm.models import Tobacco
# Create your views here.

def home(request):
    tobaccos = Tobacco.objects.all()
    
    return render(request, 'home.html')