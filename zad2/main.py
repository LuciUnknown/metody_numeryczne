import rozwiazanie

print("Co chcesz zrobić? \n 1. Pojedyńczy przykład \n 2. Więcej niż jeden, mniej niż wszystkie  \n 3. Wszystkie \n 4. inny przykład")
wybor = int(input("Podaj wybor: "))
print("Podaj warunek stopu (liczba całkowita to ilość iteracji, niecałkowita to dokładność")
war_stop = float(input("Podaj warunek stopu: "))
if wybor == 1:
    print("Podaj który przykład chcesz by był rozwiązany (1-10)")
    wybor2 = int(input("Podaj wybor: "))
    if 1 <= wybor2 <= 10:
        rozwiazanie.rozwiaz_przyklad(wybor2, war_stop)
    else:
        print("Podano numer spoza zakresu 1-10.")

elif wybor == 2:
    zakres = input("podaj zakres przykładów (format x-y): ")
    zakres = list(map(int, zakres.split('-')))
    if zakres[0] > zakres[1]:
        print("błąd zakresu")
    if 1 < zakres[0] < 10 and 1 < zakres[1] < 10:
        for i in zakres:
            rozwiazanie.rozwiaz_przyklad(zakres, war_stop)

elif wybor == 3:
    for i in range(1,11):
        rozwiazanie.rozwiaz_przyklad(i, war_stop)

elif wybor == 4:
    sciezka = input("podaj plik z współczynnikami: ")
    rozwiazanie.wybrany_plik(sciezka, war_stop)
else:
    print ("Jak nie umiesz podać cyfry od 1 do 4, to cofnij się do przedszkola, może tam cię nauczą")
