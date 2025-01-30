from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name="logout"),
    path('home-two', views.home_2, name='home_2'),
    path('about', views.about, name='about'),
    path('car-list-one',views.carList1, name='list1'),
    path('car-list-two', views.carList2, name='list2'),
    path('reservation', views.reservation, name='reserve'),
]
