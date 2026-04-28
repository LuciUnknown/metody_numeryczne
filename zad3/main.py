import numpy as np
import matplotlib.pyplot as plt
import fileread
import funkcje
import newton

def wybierz_funkcje():
    print("--- Wybór funkcji do interpolacji ---")
    print("1. Funkcja liniowa (ax + b)")
    print("2. Wartość bezwzględna (|x|)")
    print("3. Wielomian")
    print("4. Funkcja trygonometryczna (np. sin, cos)")
    print("5. Złożenie funkcji (trygonometryczna z liniową)")
    
    wybor = input("Wybierz numer (1-5): ")
    
    if wybor == '1':
        a = float(input("Podaj parametr 'a': "))
        b = float(input("Podaj parametr 'b': "))
        nazwa = f"Liniowa: {a}x + {b}"
        def f_zewn(arg): return funkcje.liniowa(a, b, arg)
            
    elif wybor == '2':
        nazwa = "Wartość bezwzględna: |x|"
        def f_zewn(arg): return funkcje.bezwzgledna(arg)
            
    elif wybor == '3':
        w_str = input("Podaj współczynniki wielomianu oddzielone spacją (od najwyższej potęgi): ")
        w = [float(i) for i in w_str.split()]
        nazwa = "Wielomian"
        def f_zewn(arg): return funkcje.wielomian(w, arg)
            
    elif wybor == '4':
        f = input("Podaj nazwę funkcji trygonometrycznej (np. sin, cos, tan): ")
        nazwa = f"Trygonometryczna: {f}(x)"
        def f_zewn(arg): return funkcje.trygonometryczna(f, arg)
            
    elif wybor == '5':
        print("Złożenie: f(g(x)), gdzie f - trygonometryczna, g - liniowa (ax + b)")
        f = input("Podaj nazwę zewnętrznej funkcji trygonometrycznej (np. sin): ")
        a = float(input("Podaj 'a' dla wewnętrznej funkcji liniowej: "))
        b = float(input("Podaj 'b' dla wewnętrznej funkcji liniowej: "))
        nazwa = f"Złożenie: {f}({a}x + {b})"
        def f_zewn(arg):
            lin = funkcje.liniowa(a, b, arg)
            return funkcje.trygonometryczna(f, lin)
            
    else:
        return None
            
    return f_zewn, nazwa

def main():
    sciezka = "zmienne"
    try:
        x_nodes = fileread.read(sciezka)
        print(f"\nWczytano węzły z pliku '{sciezka}': {x_nodes}")
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku '{sciezka}'.")
        return
    except Exception as e:
        print(f"Wystąpił błąd podczas wczytywania pliku: {e}")
        return

    x_nodes = sorted(list(set(x_nodes)))
    
    if len(x_nodes) < 2:
        print("Błąd: Do wykonania interpolacji potrzebne są co najmniej 2 unikalne węzły.")
        return

    func, func_name = wybierz_funkcje()

    y_nodes = func(x_nodes)
    print("\nWartości w węzłach interpolacyjnych:")
    for x, y in zip(x_nodes, y_nodes):
        print(f"x = {x}, y = {y}")

    x_min, x_max = min(x_nodes), max(x_nodes)
    margines = (x_max - x_min) * 0.1 if x_max != x_min else 1.0
    x_dziedzina = np.linspace(x_min - margines, x_max + margines, 500).tolist()

    y_original = func(x_dziedzina)
    y_interpolated = [newton.newton(x_nodes, y_nodes, x) for x in x_dziedzina]

    plt.figure(figsize=(10, 6))
    plt.plot(x_dziedzina, y_original, label=f'Oryginalna funkcja: {func_name}', color='blue', linestyle='--', alpha=0.7)
    plt.plot(x_dziedzina, y_interpolated, label='Wielomian interpolacyjny Newtona', color='red', linewidth=2)
    plt.scatter(x_nodes, y_nodes, color='black', zorder=5, label='Węzły interpolacyjne', s=50)
    plt.title('Metoda Newtona dla nierównych odstępów argumentu')
    plt.xlabel('Oś X')
    plt.ylabel('Oś Y')
    plt.axhline(0, color='black', linewidth=0.8, linestyle='-')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='-')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.show()

if __name__ == '__main__':
    main()