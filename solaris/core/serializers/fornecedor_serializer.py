from novadata_utils.serializers import NovadataModelSerializer

from ..models import Fornecedor


class FornecedorSerializer(NovadataModelSerializer):
    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        model = Fornecedor
        fields = "__all__"
