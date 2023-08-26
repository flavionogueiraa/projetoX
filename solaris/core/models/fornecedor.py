# from django.db import models

from .pessoa import Pessoa


class Fornecedor(Pessoa):
    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "core"
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
