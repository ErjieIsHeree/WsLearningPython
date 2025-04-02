#Las variables son espacios de la memoria que almacenan un dato temporal
#En python las variables son dinámicas, al contrario de Java no requieren
#definirlas manualmente, python las identifica y las declara por sí sola

#Creamos un variable y le almacenamos un dato, por ejemplo "Erjie"
nombre = "Erjie"
print(nombre)

#Estas cadenas creadas las podemos concatenar con otras
bienvenida = "Buenas tardes señorit@, "
#(reusando la variable anterior)
print(bienvenida + nombre)

#Como bien sabemos, en java podemos concatenar String e Integers sin más, pero
#en otros lenguajes como python o javascript no es posible, pero hay una alternativa
numero_de_hakari = 777
hakari = f"El número de Hakari es {numero_de_hakari}"
print(hakari)

#Operadores de pertenencia (in / not in)
print("Erjie" in nombre) #True
print("Erjie" not in nombre) #False