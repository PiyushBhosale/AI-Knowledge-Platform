from django.urls import path
from .views import UserListView, RegisterUserView, LoginView

urlpatterns = [
    path('', UserListView.as_view()),
    path('register',RegisterUserView.as_view()),
    path('login',LoginView.as_view()),
]