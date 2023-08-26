from novadata_utils.viewsets import NovadataModelViewSet
from servicos.models import Cliente
from servicos.serializers import ClienteSerializer


class ClienteViewSet(NovadataModelViewSet):
    queryset = Cliente.objects.all()

    serializer_class = ClienteSerializer

    auto_search_fields = True
