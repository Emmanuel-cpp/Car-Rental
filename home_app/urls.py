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
    path('error-404', views.error404, name='error404'),
    path('blog', views.blog, name='blog'),
    path('blog-details', views.blog_details, name='blog_details'),
    path('contact', views.contact, name='contact'),
]
