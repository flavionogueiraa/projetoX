from novadata_utils.serializers import NovadataModelSerializer

from ..models import Cliente


class ClienteSerializer(NovadataModelSerializer):
    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        model = Cliente
        fields = "__all__"
