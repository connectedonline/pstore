# calculator.py
def optellen(a, b): return a + b
def aftrekken(a, b): return a - b
def vermenigvuldigen(a, b): return a * b
def delen(a, b): return a / b if b != 0 else "Fout: delen door nul"

def menu():
    print("=== Calculator ===")
    print("1. Optellen")
    print("2. Aftrekken")
    print("3. Vermenigvuldigen")
    print("4. Delen")
    keuze = input("Kies een optie: ")
    a = float(input("Eerste getal: "))
    b = float(input("Tweede getal: "))

    if keuze == "1": print("Resultaat:", optellen(a, b))
    elif keuze == "2": print("Resultaat:", aftrekken(a, b))
    elif keuze == "3": print("Resultaat:", vermenigvuldigen(a, b))
    elif keuze == "4": print("Resultaat:", delen(a, b))
    else: print("Ongeldige keuze")

if __name__ == "__main__":
    while True:
        menu()
        if input("Nog een berekening? (j/n): ").lower() != "j":
            break
