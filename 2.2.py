from random import uniform
import matplotlib.pyplot as plt
import math
import np

def simpl_iterations(min, max, q, eps, x_0, f, lymbda):
     x_prev = 0
     iterations = 0
     x_k = x_0

     while (q/(1-q)*abs(x_k - x_prev) > eps):
         if(f==1):
             phi_x_k = math.acos(0.5 - 0.25 * x_k)
         if(f==2):
             phi_x_k = x_k - lymbda * (math.cos(x_k) + 0.25 * x_k - 0.5)

         print(iterations,": ","X_k: ", x_k," Phi(x): ", phi_x_k)
         x_prev = x_k
         x_k = phi_x_k
         iterations = iterations + 1

     print('Решение было найдено за ', iterations, ' итераций.')
     print('X(*): ', x_k)

def method_Nutona(eps, x_0):
    x_prev = 0
    x_k = x_0
    iterations = 0
    while(abs(x_k - x_prev) > eps):

        f_x = math.cos(x_k) + 0.25 * x_k - 0.5
        f_Xx = -math.sin(x_k) + 0.25

        print(iterations, ": X_k: ", x_k, "f(x_k): ", f_x, "f'(x_k): ",
              f_Xx, "-f(x_k)/f'(x_k): ", -f_x/f_Xx)
        iterations = iterations + 1

        x_prev = x_k
        x_k = x_prev - (f_x/f_Xx)

    print('Решение было найдено за ', iterations, ' итераций.')
    print('X(*): ', x_k)

def show_graphics(min, max, title):
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    # Начало и конец изменения значения X, разбитое на 100 точек
    x = np.linspace(min, max, 100)
    y = np.cos(x)
    y1 = 0.5 - 0.25 * x
    # Вывод графика
    plt.grid()
    ax.plot(x, y)
    ax.plot(x, y1)
    plt.show()

if __name__ == '__main__':
    show_graphics(-10, 10, 'График F1(x) и F2(x)')

    #min = 1.38; max = 1.5; f=1

    min = 3.0; max = 4.5; f=2
    eps = 0.001
    q = 0

    show_graphics(min, max, 'График отдельной области')

    #Проверка выполнения достаточного условия для метода простых итераций
    x_0 = uniform(min, max)
    if (f==1):
        phi_x = math.acos(0.5 - 0.25 * x_0)
        phi_Xx = 1 / (math.sqrt(-x_0 ** 2 + 4 * x_0 + 12))

        print("\nМетод простых итераций")
        if min <= phi_x <= max:
            print("Phi(x) принадлежит заданному промежутку: ", phi_x)

            if abs(phi_Xx) <= 1:
                q = abs(phi_Xx)
                print("Phi(x)' <= 1 = ", q)
                print("Условия теоремы 2.3 выполнены.")
                simpl_iterations(min, max, q, eps, x_0, f, 0)

    #Представляем ур-ие в форме: phi_x=x-lymb(cos(x)+0.25*x-0.5)
    if (f==2):
        #lymbda = 1/(max(0.25-math.sin(x_0)))
        lymbda = 1 / (0.25 - math.sin(max))
        phi_Xx =abs((1-lymbda*(0.25 - math.sin(x_0))))
        if(phi_Xx < 1):
            q = phi_Xx
            print("\nМетод простых итераций")
            print("Phi(x)' <= 1 = ", q)
            print("Условия теоремы 2.3 выполнены.")
            simpl_iterations(min, max, q, eps, x_0, f, lymbda)


    print("\nМетод Ньютона")


    x_0 = 1.5
    #x_0 = 4.5

    f_x = math.cos(x_0) + 0.25 * x_0 - 0.5
    f_Xx = -math.sin(x_0) + 0.25
    f_X2x = -math.cos(x_0)

    if(abs(f_x * f_X2x) < f_Xx **2):
        print("Выполняется условия теоремы 2.2: f'(x_0) f''(x_0) > 0")
        method_Nutona(eps, x_0)
    else: print("Условия теоремы 2.2 не выполняются")


