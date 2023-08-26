from core.models import Pessoa
from core.serializers import PessoaSerializer
from novadata_utils.viewsets import NovadataModelViewSet


class PessoaViewSet(NovadataModelViewSet):
    queryset = Pessoa.objects.all()

    serializer_class = PessoaSerializer

    auto_search_fields = True
