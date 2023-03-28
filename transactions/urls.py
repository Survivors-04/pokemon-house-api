from django.urls import path
from . import views

urlpatterns = [
    path("", views.TransactionView.as_view()),
    path("<str:pk>/", views.TrasanctionDetailView.as_view()),
]
