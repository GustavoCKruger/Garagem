from rest_framework.viewsets import ModelViewSet

from core.models import Acessorio
from core.serializers import AcessorioSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer