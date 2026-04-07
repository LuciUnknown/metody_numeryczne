import matplotlib.pyplot as plt
import numpy as np

def wykres(a, b, f, w, title):
    x = np.linspace(a, b, 200)
    y = []
    for i in x:
        y.append(f(i))

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label="f(x)")
    plt.plot(w, f(w), "o", color="blue")
    plt.title(title)
    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)
    plt.grid(True)
    plt.legend()
    plt.show()
