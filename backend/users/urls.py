from django.urls import path
from .views import UserListView, RegisterUserView

urlpatterns = [
    path('', UserListView.as_view()),
    path('register',RegisterUserView.as_view())
]