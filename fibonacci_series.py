def fibonacci_series(n):
    if n <= 2:
        return 1

    fib_x, fib_next = 1, 1

    i = 3
    while i <= n:
        i += 1
        fib_x, fib_next = fib_next, fib_x + fib_next
    return fib_next


list_fibo = []
if __name__ == '__main__':
    for x in range(1, 11):
        item = fibonacci_series(x)
        list_fibo.append(item)

print(list_fibo)