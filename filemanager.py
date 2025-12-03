# filemanager.py
import os

def lijst_bestanden():
    print("=== Bestanden in huidige map ===")
    for f in os.listdir("."):
        print(f)

def lees_bestand():
    naam = input("Bestandsnaam: ")
    if os.path.isfile(naam):
        with open(naam, "r") as f:
            print(f.read())
    else:
        print("Bestand niet gevonden.")

def verwijder_bestand():
    naam = input("Bestandsnaam: ")
    if os.path.isfile(naam):
        os.remove(naam)
        print("Bestand verwijderd.")
    else:
        print("Bestand niet gevonden.")

def menu():
    while True:
        print("\n=== Filemanager ===")
        print("1. Toon bestanden")
        print("2. Lees bestand")
        print("3. Verwijder bestand")
        print("4. Stop")
        keuze = input("Kies een optie: ")

        if keuze == "1": lijst_bestanden()
        elif keuze == "2": lees_bestand()
        elif keuze == "3": verwijder_bestand()
        elif keuze == "4": break
        else: print("Ongeldige keuze")

if __name__ == "__main__":
    menu()
