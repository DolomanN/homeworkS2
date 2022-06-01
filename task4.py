def binary(n):
    a = ''
    while n > 0:
        a = str(n % 2) + a
        n = n//2
    return a
n = 250
print (f'десятичное чило {n} при переводе в двоичну систему примет вид {binary(n)}')