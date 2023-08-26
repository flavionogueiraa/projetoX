from novadata_utils.viewsets import NovadataModelViewSet
from servicos.models import EstacaoSolar
from servicos.serializers import EstacaoSolarSerializer


class EstacaoSolarViewSet(NovadataModelViewSet):
    queryset = EstacaoSolar.objects.all()

    serializer_class = EstacaoSolarSerializer

    auto_search_fields = True
