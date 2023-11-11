from django.urls import path
from .views import RegistratsiyaView,HomeView,CustomerViev,ContactView

urlpatterns = [
    path("registratsiya/",RegistratsiyaView.as_view(),name="registratsiya"),
    path("home/",HomeView.as_view(),name="home"),
    path("customer/",CustomerViev.as_view(),name="customer"),
    path("customer/<int:pk>",CustomerViev.as_view(),name="customer_update"),
    path("customer/<int:pk>/contact",ContactView.as_view(),name="contact"),
]
