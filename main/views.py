from django.shortcuts import render
from goorm.models import Tobacco, Brand
# Create your views here.

def home(request):
    brands = Brand.objects.all()
    best_goorms = Tobacco.objects.all().order_by('-score')

    best_list = []
    for i in range(3):
        best_list.append(best_goorms[i])

    return render(request, 'home.html', {"brands":brands, "best_grms":best_list})