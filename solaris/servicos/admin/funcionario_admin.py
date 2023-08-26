from django.contrib import admin
from novadata_utils.admin import NovadataModelAdmin
from servicos.models import Funcionario


@admin.register(Funcionario)
class FuncionarioAdmin(NovadataModelAdmin):
    autocomplete_fields = [
        "usuario",
    ]
