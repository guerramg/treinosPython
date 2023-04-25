tabuada = int(input("Diga qual tabuada deseja visualizar? 1 à 10: "))
coeficiente = 1

if tabuada < 1 or tabuada > 10:
    print ("Tabuada inválida!")
else:
    print(f"Tabuada do numerador {tabuada}")
    while coeficiente <= 10:
        print (f"{coeficiente} x {tabuada} = {coeficiente * tabuada}")
        coeficiente = coeficiente + 1
    else:
        print(f"Final da tabuada {tabuada}")

