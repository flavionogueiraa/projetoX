from .base_list_view import BaseListView
from .base_novadata_view import BaseNovadataView
from .design_system import design_system
from .errors import error_403, error_404, error_500
from .home import HomeView
from .svg_viewer import svg_viewer

errors_views = [
    error_403,
    error_404,
    error_500,
]

__all__ = [
    BaseListView,
    BaseNovadataView,
    HomeView,
    design_system,
    svg_viewer,
] + errors_views
