""" Función para obtener el máximo número de una lista: 
    lista[1,2,3]; lista[1:] --> devuelve: [2,3] desde el índice 1 hasta el final
"""
def max(lista):
    num=1
    for x in lista:
        for y in lista[num:]:
            if x>y:
                maxi=x
        num +=1
    return maxi

"""Función para obtener el factorial de un número;
    range(5)--> devuelve [0,1,2,3,4]
 """
def factorial(num):
    aux=1
    for x in range(num):
        x +=1
        aux *=x
    return aux

"""Función que suma los caracteres de un número;
    str(123) --> '123'; num='123' num[0]--> '1'
""" 
def suma_cifras(num):
    aux=0
    num=str(num)
    for x in num:
        aux +=int(x)
    return aux