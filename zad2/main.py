import rozwiazanie

# main do dokończenia

print("Co chcesz zrobić? \n 1. Pojedyńczy przykład \n 2. Więcej niż jeden, mniej niż wszystkie  \n 3. Wszystkie")
wybor = int(input("Podaj wybor: "))
if wybor == "1":
    print("Podaj który przykład chcesz by był rozwiązany (1-10)")
    wybor2 = int(input("Podaj wybor: "))
    if 1 <= wybor2 <= 10:
        rozwiazanie(wybor2)
    else:
        print("Podano numer spoza zakresu 1-10.")



elif wybor == "2":
elif wybor == "3":
else:
    print ("Jak nie umiesz podać cyfry od 1 do 3, to cofnij się do przedszkola, może tam cię nauczą")
