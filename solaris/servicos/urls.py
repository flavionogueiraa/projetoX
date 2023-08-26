from django.urls import include, path
from rest_framework import routers
from servicos import views, viewsets

servicos_router = routers.DefaultRouter()
servicos_router.register("visita", viewsets.VisitaViewSet, basename="visita")

servicos_router.register(
    "estacao-solar", viewsets.EstacaoSolarViewSet, basename="estacao_solar"
)

servicos_router.register(
    "funcionario", viewsets.FuncionarioViewSet, basename="funcionario"
)

servicos_router.register(
    "cliente", viewsets.ClienteViewSet, basename="cliente"
)

estacao_solar_patterns = [
    path(
        "simulador-estacao/",
        views.SimuladorEstacaoSolarView.as_view(),
        name="simulador_estacao_solar_view",
    ),
]

funcionario_patterns = [
    path(
        "funcionario-update-view/<int:pk>/",
        views.FuncionarioUpdateView.as_view(),
        name="funcionario_update_view",
    ),
    path(
        "funcionario-delete-view/<int:pk>/",
        views.FuncionarioDeleteView.as_view(),
        name="funcionario_delete_view",
    ),
    path(
        "funcionario-create-view/",
        views.FuncionarioCreateView.as_view(),
        name="funcionario_create_view",
    ),
    path(
        "funcionario-list-view/",
        views.FuncionarioListView.as_view(),
        name="funcionario_list_view",
    ),
    path(
        "funcionario-detail-view/<int:pk>/",
        views.FuncionarioDetailView.as_view(),
        name="funcionario_detail_view",
    ),
]

visita_patterns = [
    path(
        "visita-create-view/",
        views.VisitaCreateView.as_view(),
        name="visita_create_view",
    ),
    path(
        "visita-update-view/<int:pk>/",
        views.VisitaUpdateView.as_view(),
        name="visita_update_view",
    ),
    path(
        "visita-delete-view/<int:pk>/",
        views.VisitaDeleteView.as_view(),
        name="visita_delete_view",
    ),
    path(
        "visita-detail-view/<int:pk>/",
        views.VisitaDetailView.as_view(),
        name="visita_detail_view",
    ),
    path(
        "visita-list-view/",
        views.VisitaListView.as_view(),
        name="visita_list_view",
    ),
    path(
        "marcar-visita-realizada/<int:pk>/",
        views.marcar_visita_realizada,
        name="marcar_visita_realizada",
    ),
]

cliente_patterns = [
    path(
        "cliente-detail-view/<int:pk>/",
        views.ClienteDetailView.as_view(),
        name="cliente_detail_view",
    ),
    path(
        "cliente-list-view/",
        views.ClienteListView.as_view(),
        name="cliente_list_view",
    ),
    path(
        "cliente-create-view/",
        views.ClienteCreateView.as_view(),
        name="cliente_create_view",
    ),
    path(
        "cliente-delete-view/<int:pk>/",
        views.ClienteDeleteView.as_view(),
        name="cliente_delete_view",
    ),
    path(
        "cliente-update-view/<int:pk>/",
        views.ClienteUpdateView.as_view(),
        name="cliente_update_view",
    ),
]

urlpatterns = (
    [
        path("api/", include(servicos_router.urls)),
    ]
    + estacao_solar_patterns
    + funcionario_patterns
    + visita_patterns
    + cliente_patterns
)
