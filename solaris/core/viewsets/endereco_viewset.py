from core.serializers import EnderecoSerializer
from novadata_utils.viewsets import NovadataModelViewSet

from ..models import Endereco


class EnderecoViewSet(NovadataModelViewSet):
    queryset = Endereco.objects.all()

    serializer_class = EnderecoSerializer

    auto_search_fields = True
