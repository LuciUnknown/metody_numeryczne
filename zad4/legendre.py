import numpy as np

def gauss_legendre_quadrature(f, a, b, n):

    # Parametry:
    # f : callable - funkcja podcałkowa f(x)
    # a : float - dolna granica całkowania
    # b : float - górna granica całkowania
    # n : int - liczba węzłów (punktów) kwadratury

    wezly_standardowe, wagi = np.polynomial.legendre.leggauss(n)

    wezly_przeskalowane = 0.5 * (b - a) * wezly_standardowe + 0.5 * (b + a)

    wartosc_calki = 0.5 * (b - a) * np.sum(wagi * f(wezly_przeskalowane))

    return wartosc_calki
