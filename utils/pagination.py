import math


def make_pagination_range(
    page_range: list[int],
    qty_pages: int,
    current_page: int,
) -> dict:
    """
    Gera o intervalo dinâmico de páginas para a exibição de um componente de paginação.

    Calcula uma janela deslizante de páginas mantendo a página atual centralizada
    sempre que possível e ajustando os limites quando estiver próximo ao início
    ou ao fim do intervalo total.

    Args:
        page_range (list[int]): Lista com a sequência de todas as páginas disponíveis.
        qty_pages (int): Quantidade máxima de botões de páginas visíveis na navegação.
        current_page (int): O número da página atualmente selecionada.

    Returns:
        dict: Um dicionário contendo o intervalo de paginação calculado e métricas
              auxiliares para a renderização na interface (templates).
    """
    # Calcula o meio do intervalo visível para manter a página atual centralizada
    middle_range = math.ceil(qty_pages / 2)

    # Define o início e o fim teóricos do intervalo com base na página atual
    start_range = current_page - middle_range
    stop_range = current_page + middle_range
    total_pages = len(page_range)

    # Calcula o offset (deslocamento) caso o início seja menor que zero (extremo esquerdo)
    start_range_offset = abs(start_range) if start_range < 0 else 0

    # Ajusta o limite inferior para não usar índices negativos e joga o excesso para o final
    if start_range < 0:
        start_range = 0
        stop_range += start_range_offset

    # Ajusta o limite superior para não ultrapassar o total e estende para a esquerda se necessário
    if stop_range >= total_pages:
        start_range = start_range - abs(total_pages - stop_range)

    # Fatia a lista de páginas conforme o intervalo final calculado
    pagination = page_range[start_range:stop_range]

    return {
        'pagination': pagination,
        'page_range': page_range,
        'qty_pages': qty_pages,
        'current_page': current_page,
        'total_pages': total_pages,
        'start_range': start_range,
        'stop_range': stop_range,
        'first_page_out_of_range': current_page > middle_range,
        'last_page_out_of_range': stop_range < total_pages,
    }
