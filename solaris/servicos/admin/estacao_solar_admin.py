from django.contrib import admin
from novadata_utils.admin import NovadataModelAdmin
from servicos.models import EstacaoSolar


@admin.register(EstacaoSolar)
class EstacaoSolarAdmin(NovadataModelAdmin):
    ...
