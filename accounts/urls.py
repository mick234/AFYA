from .import views
from django.urls import path, include
urlpatterns = [
 path('register/', views.Register,name = "register"), 
 path('login/', views.Login,name = "login"),
 path('', views.home, name = "home"),
 path('logout/', views.logout, name = "logout"),
 path('freelance/', views.freelance, name="freelance"),
 #path('edit/<str:pk>', views.edit, name="edit"),
 path('update/<int:blog_id>', views.update, name="edit"),
 path('delete/<str:pk>', views.delete, name="delete-prod"),
]