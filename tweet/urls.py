from django.contrib import admin
from django.template.context_processors import static
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('create/', views.tweet_create,name='tweet_create'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    path('register/', views.register, name='register'),
    path('login',auth_views.LoginView.as_view(template_name="login.html"),name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),

]