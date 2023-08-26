from novadata_utils.serializers import NovadataModelSerializer

from ..models import Endereco


class EnderecoSerializer(NovadataModelSerializer):
    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        model = Endereco
        fields = "__all__"
