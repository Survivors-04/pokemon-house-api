from django.urls import path
from . import views

from rest_framework_simplejwt import views as jwt_view

urlpatterns = [
    path("transactions/", views.TransactionView.as_view()),
    path("transactions/<str:pk>/", views.TrasanctionDetailView.as_view()),
    
]