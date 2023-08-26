from .marcar_visita_realizada import marcar_visita_realizada
from .visita_create_view import VisitaCreateView
from .visita_delete_view import VisitaDeleteView
from .visita_detail_view import VisitaDetailView
from .visita_list_view import VisitaListView
from .visita_update_view import VisitaUpdateView

__all__ = [
    marcar_visita_realizada,
    VisitaCreateView,
    VisitaUpdateView,
    VisitaDeleteView,
    VisitaDetailView,
    VisitaListView,
]
