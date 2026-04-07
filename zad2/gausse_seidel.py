import numpy as np

def diag_dominacja(A):
    D = np.abs(np.diag(A))
    S = np.sum(np.abs(A), axis=1) - D
    if np.all(D > S):
        print("Sukces: Macierz jest silnie diagonalnie dominująca (zbieżność gwarantowana).")
        return True
    else:
        print("Ostrzeżenie: Macierz nie jest diagonalnie dominująca. (brak zbieżności)")
        return False

def iter_Gauss_Seidel(A, b, max_iter):
    i = 0
    n = len(A)
    x = np.zeros(n)
    while i < max_iter:
        s = 0
        for j in range(n):
            if j != i:
                s += A[i][j]*x[j]
        x[i] = (b[i] - s)/A[i][i]
    return x

def acc_Gauss_Seidel(A, b, tol):
    n = len(A)
    x = np.zeros(n)
    k = 0

    while True:
        k += 1
        stare_x = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x[j] for j in range(i))
            s2 = sum(A[i][j] * stare_x[j] for j in range(i + 1, n))
            x[i] = (b[i] - s1 - s2) / A[i][i]

        roznica_wektorow = np.abs(x - stare_x)
        max_roznica = np.max(roznica_wektorow)

        if max_roznica < tol:
            print(f"Osiągnięto zadaną dokładność po {k} iteracjach.")
            return x

        if k > 1000:
            print("Przerwano: przekroczono 1000 iteracji (możliwy brak zbieżności).")
            return x

    return x

