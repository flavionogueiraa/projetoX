from .endereco_viewset import EnderecoViewSet
from .fornecedor_viewset import FornecedorViewSet
from .incidencia_estado_viewset import IncidenciaEstadoViewSet
from .notificacao_viewset import NotificacaoViewSet
from .pessoa_viewset import PessoaViewSet

__all__ = [
    IncidenciaEstadoViewSet,
    EnderecoViewSet,
    PessoaViewSet,
    FornecedorViewSet,
    NotificacaoViewSet,
]
