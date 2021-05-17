from django.urls import path

from . import views

app_name = 'covid'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup, name='signup'),
    path('upload/', views.upload, name='upload'),
    path('predict/', views.predict, name='predict'),
    path('doctor/', views.doctor, name='doctor'),
    path('recommend/', views.recommend, name='recommend'),
]
