import threading
import time
import multiprocessing
import math
# Функции для АТ-01
# запускать с n = 700008
def fibonacci(n):  # содержимое функции не менять
    """Возвращает последнюю цифру n-е числа Фибоначчи."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(f'fibonacci = {b % 10}')


# запускать с f, a, b, n равными соответственно math.sin, 0, math.pi, 20000000
def trapezoidal_rule(f, a, b, n):  # содержимое функции не менять
    """Вычисляет определенный интеграл функции f от a до b методом трапеций с n шагами."""
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        integral += f(a + i * h)
    print(f'trapezoidal_rule = {integral * h}')


def sequence():
    print("Начинаем последовательное выполнение...")
    start_time = time.time()
    fibonacci(700008)
    trapezoidal_rule(math.sin, 0, math.pi, 20000000)
    end_time = time.time()
    print(f'sequence time: {end_time - start_time: 0.2f} секунд \n')


def threads():
    print("Начинаем выполнение с использованием потоков...")
    start_time = time.time()
    thread1 = threading.Thread(target=fibonacci, args=(700008,))
    thread2 = threading.Thread(target=trapezoidal_rule, args=(math.sin, 0, math.pi, 20000000))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    end_time = time.time()
    print(f'threads time: {end_time - start_time: 0.2f} секунд \n')


def processes():
    print("Начинаем выполнение с использованием процессов...")
    start_time = time.time()
    process1 = multiprocessing.Process(target=fibonacci, args=(700008,))
    process2 = multiprocessing.Process(target=trapezoidal_rule, args=(math.sin, 0, math.pi, 20000000))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    end_time = time.time()
    print(f'processes time: {end_time - start_time: 0.2f} секунд \n')


if __name__ == '__main__':
    #sequence()
    #threads()
    processes()
