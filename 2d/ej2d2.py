"""
Enunciado:
Implementa la función 'calculate_max_and_min' que reciba como parámetro una
lista de números 'list_numbers', se deben considerar los casos en los que los
datos que se encuentran dentro de la lista sean de type string o que la lista
se encuentre vacía. 

Adicionalmente, la función debe ir imprimiendo cual es el número menor y el
número mayor según va avanzando en la lista siempre y cuando este sea distinto
al anterior resultado simulando la depuración por trazas.

Y finalmente, retornar un valor del número menor y del número mayor.

Parámetros:
list_numbers: Lista de números.

Ejemplo:
    Entrada: 
        [10, 5.1, 0, -2, 31, 55, 70, -10, 200, -55.55]
    Salida:
        'Greater:' 200
        'Lesser: ' -55.55

    Entrada:
        ['Hello', 1, 5, -20, 55.5]
    Salida:
        TypeError

    Entrada:
        []
    Salida:
        ValueError
 """


def calculate_max_and_min(list_numbers):
    # Write here your code

    """
    Find de max and min in the list
    Raise Error if not int or empty list
    """
    greater = list_numbers[0]
    lesser = list_numbers[0]

    if len(list_numbers) == 0:
        raise ValueError
    
    for i in list_numbers:
        if not isinstance(i, (int, float)):
            raise TypeError

    for i in list_numbers:
        if i > greater:
            greater = i
            print("Greater:", greater)
        if i < lesser:
            lesser = i
            print("Lesser:", lesser)
    
    return lesser, greater

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

print(
    "\nResult: ", calculate_max_and_min([10, 5.1, 0, -2, 31, 55, 70, -10, 200, -55.55])
)
