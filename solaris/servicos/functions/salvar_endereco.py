from core.forms import EnderecoForm


def salvar_endereco(view):
    """Salva o endereço do cliente."""
    has_endereco = hasattr(view.object, "endereco")
    endereco = view.object.endereco if has_endereco else None
    endereco_form = EnderecoForm(
        view.request.POST,
        instance=endereco,
    )

    if endereco_form.is_valid():
        endereco = endereco_form.save()
        if not endereco.cliente:
            endereco.cliente = view.object
            endereco.save()
