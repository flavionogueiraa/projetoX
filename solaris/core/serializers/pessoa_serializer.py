from core.models import Pessoa
from novadata_utils.serializers import NovadataModelSerializer


class PessoaSerializer(NovadataModelSerializer):
    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        model = Pessoa
        fields = "__all__"
