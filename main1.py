import os

dicOrd = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.;()¿?!¡\/ "
dicDes = "plmoknijbuhvygctfxrdzeswaqQAZWSXEDCRFVTGBYHNUJMIKOLP7531902468(!?/,¡\;)¿. "

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def shy(msg):
            shyMsg = ""
            for x in msg:
                for n in range(len(dicOrd)):
                    if x == dicOrd[n]:
                        shyMsg += dicDes[n]
            return shyMsg

def well(msg):
            wellMsg = ""
            for x in msg:
                for n in range(len(dicDes)):
                    if x == dicDes[n]:
                        wellMsg += dicOrd[n]
            return wellMsg

while True:
    
    clear()
    print("¿Quieres volver a cifrar/decifrar? (y/n)")
    opcion = input(">> ")
    
    if opcion == 'y':
    
        clear()
        print("\n1 - Cifrar un mensaje")
        print("2 - Decifrar un mensaje")
        opcion=int(input("\n¿Que deseas hacer?\n>> "))

        if opcion == 1:
            
            msg = input("\n¿Que deseas cifrar?\n>> ")
            shyMsg = shy(msg)
            print("\nMensaje cifrado: " + shyMsg)
            input("\nPreciona Enter para continuar")

        elif opcion == 2:
            
            msg = input("\n¿Que deseas decifrar?\n>> ")
            wellMsg = well(msg)
            print("\nMensaje decifrado: " + wellMsg)
            input("\nPreciona Enter para continuar")

        else:
            print("Elije una opcion valida!\n")
            input("\nPreciona Enter para continuar")
    
    elif opcion =='n':
        print("BYE!")
        break
    
    else:
        print("Opcion incorrecta")
        input("\nPreciona Enter para continuar")

