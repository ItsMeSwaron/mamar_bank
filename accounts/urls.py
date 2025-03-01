from django.urls import path
from .views import UserRegistraionView, UserLoginView, UserLogoutView, UserBankAccountUpdateView

urlpatterns = [
    path('register/', UserRegistraionView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile' )
]
