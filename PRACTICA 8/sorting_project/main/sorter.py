def sort_numbers(numbers):
    """
    Ordena una lista de números enteros en orden ascendente.
    :param numbers: Lista de números enteros.
    :return: Lista ordenada.
    """
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("Todos los elementos deben ser enteros")
    return sorted(numbers)
