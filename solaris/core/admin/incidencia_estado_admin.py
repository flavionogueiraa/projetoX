from django.contrib import admin
from novadata_utils.admin import NovadataModelAdmin

from ..models import IncidenciaEstado


@admin.register(IncidenciaEstado)
class IncidenciaEstadoAdmin(NovadataModelAdmin):
    ...
