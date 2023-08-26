from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from novadata_utils.redirect import reverse_lazy_plus
from servicos.models import Visita


@login_required
def marcar_visita_realizada(request, pk):
    """Marca uma visita como realizada."""
    visita = get_object_or_404(Visita, pk=pk)
    visita.realizada = True
    visita.save()

    return reverse_lazy_plus(
        "cliente_detail_view",
        url_params=[visita.cliente.id],
        get_params={"mensagem_toastify": "Visita marcada como realizada!"},
    )
