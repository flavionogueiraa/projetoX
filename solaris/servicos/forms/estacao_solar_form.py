from django import forms
from global_functions.utils.forms import prepare_form_fields
from servicos.models import EstacaoSolar


class EstacaoSolarForm(forms.ModelForm):
    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        model = EstacaoSolar

        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """Método para executarmos ações ao iniciar a classe."""
        super(EstacaoSolarForm, self).__init__(*args, **kwargs)
        self.fields = prepare_form_fields(self.fields)
