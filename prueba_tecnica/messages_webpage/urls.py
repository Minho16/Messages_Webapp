from django.urls import path
from . import views 
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', views.home, name='home'),    
    path('register/', views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='messages_webpage/login.html'), name = 'login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='messages_webpage/logout.html'), name = 'logout'),
    path('user/<str:name>', views.user_page, name='user_page'),
    path('notfound',  views.notfound, name='notfound')

]