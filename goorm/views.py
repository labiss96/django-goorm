from django.shortcuts import render, get_object_or_404, redirect
from .models import Tobacco, Comment

def goormlist(request):
    list = Tobacco.objects.all()
    return render(request, 'goorm/list.html', {'list': list})

def detail(request, tobacco_id):
    tobacco_detail = get_object_or_404(Tobacco, pk=tobacco_id)
    
    comments = tobacco_detail.comments.all()
    if request.method == "POST" :
        comment = Comment()
        comment.post = Tobacco.objects.get(id = tobacco_id)
        comment.writer = request.POST['comment_writer']
        comment.text = request.POST['comment_text']
        comment.save()
    return render(request, 'goorm/detail.html',{'tobacco': tobacco_detail, 'comments':comments})

def new(request):
    return render(request, 'goorm/new.html')

def image(request):
    tobacco_image = Tobacco.objects
    return render(request, 'goorm/portfolio.html', {'image': image})

def create(request):
    new_tobacco = Tobacco()
    new_tobacco.name = request.POST['name']
    new_tobacco.price = request.POST['price']
    new_tobacco.rel_date = request.POST['rel_date']
    new_tobacco.nicotine = request.POST['nicotine']
    new_tobacco.TAR = request.POST['TAR']
    new_tobacco.feel_of_hit = request.POST['feel_of_hit']
    new_tobacco.img = request.FILES.get('tobacco_img')
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

def comment_delete(request, comment_id) : 
    delete_comment = Comment.objects.get(id=comment_id)
    delete_comment.delete()
    return redirect('/goorm/' + str(delete_comment.tobacco.id))


# Create your views here.
