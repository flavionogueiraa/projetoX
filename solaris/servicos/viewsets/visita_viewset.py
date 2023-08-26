from novadata_utils.viewsets import NovadataModelViewSet
from servicos.models import Visita
from servicos.serializers import VisitaSerializer


class VisitaViewSet(NovadataModelViewSet):
    queryset = Visita.objects.all()

    serializer_class = VisitaSerializer

    auto_search_fields = True
