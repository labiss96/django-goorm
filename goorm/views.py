from django.shortcuts import render, get_object_or_404, redirect
from .models import Tobacco

def goormlist(request):
    list = Tobacco.objects.all()
    return render(request, 'goorm/list.html', {'list': list})

def detail(request, tobacco_id):
    tobacco_detail = get_object_or_404(Tobacco, pk=tobacco_id)
    return render(request, 'goorm/detail.html',{'tobacco': tobacco_detail})

def new(request):
    return render(request, 'goorm/new.html')

def create(request):
    new_tobacco = Tobacco()
    new_tobacco.name = request.POST['name']
    new_tobacco.price = request.POST['price']
    new_tobacco.rel_date = request.POST['rel_date']
    new_tobacco.nicotine = request.POST['nicotine']
    new_tobacco.TAR = request.POST['TAR']
    new_tobacco.feel_of_hit = request.POST['feel_of_hit']
    if request.POST['isMenthol']=='check':
       new_tobacco.isMenthol = True
    new_tobacco.save()
    return redirect('/goorm/' +str(new_tobacco.id))

# def edit(request, tobacco_id):
#     edit_tobacco = Tobacco.objects.get(id=tobacco_id)
#     return render(request, 'edit.html',{'tobacco':edit_tobacco})

# def update(request, tobacco_id):
#     update_tobacco = Tobacco()
#     update_tobacco.name = request.POST['name']
#     update_tobacco.price = request.POST['price']
#     update_tobacco.rel_date = request.POST['rel_date']
#     update_tobacco.nicotine = request.POST['nicotine']
#     update_tobacco.TAR = request.POST['TAR']
#     update_tobacco.feel_of_hit = request.POST['feel_of_hit']
#     update_tobacco.isMenthol = request.POST['isMenthol']
#     update_tobacco.save()
#     return redirect('/goorm/' + str(update_tobacco.id))

def delete(request, tobacco_id):
    delete_t= Tobacco.objects.get(id = tobacco_id)
    delete_t.delete()
    return redirect('goorm:goormlist')

# Create your views here.
