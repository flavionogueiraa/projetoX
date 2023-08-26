from novadata_utils.serializers import NovadataModelSerializer

from ..models import Notificacao


class NotificacaoSerializer(NovadataModelSerializer):
    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        model = Notificacao
        fields = "__all__"
