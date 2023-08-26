from core.models import Notificacao
from django import forms
from global_functions.utils.forms import prepare_form_fields


class NotificacaoForm(forms.ModelForm):
    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        model = Notificacao

        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """Método para executarmos ações ao iniciar a classe."""
        super(NotificacaoForm, self).__init__(*args, **kwargs)
        self.fields = prepare_form_fields(self.fields)
