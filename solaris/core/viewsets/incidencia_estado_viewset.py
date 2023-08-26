from core.serializers import IncidenciaEstadoSerializer
from novadata_utils.viewsets import NovadataModelViewSet

from ..models import IncidenciaEstado


class IncidenciaEstadoViewSet(NovadataModelViewSet):
    queryset = IncidenciaEstado.objects.all()

    serializer_class = IncidenciaEstadoSerializer

    auto_search_fields = True

    filterset_fields = ["sigla"]
