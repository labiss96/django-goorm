from django.contrib import admin
from django.urls import path
from . import views

app_name = 'goorm'

urlpatterns = [
    path('goormlist',views.goormlist, name='goormlist'),
    path('<int:tobacco_id>', views.detail, name='detail'),
    path('new', views.new, name='new'),
    path('create', views.create, name='create'),
    path('brand_detail/<str:brand_id>', views.brand_filter, name='brand_filter'),
    path('delete/<int:tobacco_id>', views.delete, name='delete'),
    path('comment_delete/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('comment_edit/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('comment_update/<int:comment_id>', views.comment_update, name='comment_update'),
    path('search/', views.search, name='search'),
    path('edit/<int:tobacco_id>', views.edit, name='edit'),
    path('update/<int:tobacco_id>', views.update, name='update'),
]