import numpy as np
import file_reader
import gausse_seidel

# Ogólnie, nie zrobiłem tu jeszcze żeby rozróżniać warunek stopu i tyle

def rozwiaz_przyklad(numer,war_stop):
    sciezka = f"przyklady_do_rozw/{numer}.txt"
    print(f"\n--- Rozwiązywanie przykładu {numer} z pliku {sciezka} ---")

    try:
        tabela = file_reader.read_coefficient(sciezka)
        if not tabela:
            print("Plik jest pusty.")
            return

        A = []
        b = []
        for wiersz in tabela:
            A.append(wiersz[:-1])  # Wszystko oprócz ostatniego elementu w rzędzie
            b.append(wiersz[-1])  # Tylko ostatni element w rzędzie

        A = np.array(A)
        b = np.array(b)

        gausse_seidel.diag_dominacja(A)

        # wynik = gausse_seidel.iter_Gauss_Seidel(A, b, max_iter=20)
        # wynik = gausse_seidel.acc_Gauss_Seidel(A, b, tol=0.0000001)
        # print("Znalezione rozwiązanie (x):", wynik)

    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku {sciezka}.")
