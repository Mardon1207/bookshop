from django.urls import path
from .views import RegistratsiyaView,HomeView,CustomerViev,ContactView,PublishersView,PublisherDetailView,LanguagesView,LanguageDetailView,BooksView,BookDetailView,AuthorView,AuthorDetailView,GenreView,GenreDetailView

urlpatterns = [
    path("registratsiya/",RegistratsiyaView.as_view(),name="registratsiya"),
    path("home/",HomeView.as_view(),name="home"),
    path("customer/",CustomerViev.as_view(),name="customer"),
    path("customer/<int:pk>",CustomerViev.as_view(),name="customer_update"),
    path("customer/<int:pk>/contact",ContactView.as_view(),name="contact"),
    path("publisher/",PublishersView.as_view(),name="publisher"),
    path("publisher/<int:pk>",PublisherDetailView.as_view(),name="publisher_detail"),
    path("lang/",LanguagesView.as_view(),name="lang"),
    path("lang/<int:pk>",LanguageDetailView.as_view(),name="lang_detail"),
    path("book/",BooksView.as_view(),name="book"),
    path("book/<int:pk>",BookDetailView.as_view(),name="book_detail"),
    path("author/",AuthorView.as_view(),name="author"),
    path("author/<int:pk>",AuthorDetailView.as_view(),name="author_detail"),
    path("genre/",GenreView.as_view(),name="genre"),
    path("genre/<int:pk>",GenreDetailView.as_view(),name="author_detail"),
]
