from django import template
from django.conf import settings
from novadata_utils.redirect import reverse_lazy_plus

register = template.Library()


@register.simple_tag()
def is_dev():
    """Retorna se o ambiente é de desenvolvimento."""
    return settings.DEV


@register.simple_tag()
def get_single_model_links(model, id):
    """Retorna os links de detail, update e delete de um model."""
    return {
        "detail": reverse_lazy_plus(
            f"{model}_detail_view",
            url_params=[id],
            just_uri=True,
        ),
        "update": reverse_lazy_plus(
            f"{model}_update_view",
            url_params=[id],
            just_uri=True,
        ),
        "delete": reverse_lazy_plus(
            f"{model}_delete_view",
            url_params=[id],
            just_uri=True,
        ),
    }


@register.simple_tag()
def get_normal_model_links(model):
    """Retorna o link de create de um model."""
    return {
        "create": reverse_lazy_plus(
            f"{model}_create_view",
            just_uri=True,
        ),
        "list": reverse_lazy_plus(
            f"{model}_list_view",
            just_uri=True,
        ),
    }


@register.filter()
def get_attribute(obj, field_and_attribute):
    """
    Retorna o verbose_name de um campo de um objeto.

    Forma de uso::

        {{ obj|get_attribute:"field,verbose_name" }}
    """
    splited_values = field_and_attribute.split(",")
    field = splited_values[0]
    attribute = splited_values[1]

    has_field = hasattr(obj, field)
    if not has_field:
        return f'O objeto "{obj}" não tem o atributo "{field}".'

    field_obj = obj._meta.get_field(field)
    has_attribute = hasattr(field_obj, attribute)

    if not has_attribute:
        return f'O campo "{field}" do objeto "{obj}" não tem o atributo "{attribute}".'  # noqa E501

    return getattr(field_obj, attribute)
