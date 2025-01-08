from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage, name='index'),
    path('register/', views.UserRegisterView, name='register'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('about/', views.AboutPage, name='about'),
    path('contact/', views.ContactPage, name='contact'),
    path('search-result/', views.SearchBlogPage, name='search_blog'),
    path('blog/<slug:slug>/', views.DetailBlog, name='detail_blog'),
    path('create/', views.CreateBlogView, name='blog_create'),
    path('category/<str:category>/', views.category_filter_view, name='category_filter'),
]
