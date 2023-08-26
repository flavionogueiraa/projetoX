from novadata_utils.serializers import NovadataModelSerializer

from ..models import IncidenciaEstado


class IncidenciaEstadoSerializer(NovadataModelSerializer):
    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        model = IncidenciaEstado
        fields = "__all__"
