from django.urls import path
from . import views

urlpatterns = [
    path('', views.youtube, name= 'youtube'),
    path('successful/', views.successful_page, name='successful_page'),
]
