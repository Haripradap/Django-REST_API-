from django.urls import path
from .views import get_user,create_user,user_detail

urlpatterns = [
    path('users/', get_user, name = "get_users"),
    path('users/create/', create_user, name = "create_users"),
    path('users/<int:pk>', user_detail, name = "user_detail"),

]