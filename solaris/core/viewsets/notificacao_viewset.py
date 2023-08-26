from core.serializers import NotificacaoSerializer
from novadata_utils.viewsets import NovadataModelViewSet

from ..models import Notificacao


class NotificacaoViewSet(NovadataModelViewSet):
    queryset = Notificacao.objects.all()

    serializer_class = NotificacaoSerializer

    auto_search_fields = True
