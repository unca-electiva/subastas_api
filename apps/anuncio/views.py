from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Anuncio
from .serializers import AnuncioSerializer
from ..usuario.models import Usuario


# Vistas con APIView
class AnuncioListaAPIView(APIView):
    def get(self, request, format=None):
        anuncios = Anuncio.objects.all()
        serializer = AnuncioSerializer(anuncios, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AnuncioSerializer(data=request.data)
        # Asignamos el usuario por defecto temporalmente
        usuario = Usuario.objects.get(id=1)
        if serializer.is_valid():
            serializer.save(publicado_por=usuario)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnuncioDetalleAPIView(APIView):
    def get(self, request, pk, format=None):
        anuncio = get_object_or_404(Anuncio.objects.all(), pk=pk)
        serializer = AnuncioSerializer(anuncio)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        anuncio = get_object_or_404(Anuncio.objects.all(), pk=pk)
        serializer = AnuncioSerializer(anuncio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        anuncio = get_object_or_404(Anuncio.objects.all(), pk=pk)
        anuncio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Vistas Concretas
class AnuncioListaGenericView(ListCreateAPIView):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer

    def perform_create(self, serializer):
        usuario = Usuario.objects.get(id=1)
        serializer.save(publicado_por=usuario)


class AnuncioDetalleGenericView(RetrieveUpdateDestroyAPIView):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer


# ViewSets
class AnuncioViewSet(viewsets.ModelViewSet):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer

    def perform_create(self, serializer):
        usuario = Usuario.objects.get(id=1)
        serializer.save(publicado_por=usuario)
