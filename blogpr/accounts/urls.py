from django.urls import path
from . import views
app_name='auth'

urlpatterns=[
    path('login/',views.user_login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.user_logout,name='logout')

]