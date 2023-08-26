from servicos.forms import EstacaoSolarForm


def salvar_estacao_solar(view):
    """Salva o endereço do cliente."""
    estacao_solar = view.object.estacaosolar_set.first()
    estacao_solar_form = EstacaoSolarForm(
        view.request.POST,
        instance=estacao_solar,
    )

    if estacao_solar_form.is_valid():
        estacao_solar = estacao_solar_form.save()
        if not estacao_solar.cliente:
            estacao_solar.cliente = view.object
            estacao_solar.save()
