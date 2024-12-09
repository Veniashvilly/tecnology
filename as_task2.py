import asyncio
import time
import math
async def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(f'fibonacci = {b % 10}')
async def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        integral += f(a + i * h)
    print(f'trapezoidal_rule = {integral * h}')
async def main():
    start_time = time.time()
    await asyncio.gather(
        fibonacci(700008),
        trapezoidal_rule(math.sin, 0, math.pi, 20000000)
    )
    end_time = time.time()
    print(f'time: {end_time - start_time:.2f} секунд\n')
asyncio.run(main())
