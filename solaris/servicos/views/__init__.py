from .cliente import (
    ClienteCreateView,
    ClienteDeleteView,
    ClienteDetailView,
    ClienteListView,
    ClienteUpdateView,
)
from .estacao_solar import SimuladorEstacaoSolarView
from .funcionario import (
    FuncionarioCreateView,
    FuncionarioDeleteView,
    FuncionarioDetailView,
    FuncionarioListView,
    FuncionarioUpdateView,
)
from .visita import (
    VisitaCreateView,
    VisitaDeleteView,
    VisitaDetailView,
    VisitaListView,
    VisitaUpdateView,
    marcar_visita_realizada,
)

estacao_solar_views = [
    SimuladorEstacaoSolarView,
]
funcionario_views = [
    FuncionarioUpdateView,
    FuncionarioDeleteView,
    FuncionarioCreateView,
    FuncionarioListView,
    FuncionarioDetailView,
]
visita_views = [
    VisitaCreateView,
    VisitaUpdateView,
    VisitaDeleteView,
    VisitaDetailView,
    VisitaListView,
    marcar_visita_realizada,
]
cliente_views = [
    ClienteDetailView,
    ClienteListView,
    ClienteCreateView,
    ClienteDeleteView,
    ClienteUpdateView,
]

__all__ = (
    [] + estacao_solar_views + funcionario_views + visita_views + cliente_views
)
