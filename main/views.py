from django.shortcuts import render,redirect
from goorm.models import Tobacco, Brand
from .models import Buying_Log
# Create your views here.

def home(request):
    brands = Brand.objects.all()
    best_goorms = Tobacco.objects.all().order_by('-score')

    best_list = []
    if len(best_goorms) >= 3:
        for i in range(3):

            # score_star = '<small class="text-muted">'
            score_star = score_trans(best_goorms[i].score)
            # score_star += '</small>'


            best_goorms[i].star = score_star
            best_list.append(best_goorms[i])

    return render(request, 'home.html', {"brands":brands, "best_grms":best_list})

def buy_tobacco(request):
    tobaccos = Tobacco.objects.all()
    return render(request, 'buy_tobacco.html',{"tobaccos":tobaccos})

def save_log(request):
    log = Buying_Log()
    log.buyer = request.user
    log.product = Tobacco.objects.get(id =request.GET['tobacco'])
    log.save()
    return redirect('home')

def score_trans(score):
    if score < 2:
        return '★☆☆☆☆'
        # return '&#9733; &#9734; &#9734; &#9734; &#9734;'
    elif 2 <= score < 3:
        return '★★☆☆☆'
        # return '&#9733; &#9733; &#9734; &#9734; &#9734;'
    elif 3 <= score < 4:   
        return '★★★☆☆'
        # return '&#9733; &#9733; &#9733; &#9734; &#9734;'
    elif 4 <= score < 5:
        return '★★★★☆'
        # return '&#9733; &#9733; &#9733; &#9733; &#9734;'
    else:
        return '★★★★★'
        # return '&#9733; &#9733; &#9733; &#9733; &#9733;'