from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from users.models import User

from users.serializers import UserSerializer


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
