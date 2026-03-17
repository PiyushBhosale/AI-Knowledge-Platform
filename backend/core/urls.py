from django.urls import path
from core.views import HealthCheckView
urlpatterns = [
    path('check',HealthCheckView.as_view()),
]