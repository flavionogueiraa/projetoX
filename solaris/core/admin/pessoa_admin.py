from core.models import Pessoa
from django.contrib import admin
from novadata_utils.admin import NovadataModelAdmin


@admin.register(Pessoa)
class PessoaAdmin(NovadataModelAdmin):
    ...
