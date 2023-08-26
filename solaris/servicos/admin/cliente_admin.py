from core.admin import EnderecoInline
from django.contrib import admin
from novadata_utils.admin import NovadataModelAdmin
from servicos.models import Cliente


@admin.register(Cliente)
class ClienteAdmin(NovadataModelAdmin):
    inlines = [
        EnderecoInline,
    ]
