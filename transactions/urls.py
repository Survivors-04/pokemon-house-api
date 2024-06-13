from django.urls import path
from . import views

urlpatterns = [
    path("transactions/", views.TransactionView.as_view()),
    path("transactions/<str:pk>/", views.TrasanctionDetailView.as_view()),
]
