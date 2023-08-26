from core.serializers import FornecedorSerializer
from novadata_utils.viewsets import NovadataModelViewSet

from ..models import Fornecedor


class FornecedorViewSet(NovadataModelViewSet):
    queryset = Fornecedor.objects.all()

    serializer_class = FornecedorSerializer

    auto_search_fields = True
