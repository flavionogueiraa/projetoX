from novadata_utils.viewsets import NovadataModelViewSet
from servicos.models import Funcionario
from servicos.serializers import FuncionarioSerializer


class FuncionarioViewSet(NovadataModelViewSet):
    queryset = Funcionario.objects.all()

    serializer_class = FuncionarioSerializer

    auto_search_fields = True
