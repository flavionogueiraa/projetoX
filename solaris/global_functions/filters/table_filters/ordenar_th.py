def ordenar_th(ordem, query):
    def get_reverse(ordem):
        if ordem.startswith('-'):
            return True
        else:
            return False
    
    if ordem and ordem != 'None':
        try:
            query = query.order_by(ordem)
        except:
            query = sorted(query, key=lambda object: getattr(object, ordem.replace('-', '')), reverse=get_reverse(ordem))
    return query
