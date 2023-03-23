from django.forms import model_to_dict
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.views import Response, Request,status, APIView
from pokemons.models import Pokemons

from pokemons.serializers import PokemonSerializer


class PokemonListCreateView(ListCreateAPIView):
    serializer_class = PokemonSerializer
    queryset = Pokemons.objects.all()

    def create(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)

        if is_many:
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        serializer = PokemonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class PokemonDetailView(RetrieveAPIView):
        serializer_class = PokemonSerializer
        queryset = Pokemons.objects.all()

