from django import forms

from ..models import Pessoa


class PessoaForm(forms.ModelForm):
    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        model = Pessoa

        fields = "__all__"
