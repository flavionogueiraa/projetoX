from .fornecedor import (
    FornecedorCreateView,
    FornecedorDeleteView,
    FornecedorDetailView,
    FornecedorListView,
    FornecedorUpdateView,
)
from .notificacao import (
    NotificacaoCreateView,
    NotificacaoDeleteView,
    NotificacaoDetailView,
    NotificacaoListView,
    NotificacaoUpdateView,
)
from .pessoa import (
    PessoaCreateView,
    PessoaDeleteView,
    PessoaDetailView,
    PessoaListView,
    PessoaUpdateView,
)

notificacao_views = [
    NotificacaoCreateView,
    NotificacaoUpdateView,
    NotificacaoDeleteView,
    NotificacaoDetailView,
    NotificacaoListView,
]
pessoa_views = [
    PessoaUpdateView,
    PessoaCreateView,
    PessoaListView,
    PessoaDetailView,
    PessoaDeleteView,
]
fornecedor_views = [
    FornecedorCreateView,
    FornecedorListView,
    FornecedorDeleteView,
    FornecedorDetailView,
    FornecedorUpdateView,
]

__all__ = [] + notificacao_views + pessoa_views + fornecedor_views
