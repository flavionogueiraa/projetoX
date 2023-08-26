from novadata_utils.serializers import NovadataModelSerializer
from servicos.models import EstacaoSolar


class EstacaoSolarSerializer(NovadataModelSerializer):
    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        model = EstacaoSolar
        fields = "__all__"
