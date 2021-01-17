def f(x):
    return x**2

# Przypisanie wyniku funkcji do zmiennej
y1 = f(4)
print(y1)

# Przypisanie funkcji do zmiennej
y2 = f
print(y2)
print(y2(4))

# Lambda
y3 = lambda x: x**2
print(y3(4))


# Znajdź kwadraty liczb naturalnych od 1 do 10 większe od 50.
# Sposób pierwszy
def square(x):
    return x**2

result = []
for num in range(1, 11):
    num_square = square(num)
    if num_square > 50:
        result.append(num_square)

print(f"Pierwszy wynik: {result}")

# Sposób drugi - funkcyjny
result = list(filter(lambda x: x>50, map(lambda x:x**2, range(1,11))))
print(f"Drugi wynik: {result}")

# Funkcja map
def f2(x):
    """Podnosi do kwadratu"""
    return x**2

print(list(map(f2, [1,2,3,4,45])))

# Funkcja filter
def f3(x):
    """Sprawdza, czy liczba jest parzysta"""
    if x%2 == 0:
        return True
    return False

print(list(filter(f3, [1,2,3,4,45])))

def func(x):
    return (x[0]**2 + x[1]**2) ** 0.5

# Funkcja min (tak samo max, sort)
print(min([(1,2), (3,4), (5,6)], key=func))