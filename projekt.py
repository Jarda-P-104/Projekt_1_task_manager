ukoly = []
def pridat_ukol(ukoly):
        print("\n")
        nazev = input("Zadejte název úkolu: ")
        while nazev == "":
             print("Zadali jste prazdne pole")
             nazev = input("Zadejte název úkolu: ")
        popis = input("Zadejte popis úkolu: ")
        while popis == "":
             print("Zadali jste prazdne pole")
             popis = input("Zadejte popis úkolu: ")
        ukoly.append({"nazev": nazev, "popis": popis})
        print("\n")
        print("Úkol " + nazev + " byl přidán")

def zobrazit_ukoly(ukoly):
      if not ukoly:
        print("Nejsou žádné úkoly")
        return
      print("\n")
      print("Seznam úkolů: ")
      index = 1
      for i in ukoly:
        print(index,"Název:", i["nazev"], "Popis:", i["popis"])
        index += 1

def odstranit_ukol(ukoly):
    if not ukoly:
        print("\nNejsou žádné úkoly")
        return

    zobrazit_ukoly(ukoly)

    try:
        smazat = int(input("Zadejte číslo úkolu, který chcete smazat: "))
        smazat -= 1
    except ValueError:
        print("Neplatné číslo")
        return

    if 0 <= smazat < len(ukoly):
        odebrany = ukoly[smazat]
        ukoly.pop(smazat)
        print("\nÚkol", odebrany["nazev"], "byl odstraněn")
    else:
        print("Neplatné číslo")

def hlavni_menu():

    while True:
        print("\n")
        print("Správce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        print("\n")
        volba = input("Vyberte možnost (1-4): ")
        

        if volba == "1":
            pridat_ukol(ukoly)
        elif volba == "2":
              zobrazit_ukoly(ukoly)
        elif volba == "3":
             odstranit_ukol(ukoly)
            
        elif volba == "4":
                print("Ukončili jste program")
                break
        else:
             print("Neplatná hodnota - Zadejte číslo 1-4")

hlavni_menu()


