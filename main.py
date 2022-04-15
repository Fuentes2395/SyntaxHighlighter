import string

# Parte 1: Tarea pasada
file = open("texto.txt", "r")

#Declaración de variables
variables = list(string.ascii_letters)
# variables = ["a", "b", "c"]
operadores = ["+", "-", "*", "=", "^", "(", ")", ";"]
numeros = ["1","2","3","4","5","6","7","8","9","0"]
tempText = ""
stopCategoria = False
checkReal = False
flag = False
cont = 1
contNumeros = 0
listaValores = []

# Lee cada fila del archivo de texto
# for line in file:
#     #Saca cada palabra de la linea y la mete en una lista
#     for word in line.split():
#         listaValores.append(word)
#     print("Problema", cont)
#     stopCategoria = False
#     contNumeros = 0

#     #Saca el número de comparaciones que el programa tendra que hacer para obtener el token del valor.
#     for i in range (len(listaValores)):
#         checkReal = False
#         #Sirve para parar el for loop si se detecto un comentario
#         if stopCategoria == True:
#             break
#         #El valor de la lista dependiendo del índice lo mete a la variable tempText
#         tempText = listaValores[i]
#         #Regresa "flag" a su estado original para que categorize el valor
#         flag = False
#         for j in range(len(tempText)):

#             #Revisa si es VARIABLE
#             #Con que tenga una letra (EXCEPTO E), es considerado como VARIABLE
#             if flag == False:
#                 for k in range(len(variables)):
#                     if tempText[j] == variables[k]:
#                         contNumeros += 1
#                         while j+contNumeros < len(tempText):
#                             for r in range(len(operadores)):
#                                 if tempText[j+contNumeros] == operadores[r]:
#                                     print("ERROR. FAVOR DE INGRESAR UNA VARIABLE VÁLIDA")
#                                     #Para que ya no analice más valores de la lista.
#                                     stopCategoria = True
#                                     #Este checkReal va a servir para que cuando detecte un error, se pare el problema por completo.
#                                     checkReal = True
#                             contNumeros += 1
#                         if checkReal == False:
#                             print(tempText, ": Variable")
#                         flag = True
#                         break
            
#             #Revisa si es OPERADOR
#             if flag == False:
#                 for k in range(len(operadores)):
#                     if tempText[j] == operadores[k]:
#                         if len(tempText) > 1:
#                             print("ERROR. NO PUEDES PONER UN OPERADOR A LADO DE ORO VALOR.")
#                             stopCategoria = True
#                             checkReal = True
#                         else:
#                             if tempText[j] == "+":
#                                 print(tempText, ": Suma")
#                             elif tempText[j] == "*":
#                                 print(tempText, ": Multiplicación")
#                             elif tempText[j] == "=":
#                                 print(tempText, ": Asignación")
#                             elif tempText[j] == "^":
#                                 print(tempText, ": Potencia")
#                             elif tempText[j] == "-":
#                                 print(tempText, ": Resta")
#                             elif tempText[j] == "(":
#                                 print(tempText, ": Paréntesis que abre")
#                             elif tempText[j] == ")":
#                                 print(tempText, ": Paréntesis que cierra")
#                             elif tempText[j] == ";":
#                                 print(tempText, ": Punto y coma")
#                             flag = True
#                             break

#             if flag == False:
#                 if tempText[j] == "/":
#                     #Si no existe a lado de la palabra, el try except evita el error
#                     try:
#                         #Si hay un / a lado, entonces es comentario
#                         #Todo lo que esta a lado lo imprime como comentario
#                         if tempText[j+1] == "/":
#                             #r como variable para ir por la lista de valores imprimiendo todos los valores de la lista como comentario
#                             r = i
#                             tempText = ""
#                             while r < len(listaValores):
#                                 #Aplica cuando ya no esta vacio
#                                 if tempText != "":
#                                     tempText = tempText + " " + listaValores[r]
#                                 #Aplica si esta vacio el tempText
#                                 else: 
#                                     tempText = listaValores[r]
#                                 r += 1
#                             print(tempText, ": Comentario")
#                             #Se pone como True para que el programa se pare
#                             stopCategoria = True
#                     #Evita error y dice que es división el problema
#                     except IndexError:
#                         print(tempText, ": División")
#                     flag = True
#                     break

