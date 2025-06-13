


def fibonacci_v1(n):
    if n < 0:
        raise ValueError("Eroare")

    if n in (0,1):
        return n
        
    return fibonacci_v1(n-1) + fibonacci_v1(n-2)


def fibonacci(n):

    if n < 0:
        raise ValueError("Eroare")

    if n in (0,1):
        return n
    
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a