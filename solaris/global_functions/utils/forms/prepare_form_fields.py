def prepare_form_fields(fields):
    for name, field in fields.items():
        field = make_classes_config(name, field)
        field = make_props_configs(field)
    return fields


def make_classes_config(name, field):
    default_classes = [""]

    text_types = ["text", "email", "url"]
    class_text = "input-text"

    classes_textarea = "textarea"

    number_types = ["number"]

    default_hidden_fields = ["latitude", "longitude"]
    class_hidden = "hidden"

    default_masks = {
        "cpf_cnpj": "000.000.000-00",
        "telefone": "(00) 0 0000-0000",
        "cep": "00000-000",
    }

    field_is_hidden_field = name in default_hidden_fields

    if has_input_type(field):
        field_is_text_type = field.widget.input_type in text_types
        field_is_number_type = field.widget.input_type in number_types
        field_has_format_key = hasattr(field.widget, "format_key")
        field_is_date_input = (
            field_has_format_key
            and field.widget.format_key == "DATE_INPUT_FORMATS"
        )
        field_is_datetime_input = (
            field_has_format_key
            and field.widget.format_key == "DATETIME_INPUT_FORMATS"
        )

        if field_is_text_type:
            field.widget.attrs["class"] = class_text
        if field_is_number_type:
            field.widget.attrs["class"] = class_text
        if field_is_date_input:
            field.widget.attrs["type"] = "date"
            field.widget.input_type = "date"
        if field_is_datetime_input:
            field.widget.attrs["type"] = "datetime-local"
            field.widget.input_type = "datetime-local"

        field.widget.attrs["class"] = (
            " ".join(default_classes)
            + " "
            + field.widget.attrs.get("class", "")
        )

        if name in default_masks.keys():
            field.widget.attrs["data-mask"] = default_masks.get(name, "")

    if is_text_area(field):
        field.widget.attrs["class"] = classes_textarea
        field.widget.attrs["placeholder"] = "Escreva aqui..."

    if field_is_hidden_field:
        field.widget.attrs["class"] = class_hidden

    return field


def make_props_configs(field):
    select_types = ["select"]

    select_attr = "js-choices"
    select_props = "js-choices-props"
    select_props_value = '{"searchEnabled": true, "searchChoices": true}'

    if has_input_type(field):
        field_is_select_type = field.widget.input_type in select_types
        if field_is_select_type:
            field.widget.attrs[select_attr] = "true"
            field.widget.attrs[select_props] = select_props_value

    return field


def is_text_area(field):
    has_cols = "cols" in field.widget.attrs
    has_rows = "rows" in field.widget.attrs

    if has_cols or has_rows:
        return True
    return False


def has_input_type(field):
    return hasattr(field.widget, "input_type")
