from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import User

app_name = 'account'
urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='login'),
    path('profile', User.as_view(), name='profile_view'),

]