#             #Revisa si es NUMERO
#             if flag == False:
#                 for k in range(len(numeros)):
#                     if tempText[j] == numeros[k]:
#                         contNumeros += 1
#                         #Revisa si es un número REAL o ENTERO
#                         while j+contNumeros < len(tempText):
#                             #Si tiene un . o E, automáticamente es Real
#                             if tempText[j+contNumeros] == "." or tempText[j+contNumeros] == "E":
#                                 print(tempText, ": Real")
#                                 checkReal = True
#                                 break
#                             for r in range(len(variables)):
#                                 if tempText[j+contNumeros] == variables[r]:
#                                     print("ERROR. FAVOR DE INGRESAR UNA VARIABLE VÁLIDA")
#                                     #Para que ya no analice más valores de la lista.
#                                     stopCategoria = True
#                                     #Este checkReal va a servir para que cuando detecte un error, se pare el problema por completo.
#                                     checkReal = True
#                             contNumeros += 1
#                         #Si el check nunca cambia, significa que el número no tiene ni . o E
#                         if checkReal == False:
#                             print(tempText, ": Entero")
#                         flag = True
#                         break

#     listaValores = []
#     cont += 1

# file.close()

def revisar_variables(string_temp, flag_error, diccionario_lexico):
    for i in range(len(string_temp)):
        for j in range(len(variables)):
            if string_temp[i] == variables[j]:
                cont_numeros = 1
                while i+cont_numeros < len(string_temp):
                    # Revisa si a lado de la variable existe un operador
                    for k in range(len(operadores)):
                        if string_temp[i+cont_numeros] == operadores[k]:
                            flag_error = True
                            return False
                    # Revisa si a lado de la variable existe un número
                    for k in range(len(numeros)):
                        if string_temp[i+cont_numeros] == numeros[k]:
                            flag_error = True
                            return False
                    cont_numeros += 1
    return True

def tres(lista_lexica, cont_lexico, indice_cont_lexico, flag_error, diccionario_lexico):
    # string_temp = lista_lexica[cont_lexico - indice_cont_lexico]
    # correcto = True
    # correcto = revisar_variables(string_temp, flag_error, diccionario_lexico)

    return mensaje_exito, flag_error, diccionario_lexico

def dos_revisar_igual(lista_lexica, cont_lexico, indice_cont_lexico, flag_error, diccionario_lexico):
    string_temp = lista_lexica[cont_lexico - indice_cont_lexico]
    if string_temp == "=":
        diccionario_lexico[string_temp] = "asignación"
        texto, flag_error, diccionario_lexico = tres(lista_lexica, cont_lexico, indice_cont_lexico-1, flag_error, diccionario_lexico)
        return texto, flag_error, diccionario_lexico
    flag_error = True
    return mensaje_error, flag_error, diccionario_lexico

def uno_revisar_variable(lista_lexica, cont_lexico, indice_cont_lexico, flag_error, diccionario_lexico):
    string_temp = lista_lexica[cont_lexico - indice_cont_lexico]
    for i in range(len(string_temp)):
        for j in range(len(variables)):
            if string_temp[i] == variables[j]:
                cont_numeros = 1
                while i+cont_numeros < len(string_temp):
                    # Revisa si a lado de la variable existe un operador
                    for k in range(len(operadores)):
                        if string_temp[i+cont_numeros] == operadores[k]:
                            flag_error = True
                            return mensaje_error, flag_error, diccionario_lexico
                    # Revisa si a lado de la variable existe un número
                    for k in range(len(numeros)):
                        if string_temp[i+cont_numeros] == numeros[k]:
                            flag_error = True
                            return mensaje_error, flag_error, diccionario_lexico
                    cont_numeros += 1
                diccionario_lexico[string_temp] = "variable"
                texto, flag_error, diccionario_lexico = dos_revisar_igual(lista_lexica,cont_lexico, indice_cont_lexico-1, flag_error, diccionario_lexico)
                if flag_error == True:
                    return mensaje_error, flag_error, diccionario_lexico
                return texto, flag_error, diccionario_lexico

lista_lexica = []
diccionario_lexico = {}
cont_lexico = 0
indice_cont_lexico = 0
string_comentario = ""
flag_comentario = False
flag_error = False
mensaje_error = "Ocurrio en error. Favor de revisar codigo"
mensaje_exito = "Exito."

#Parte 2: Revisador Léxico
file = open("texto.txt", "r")

for line in file:
    #El line.split() ignora los espacios del archivo de texto
    for word in line.split():
        lista_lexica.append(word)
        cont_lexico += 1

    for i in range(cont_lexico-1):
        if lista_lexica[i] == "//":
            flag_comentario = False
            # Une desde el indice especificado hasta el final 
            #https://stackoverflow.com/questions/39229286/join-list-from-specific-index
            string_comentario = " ".join(lista_lexica[i:])
            # Borrar desde el indice especificado hasta el final
            #https://stackoverflow.com/questions/627435/how-to-remove-an-element-from-a-list-by-index
            del lista_lexica[i:cont_lexico]
            lista_lexica.append(string_comentario)
            break

    print(lista_lexica)

    indice_cont_lexico = cont_lexico
    prueba, flag_error, diccionario_lexico = uno_revisar_variable(lista_lexica, cont_lexico, indice_cont_lexico, flag_error, diccionario_lexico)

    print(prueba)

        