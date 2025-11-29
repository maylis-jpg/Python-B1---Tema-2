"""
Enunciado:
Implementa una función 'triangle_area_calculate', que recibe dos parámetros,
que corresponden a la altura y la base de un triángulo que deben
ser números positivos. Dichos parámetros deben ser nombrados correctamente,
considerando las buenas prácticas de programación PEP8.
La función debe retornar el cálculo del área de un triángulo mediante los
datos introducidos, adicionalmente, el código debe tener comentarios de manera
que se vaya explicando el procedimiento.

Parámetros:
Son dos parámetros, que corresponden a la altura y la base de
un triángulo y deben ser números positivos. Se deben crear correctamente
utilizando las buenas prácticas de programación PEP8.


Ejemplo:
    Entrada:
    triangle_area_calculate(33, 45)

    Salida:
    742.5
"""


def triangle_area_calculate(base, height):
    """
    Determina area de un trángulo.

    Parámetros
    ----------
    base : float
        Base del triángulo (número positivo).
    height : float
        Altura del triángulo (número positivo).

        Returns
    -------
    float
        Resultado del área del triangulo.
    """
    # Determinar si parámetros son positivos
    if base <= 0 or height <= 0:
        raise ValueError('base y altura tienen que ser positivo')

    # Calculo área del triangulo
    area_triangulo = 1/2 * base * height
    return area_triangulo

# print(triangle_area_calculate(33, 45)
