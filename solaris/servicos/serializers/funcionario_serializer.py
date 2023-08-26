from novadata_utils.serializers import NovadataModelSerializer

from ..models import Funcionario


class FuncionarioSerializer(NovadataModelSerializer):
    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        model = Funcionario
        fields = "__all__"
