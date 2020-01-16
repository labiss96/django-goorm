from django.shortcuts import render,redirect
from goorm.models import Tobacco, Brand
from django.utils import timezone
from .models import Buying_Log
# Create your views here.

def home(request):
    brands = Brand.objects.all()
    best_goorms = Tobacco.objects.all().order_by('-score')

# top3 Goorm 표시를 위한 데이터처리.
    best_list = []
    if len(best_goorms) >= 4:
        for i in range(4):
            score_star = score_trans(best_goorms[i].score)
            best_goorms[i].star = score_star
            best_list.append(best_goorms[i])

# modal에 출력될 브랜드-구름 selectbox를 위한 데이터처리.
    goorm_dic = {}
    for brd in brands:
        option_list = []
        for grm in best_goorms:
            if brd.brd_name == grm.brand.brd_name:
                option_list.append(grm)
        goorm_dic[brd.brd_name] = option_list
        

    return render(request, 'home.html', {"brands":brands, "best_grms":best_list, "goorm_list":best_goorms, "goorm_dic":goorm_dic})

def buy_tobacco(request):
    tobaccos = Tobacco.objects.all()
    return render(request, 'buy_tobacco.html',{"tobaccos":tobaccos})

def save_log(request):
    log = Buying_Log()
    log.buyer = request.user
    log.product = Tobacco.objects.get(id=request.POST['grmName'])
    log.date = timezone.datetime.now()
    log.save()
    # print('정상적으로 구매되었음.')
    return redirect('home')

def score_trans(score):
    if score < 2:
        return '★☆☆☆☆'
        # return '&#9733; &#9734; &#9734; &#9734; &#9734;'
    elif 2 <= score < 3:
        return '★★☆☆☆'
        
    elif 3 <= score < 4:   
        return '★★★☆☆'
        
    elif 4 <= score < 5:
        return '★★★★☆'
        
    else:
        return '★★★★★'
        