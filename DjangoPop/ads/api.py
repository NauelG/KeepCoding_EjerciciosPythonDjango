from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad
from ads.permissions import AdPermission
from ads.serializers import AdListSerializer, AdSerializer


""" Clase de la API hecha de manera tradicional
class AdListAPIView(APIView):

    def get(self, request):
        ads = Ad.objects.all()
        serializer = AdListSerializer(ads, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
"""

# Heredando de ListCreateAPIView Hace lo mismo que el comentario anterior
"""
class AdListAPIView(ListCreateAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Ad.objects.all() if self.request.user.is_authenticated else Ad.objects.filter(status=Ad.PUBLISHED)

    def get_serializer_class(self):
        return AdListSerializer if self.request.method == 'GET' else AdSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
"""

# Pasamos la clase anterior a model view set
class AdViewSet(ModelViewSet):

    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, AdPermission]

    def get_queryset(self):
        return self.queryset if self.request.user.is_authenticated else self.queryset.filter(status=Ad.PUBLISHED)

    def get_serializer_class(self):
        return AdListSerializer if self.action == 'list' else AdSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

"""
class AdDetailAPIView(APIView):

    def get(self, request, pk):
        ad = get_object_or_404(Ad, pk=pk)
        serializer = AdSerializer(ad)
        return Response(serializer.data)

    def put(self, request, pk):
        ad = get_object_or_404(Ad, pk=pk)
        serializer = AdSerializer(ad, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        ad = get_object_or_404(Ad, pk=pk)
        ad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

# Hace lo mismo que el comentario anterior
"""QUEDA INCLUIDO EN EL ADVIEWSET
class AdDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [AdPermission]
"""