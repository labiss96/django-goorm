from django.shortcuts import render, get_object_or_404, redirect
from .models import Tobacco, Comment, Brand
from django.contrib.auth.decorators import login_required

def goormlist(request):
    grm_list = Tobacco.objects.all()
    brd_list = Brand.objects.all()

    brd_grm = []
    for brd in brd_list:
        tmps = []
        tmps.append(brd)
        grm_info = grm_list.filter(brand = brd)

        for grm in grm_info:    
            score_star = score_trans(grm.score)
            grm.star = score_star

        tmps.append(grm_info)
        brd_grm.append(tmps)

    return render(request, 'goorm/list.html', {'grm_list': grm_list, 'brd_grm': brd_grm, 'brd_list':brd_list})

def score_trans(score):
    if score < 2:
        return '★☆☆☆☆'
    elif 2 <= score < 3:
        return '★★☆☆☆'
    elif 3 <= score < 4:   
        return '★★★☆☆'
    elif 4 <= score < 5:
        return '★★★★☆'    
    else:
        return '★★★★★'

def detail(request, tobacco_id):
    
    # POST(comment 생성)
    if request.method == "POST" :
        tobacco_detail = get_object_or_404(Tobacco, pk=tobacco_id)
        
        # create comment 
        comment = Comment()
        comment.tobacco = Tobacco.objects.get(id = tobacco_id)
        comment.writer = request.user
        comment.contents = request.POST['comment_text']
        comment.score = request.POST['comment_score']
        comment.save()

        comments = Comment.objects.filter(tobacco=tobacco_id)
    
    # GET
    else:
        tobacco_detail = get_object_or_404(Tobacco, pk=tobacco_id)
        comments = Comment.objects.filter(tobacco=tobacco_id)

    # 구름과자 score 계산 로직
    num_of_cmt = len(comments)
    total_score = 0
    for cmt in comments:
        total_score += cmt.score
    if total_score != 0:
        total_score = total_score / num_of_cmt
    tobacco_detail.score = total_score
    tobacco_detail.save()

    cmt_flag = False
    for cmt in comments:
        if request.user == cmt.writer:
            cmt_flag = True 

    return render(request, 'goorm/detail.html',{'tobacco': tobacco_detail, 'comments':comments, 'cmt_flag':cmt_flag})

@login_required
def new(request):
    if request.user.username == 'admin':
        brands = Brand.objects.all()
        return render(request, 'goorm/new.html', {'brands':brands} )
    else:
        err = '권한이 없습니다.'
        return render(request, 'accounts/error.html', {'err':err} )
    

def create(request):
    if request.POST['brand']=='isNewBrand':
        selected_brand = Brand()
        selected_brand.brd_name = request.POST['newBrand']
        selected_brand.save()
    else:
        selected_brand = Brand.objects.get(brd_name=request.POST['brand'])
    
    new_tobacco = Tobacco()
    new_tobacco.brand = selected_brand
    new_tobacco.name = request.POST['name']
    new_tobacco.price = request.POST['price']
    new_tobacco.rel_date = request.POST['rel_date']
    new_tobacco.nicotine = request.POST['nicotine']
    new_tobacco.TAR = request.POST['TAR']
    new_tobacco.feel_of_hit = request.POST['feel_of_hit']
    new_tobacco.img = request.FILES.get('tobacco_img')
    if request.POST['isMenthol'] == 'yes':
       new_tobacco.isMenthol = True
    else:
       new_tobacco.isMenthol = False 
    new_tobacco.save()
    return redirect('/goorm/' +str(new_tobacco.id))

@login_required
def edit(request, tobacco_id) :
    if request.user.username == 'admin':
        edit_tobacco = Tobacco.objects.get(id=tobacco_id)
        return render(request, 'goorm/edit.html', {'tobacco' : edit_tobacco})
    else:
        err = '권한이 없습니다.'
        return render(request, 'accounts/error.html', {'err':err} )


def update(request, tobacco_id):
    update_tobacco = Tobacco.objects.get(id=tobacco_id)
    update_tobacco.name = request.POST['name']
    update_tobacco.price = request.POST['price']
    update_tobacco.rel_date = request.POST['rel_date']
    update_tobacco.nicotine = request.POST['nicotine']
    update_tobacco.TAR = request.POST['TAR']
    update_tobacco.feel_of_hit = request.POST['feel_of_hit']
    if request.FILES.get('tobacco_img'):
        update_tobacco.img = request.FILES.get('tobacco_img')
    if request.POST['isMenthol'] == 'yes':
        update_tobacco.isMenthol = True
    else:
        update_tobacco.isMenthol = False
    update_tobacco.save()
    return redirect('/goorm/' + str(update_tobacco.id))

@login_required
def delete(request, tobacco_id):
    if request.user.username == 'admin':
        delete_t= Tobacco.objects.get(id = tobacco_id)
        delete_t.delete()
        return redirect('goorm:goormlist')
    else:
        err = '권한이 없습니다.'
        return render(request, 'accounts/error.html', {'err':err} )

def comment_delete(request, comment_id) : 
    delete_comment = Comment.objects.get(id=comment_id)
    delete_comment.delete()
    return redirect('/goorm/' + str(delete_comment.tobacco.id))

def comment_update(request, comment_id):
    update_comment = Comment.objects.get(id=comment_id)
    update_comment.contents = request.POST['edit_text']
    update_comment.score = request.POST['edit_score']
    update_comment.save()
    return redirect('/goorm/' + str(update_comment.tobacco.id))
    
    

def brand_filter(request , brand_id) :
   brand_tobacco=Tobacco.objects.filter(brand = brand_id)
   brand = Brand.objects.get(pk=brand_id)
   return render(request, 'goorm/brand_detail.html' ,{'tobaccos':brand_tobacco, 'brand': brand})    

def search(request):
    if request.GET.get('q'):
        brd = Brand.objects.all()
        grm = Tobacco.objects.all()
        search_type = request.GET.get('fd_name')
        search_data = request.GET.get('q')

        if search_type == 'brand':
            results = brd.filter(brd_name__icontains = search_data)
        elif search_type == 'name':
            results = grm.filter(name__icontains = search_data)

    return render(request, 'goorm/search.html', { 'results': results, 'search_type':search_type})
# Create your views here.