from core.models import Fornecedor
from django.contrib import admin
from novadata_utils.admin import NovadataModelAdmin


@admin.register(Fornecedor)
class FornecedorAdmin(NovadataModelAdmin):
    ...
