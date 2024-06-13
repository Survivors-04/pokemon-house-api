
from .models import Transaction
from .serializers import TransactionSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class TransactionView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

    def perform_create(self, serializer):
      serializer.save(seller_id = self.request.user)

class TrasanctionDetailView(generics.RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()