from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', show_post.as_view(), name='show_post'),
    path('register/', register_user.as_view(), name='register'),
    path('login/', login_user.as_view(), name='login'),
    path('logout/', views.logoutuser, name='logout'),

]

