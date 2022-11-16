import os
from colorama import init, Fore, Back, Style

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
    print(Fore.GREEN+"¿Quieres volver a cifrar/decifrar? (y/n)")
    opcion = input(">> " + Fore.YELLOW)
    
    if opcion == 'y':
    
        clear()
        print(Fore.WHITE+"\n1 - Cifrar un mensaje")
        print(Fore.WHITE+"2 - Decifrar un mensaje")
        opcion=int(input("\n¿Que deseas hacer?\n>> " + Fore.YELLOW))

        if opcion == 1:
            
            msg = input(Fore.WHITE + "\n¿Que deseas " + Fore.BLUE + "cifrar?"+ Fore.WHITE + "\n>> " + Fore.YELLOW)
            shyMsg = shy(msg)
            print(Fore.LIGHTGREEN_EX+"\nMensaje cifrado: " + shyMsg)
            input(Fore.YELLOW+"\nPreciona Enter para continuar")

        elif opcion == 2:
            
            msg = input(Fore.WHITE + "\n¿Que deseas" + Fore.BLUE + " decifrar?" + Fore.WHITE + "\n>> " + Fore.YELLOW)
            wellMsg = well(msg)
            print(Fore.LIGHTGREEN_EX+"\nMensaje decifrado: " + wellMsg)
            input(Fore.YELLOW+"\nPreciona Enter para continuar")

        else:
            print(Fore.RED+"Elije una opcion valida!\n")
            input(Fore.YELLOW+"\nPreciona Enter para continuar")
    
    elif opcion =='n':
        print(Fore.RED+"BYE!")
        break
    
    else:
        print(Fore.RED+"Opcion incorrecta")
        input(Fore.WHITE+"\nPreciona Enter para continuar")

