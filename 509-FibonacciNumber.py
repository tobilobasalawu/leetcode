def fib(n: int) -> int:
    if n == 1:
        return 1

    elif n == 0:
        return 0

    else:
        prev = 0
        current = 1
        for i in range(2, n+1):
            new = prev + current
            prev = current
            current = new
        return current