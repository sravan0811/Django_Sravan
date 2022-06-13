from django.urls import path
from . import views

app_name = 'basic_app'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('form/', views.form_name_view, name='form_name'),
    path('register/', views.user, name='register') ,
    path('user_login/', views.user_login, name='user_login'),
]