from django.urls import path
from .views import user_list,register_user,login_user

urlpatterns = [
    path('', user_list),
    path('register/', register_user),
    path('login/', login_user),

]