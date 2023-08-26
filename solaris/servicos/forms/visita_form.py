from django import forms
from global_functions.utils.forms import (
    prepare_form_fields,
    prepare_form_initial,
)
from servicos.models import Visita


class VisitaForm(forms.ModelForm):
    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        model = Visita

        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """Método para executarmos ações ao iniciar a classe."""
        super(VisitaForm, self).__init__(*args, **kwargs)
        self.fields = prepare_form_fields(self.fields)
        self.initial = prepare_form_initial(self.initial)
