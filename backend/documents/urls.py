from django.urls import path
from .views import DocumentUploadView, DocumentGetView

urlpatterns = [
    path('upload/', DocumentUploadView.as_view()),
    path('get/',DocumentGetView.as_view()),
]