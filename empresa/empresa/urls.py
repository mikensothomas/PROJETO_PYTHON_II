from django.urls import path
from app_empresa import views

urlpatterns = [
    path('',views.home,name='home'),
]
