from novadata_utils.serializers import NovadataModelSerializer

from ..models import Visita


class VisitaSerializer(NovadataModelSerializer):
    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        model = Visita
        fields = "__all__"
