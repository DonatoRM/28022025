# Crea un programa que tome un nombre y un apellido; que los una con concatenación y muestre el nombre completo
# Creo las variables
name = "Pepe"
surname="Pérez"
name_complete=name+" "+surname
print(name_complete)
# Longitud de una cadena. Escribe un programa que calcule y muestre la longitud de la cadena y muestre el texto del usuario
texto="Buenos días, people"
longitud=len(texto)
print(f"La longitud de la cadena de texto es {longitud}")
# convertir en mayúsculas. Creamos un programa que convierta el texto en mayúsculas y se muestre
texto="jamón"
texto_mayusculas=texto.upper() #upper,lower.capitalize
print(f"Texto en mayúsculas: {texto_mayusculas}")
# reemplazar texto.
texto="people cambio de texto"
nuevo_texto=texto.replace("texto","palabra")
print(nuevo_texto)
print(texto)
# Contar ocurrencias de la letra a
parrafo="El día en que lo iban a matar, Santiago Nasar se levantó a las 5.30 de la mañana para esperar el buque en que llegaba el obispo. Había soñado que atravesaba un bosque de higuerones donde caía una llovizna tierna, y por un instante fue feliz en el sueño, pero al despertar se sintió por completo salpicado de cagada de pájaros"
contar=parrafo.count('a')
print("El caracter 'a' aparece ",contar," veces")
# Dividir una cadena en una lista
tipos="manzana,naranja,mandarina,uva"
cadena=tipos.split(',')
print("la cadena es ",cadena)
# impresionante ☺
cadena2=['la','cadena','es','esta']
unido=' '.join(cadena2)
print(unido)
#verifica que la cadena comienza con un prefijo
palabras="Buenos días, people"
palabra_inicial=palabras.startswith("Buenos") # endwith
print("el texto comienza con la palabra 'Buenos'")
