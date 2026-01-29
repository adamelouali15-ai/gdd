import rechenoperationen as ro # type: ignore

def taschenrechner():
    zahl1 = float(input("Geben Sie die erste Zahl ein: "))
    zahl2 = float(input("Geben Sie die zweite Zahl ein: "))

    operations = ["add", "sub", "mult", "div"]
    print(f"Diese Operationen stehen zur Verfügung: {operations}")
    selection = input("Geben Sie eine Operation an: ")

    if selection == "add":
        result = ro.addition(zahl1, zahl2)
    elif selection == "sub":
        result = ro.subtraction(zahl1, zahl2)
    elif selection == "mult":
        result = ro.multiplication(zahl1, zahl2)
    elif selection == "div":
        result = ro.division(zahl1, zahl2)
    else:
        print("Ungültige Auswahl")
        return

    print(f"Das Ergebnis lautet: {result}")
if __name__ == "__main__":
    taschenrechner()
# Dies ist ein einfacher Taschenrechner, der Addition, Subtraktion, Multiplikation und Division unterstützt.

