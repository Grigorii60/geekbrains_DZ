def fact(n):
    i = 1
    for el in range(n):
        el += 1
        i *= el
        yield i


n = 5

for el in fact(n):
    print(el)

    """Как в методичке"""
g = fact(n)
print(g)

for el in g:
    print(el)
