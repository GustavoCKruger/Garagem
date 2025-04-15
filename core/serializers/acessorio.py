from core.views.acessorio import Acessorio
from rest_framework.serializers import ModelSerializer

from core.models import Categoria

class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"