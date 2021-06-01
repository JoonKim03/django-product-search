from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    #path('login/', views.login, name='login'),
 #   path('search/', views.Search_Product, name='search'),
    #path('detail/', views.search_detail, name='search_detail'),
    #path('parameter', views.get_post, name='parameter')
    path('detail/', views.detail, name='detail'),
    path('search/', views.search_product, name='product'),
    path('logout/', views.logout, name='logout')
]