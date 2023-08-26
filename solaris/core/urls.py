from core import views, viewsets
from django.urls import include, path
from rest_framework import routers

core_router = routers.DefaultRouter()
core_router.register(
    "incidencia-estado",
    viewsets.IncidenciaEstadoViewSet,
    basename="incidencia_estado",
)

core_router.register("endereco", viewsets.EnderecoViewSet, basename="endereco")

core_router.register("pessoa", viewsets.PessoaViewSet, basename="pessoa")

core_router.register(
    "fornecedor", viewsets.FornecedorViewSet, basename="fornecedor"
)

core_router.register(
    "notificacao", viewsets.NotificacaoViewSet, basename="notificacao"
)

notificacao_patterns = [
    path(
        "notificacao-create-view/",
        views.NotificacaoCreateView.as_view(),
        name="notificacao_create_view",
    ),
    path(
        "notificacao-update-view/<int:pk>/",
        views.NotificacaoUpdateView.as_view(),
        name="notificacao_update_view",
    ),
    path(
        "notificacao-delete-view/<int:pk>/",
        views.NotificacaoDeleteView.as_view(),
        name="notificacao_delete_view",
    ),
    path(
        "notificacao-detail-view/<int:pk>/",
        views.NotificacaoDetailView.as_view(),
        name="notificacao_detail_view",
    ),
    path(
        "notificacao-list-view/",
        views.NotificacaoListView.as_view(),
        name="notificacao_list_view",
    ),
]

pessoa_patterns = [
    path(
        "pessoa-update-view/<int:pk>/",
        views.PessoaUpdateView.as_view(),
        name="pessoa_update_view",
    ),
    path(
        "pessoa-create-view/",
        views.PessoaCreateView.as_view(),
        name="pessoa_create_view",
    ),
    path(
        "pessoa-list-view/",
        views.PessoaListView.as_view(),
        name="pessoa_list_view",
    ),
    path(
        "pessoa-detail-view/<int:pk>/",
        views.PessoaDetailView.as_view(),
        name="pessoa_detail_view",
    ),
    path(
        "pessoa-delete-view/<int:pk>/",
        views.PessoaDeleteView.as_view(),
        name="pessoa_delete_view",
    ),
]

fornecedor_patterns = [
    path(
        "fornecedor-create-view/",
        views.FornecedorCreateView.as_view(),
        name="fornecedor_create_view",
    ),
    path(
        "fornecedor-list-view/",
        views.FornecedorListView.as_view(),
        name="fornecedor_list_view",
    ),
    path(
        "fornecedor-delete-view/<int:pk>/",
        views.FornecedorDeleteView.as_view(),
        name="fornecedor_delete_view",
    ),
    path(
        "fornecedor-detail-view/<int:pk>/",
        views.FornecedorDetailView.as_view(),
        name="fornecedor_detail_view",
    ),
    path(
        "fornecedor-update-view/<int:pk>/",
        views.FornecedorUpdateView.as_view(),
        name="fornecedor_update_view",
    ),
]

urlpatterns = (
    [
        path("api/", include(core_router.urls)),
    ]
    # + notificacao_patterns
    + pessoa_patterns
    + fornecedor_patterns
)
