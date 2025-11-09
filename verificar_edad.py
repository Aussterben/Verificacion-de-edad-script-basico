#!/usr/bin/env python3

edad = int(input("[+] Introduce tu edad: "))

if edad < 10:
    print(f"[!] ¿Estás seguro? Si eres menor de 10, eres muy pequeño para entrar")
    edad = int(input("\n[+] Introduce tu edad: "))
    if edad >= 10:
        print(f"[+] Eres mayor o tienes 10 años\n")
        print(f"\n[+] Ahora puedes elegir qué escoger, escoge del 1 al 3")
        escoger = int(input("\n[+] Introduce un valor: "))

        if escoger == 1:
            print(f"[+] URL: (https://www.youtube.com/@aussterbenDev)")
        if escoger == 2:
            print(f"[+] URL: (https://www.tiktok.com/@aussterbendev)")
        if escoger == 3:
            print(f"[+] URL: (https://x.com/AussterbenDev)")
        if escoger >= 4:
            print(f"\n[!] ERROR: Elige un número del 1-3")
        if escoger == 0:
            print(f"\n[!] ERROR: Elige un número del 1-3")
    else:
        print(f"[!] Sigues siendo menor")

else:
    print(f"\n[+] Eres mayor o tienes 10 años")
    print(f"\n[+] Ahora puedes elegir qué escoger, escoge del 1 al 3")
    escoger = int(input(f"[+] Introduce un valor: "))

    if escoger == 1:
        print(f"[+] URL: (https://www.youtube.com/@aussterbenDev)")
    if escoger == 2:
        print(f"[+] URL: (https://www.tiktok.com/@aussterbendev)")
    if escoger == 3:
        print(f"[+] URL: (https://x.com/AussterbenDev)")
    if escoger >= 4:
        print(f"\n[!] ERROR: Elige un número del 1-3")
    if escoger == 0:
        print(f"\n[!] ERROR: Elige un número del 1-3")

# By aussterben

