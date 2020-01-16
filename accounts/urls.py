from django.contrib import admin
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('edit/<str:profile_name>',views.edit,name='edit'),
    path('update/<str:profile_name>',views.update,name='update'),
    path('mypage/<str:profile_name>', views.mypage, name='mypage'),
    path('error/', views.error, name='error'),
    path('developer/', views.developer, name='developer'),
]