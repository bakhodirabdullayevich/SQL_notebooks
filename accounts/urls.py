from django.urls import path
from .views import *


urlpatterns = [
    path('xxx/', login_function, name='login'),
    path('logout/', logout_function, name="logout"),
    path('login/', LoginView.as_view(), name="login"),
    #path('logout/', LoginView.as_view(), name="logout"),
]