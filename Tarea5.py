
entrada=input("Ingrese la entrada: ")
estado=0
palabra=""
for caracter in entrada:
    if estado==0:
        if caracter.isalpha():
            estado=2
            palabra=palabra+caracter
        elif caracter=='_':
            estado=1
            palabra=palabra+caracter
        else:
            print("Error en la cadena de entrada, el simbolo: "+str(caracter)+" no es reconocido en el estado "+str(estado)+", cadena reconocida: "+str(palabra))
            break
    elif estado==1:
        if caracter.isalpha():
            estado=3
            palabra=palabra+caracter
        elif caracter=='_':
            estado=1
            palabra=palabra+caracter
        else:
            print("Error en la cadena de entrada, el simbolo: "+str(caracter)+" no es reconocido en el estado "+str(estado)+", cadena reconocida: "+str(palabra))
            break
    elif estado==2:
        if caracter.isalpha():
            estado=2
        elif caracter.isnumeric():
            estado=4
        else:
            print("Error en la cadena de entrada, el simbolo: "+str(caracter)+" no es reconocido en el estado "+str(estado)+", cadena reconocida: "+str(palabra))
            break
    elif estado==3:
        if caracter.isnumeric():
            estado=4
            palabra=palabra+caracter
        else:
            print("Error en la cadena de entrada, el simbolo: "+str(caracter)+" no es reconocido en el estado "+str(estado)+", cadena reconocida: "+str(palabra))
            break
    elif estado==4:
        print("Se a aceptado la cadena de caracteres: "+str(palabra))
        break
if estado!=4:
    print("error en la cadena, no ha llegado a un estado de aceptacion")