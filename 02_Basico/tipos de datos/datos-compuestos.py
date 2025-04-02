#Estas se pueden modificar
lista = ["Erjie Xia", "Soy Chino", True, 1.25]

#Estas no se pueden modificar
tupla = ("Erjie Xia", "Soy Chino", True, 1.25)

#Aquí modificamos un elemento de la lista
lista[3] = False

#No se pueden modificar los elementos de las tuplas, pero si cambiar el valor entero de ella
#tupla[3] = "1.25"
tupla = ("Erjie Xia", 14, True, 1.25)

#Los conjuntos/sets son datos compuestos que no se acceden por índice y además no almacenan
#los datos duplicados
conjunto = {"Erjie Xia", "Soy Chino", True, 1.25, "Soy Chino"}
#Haciendo un print podemos comprobar que "Soy Chino", solo se muestra una vez

#Los diccionarios en python son como json
diccionario = {
    'nombre': "Erjie Xia",
    'canal': "Erjiegamer",
    'altura': 1.74,
    'es_chino': True,
    'nombre_dupe': "Erjie Xia"
}
print(diccionario)