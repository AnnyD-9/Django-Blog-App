from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('signup/', views.user_signup,name='signup'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('login/', views.user_logout,name='logout'),
    path('logout/', views.user_login,name='login'),
    path('addpost/', views.add_post,name='add_post'),
    path('updatepost/<int:id>', views.update_post,name='update_post'),
    path('deletepost/<int:id>', views.delete_post,name='delete_post'),
]