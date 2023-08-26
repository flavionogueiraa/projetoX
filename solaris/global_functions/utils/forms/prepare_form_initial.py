from datetime import date


def prepare_form_initial(initital):
    """Prepara o initial do form de maneira automática."""
    for field in initital:
        if isinstance(initital[field], date):
            initital[field] = initital[field].strftime("%Y-%m-%d %H:%M:%S")

    return initital
