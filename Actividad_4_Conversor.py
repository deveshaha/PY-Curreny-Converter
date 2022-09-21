# Declaracion de variables precio de cada moneda

usd_cop = 3750
usd_yuan = 6.37
usd_gbp = 0.76

eur_cop = 4000
eur_yuan = 6.93
eur_gbp = 0.83

print("Bienvenido al conversor de monedas")

moneda_seleccionada = input("Selecciona la moneda desde la cual quieres convertir"
                            "\n1 - USD"
                            "\n2 - Euro")

match moneda_seleccionada:
    case "1":
        print("Has seleccionado convertir desde dolar")

        def dolarto():
            seleccion = input("Selecciona a que moneda quieres convetir"
                              "\n1 - Pesos Colombianos"
                              "\n2 - Yuanes"
                              "\n3 - Libras")

            if seleccion == "1":
                print(f'Has seleccionado convertir de dolares a Pesos colombianos'
                      f'\n Un dolar equivale a {usd_cop}')
                cantidad = input("¿Cuantos dolares a pesos colombianos deseas convertir?")
                print(f'{cantidad} dolares a Pesos colombianos es: {int(cantidad) * float(usd_cop)}')
            elif seleccion == "2":
                print(f'Has seleccionado convertir de dolares a Yuanes'
                      f'\n Un dolar equivale a {usd_yuan}')
                cantidad = input("¿Cuantos dolares a yuanes deseas convertir?")
                print(f'{cantidad} dolares a Yuanes es: {int(cantidad) * float(usd_yuan)}')
            elif seleccion == "3":
                print(f'Has seleccionado convertir de dolares a Libras'
                      f'\n Un dolar equivale a {usd_gbp}')
                cantidad = input("¿Cuantos dolares a Libras deseas convertir?")
                print(f'{cantidad} dolares a Libras es: {int(cantidad) * float(usd_gbp)}')
            else:
                print("La selección no es valida")

        dolarto()

    case "2":
        print("Has seleccionado convertir desde euro")


        def eurto():
            seleccion = input("Selecciona a que moneda quieres convetir"
                              "\n1 - Pesos Colombianos"
                              "\n2 - Yuanes"
                              "\n3 - Libras")

            if seleccion == "1":
                print(f'Has seleccionado convertir de euros a Pesos colombianos'
                      f'\n Un euro equivale a {eur_cop}')
                cantidad = int(input("¿Cuantos euros a pesos colombianos deseas convertir?"))
                print(f'{cantidad} euros a Pesos colombianos es: {int(cantidad) * float(eur_cop)}')
            elif seleccion == "2":
                print(f'Has seleccionado convertir de euros a Yuanes'
                      f'\n Un euro equivale a {eur_yuan}')
                cantidad = input("¿Cuantos euros a yuanes deseas convertir?")
                print(f'{cantidad} dolares a Yuanes es: {int(cantidad) * float(eur_yuan)}')
            elif seleccion == "3":
                print(f'Has seleccionado convertir de euros a Libras'
                      f'\n Un euro equivale a {eur_gbp}')
                cantidad = input("¿Cuantos dolares a Libras deseas convertir?")
                print(f'{cantidad} euros a Libras es: {int(cantidad) * float(eur_gbp)}')
            else:
                print("La selección no es valida")


        eurto()

    case _:
        print("No se ha encontrado tal moneda")
