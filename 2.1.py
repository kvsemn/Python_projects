import numpy as np, matplotlib.pyplot as plt


def function_fi(x1, x2):
    return -np.cos(x2) + 1, 2 + np.log(x1+1)


def function_f(x1, x2):
    return x1 - np.cos(x2) - 1, x2 - np.log(x1+1) - 2

def dfix1(x1, x2):
    return 0, 1/(x1+1)

def dfix2(x1, x2):
    return np.sin(x2), 0

def df1x1(x1, x2):
    return 1.0

def df1x2(x1, x2):
    return np.sin(x2)

def df2x1(x1, x2):
    return -1/(x1+1)

def df2x2(x1, x2):
    return 1.0

def detA1(x1, x2):
    return function_f(x1, x2)[0] * df2x2(x1, x2) - function_f(x1, x2)[1] * df1x2(x1, x2)

def detA2(x1, x2):
    return df1x1(x1, x2) * function_f(x1, x2)[1] - df2x1(x1, x2) * function_f(x1, x2)[0]


def detJ(x1, x2):
    return df1x1(x1, x2) * df2x2(x1, x2) - df2x1(x1, x2) * df1x2(x1, x2)


def norm(b):
    max = 0
    for i in range(len(b)):
        if b[i] > max:
            max = b[i]
    return max


def simple_iter(eps, q, a, b):
    X_prev = [a, a]
    X_k = [function_fi(a, a)[0], function_fi(a, a)[1]]
    eps_k = []
    for i in range(len(X_k)):
        eps_k.append(abs(X_prev[i] - X_k[i]))
    while q / (1 - q) * norm(eps_k) > eps:
        X_prev[0] = X_k[0]
        X_k[0] = function_fi(X_k[0], X_k[1])[0]
        X_prev[1] = X_k[1]
        X_k[1] = function_fi(X_k[0], X_k[1])[1]
        for i in range(len(eps_k)):
            eps_k[i] = abs(X_prev[i] - X_k[i])
    X_k.reverse()
    return X_k


def newton_method(eps, a, b):
    X_prev = [0, 0]
    X_k = [function_f((a + b) / 2, (a + b) / 2)[0], function_f((a + b) / 2, (a + b) / 2)[1]]
    eps_k = []

    for i in range(len(X_k)):
        eps_k.append(abs(X_prev[i] - X_k[i]))
    while norm(eps_k) > eps:
        x1 = detA1(X_k[0], X_k[1]) / detJ(X_k[0], X_k[1])
        x2 = detA2(X_k[0], X_k[1]) / detJ(X_k[0], X_k[1])
        X_prev[0] = X_k[0]
        X_prev[1] = X_k[1]
        X_k[0] -= x1
        X_k[1] -= x2
        for i in range(len(eps_k)):
            eps_k[i] = abs(X_k[i] - X_prev[i])
    X_k.reverse()
    return X_k


def main():
    eps = 0.0001
    plt.title("Графики функций")
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.grid()
    x1 = np.linspace(-10, 10, 100)
    x2 = np.linspace(-10, 10, 100)
    y = function_fi(x1, x2)
    plt.plot(x1, y[0], y[1], x2)
    plt.show()

    #точка пересечения графиков функций
    x1 = 2.3
    x2 = 0.34
    #область по X
    a = 0.94
    b = 3.5

    #достаточное условие сходимости метода простых итераций
    diff_fi = [dfix1(x1, x2)[0], dfix2(x1, x2)[0], dfix1(x1, x2)[1], dfix2(x1, x2)[1]]
    for i in range(len(diff_fi)):
        diff_fi[i] = abs(diff_fi[i])
    if (norm(diff_fi) < 1):
        q = max(diff_fi)
        print("Достаточное условие сходимости итерационного процесса выполнено.\n")

    print("Методом простых итераций:\n"
          "Решение уравнения: ", simple_iter(eps, q, a, b))


    print("\nМетодом Нюьтона:\n"
          "Решение уравнения: ", newton_method(eps, a, b))


main()