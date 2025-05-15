def rectangle_area(width, height):
    # Oblicza pole prostokąta
    if width < 0 or height < 0:
        raise ValueError("Wymiary muszą być nieujemne")
    return width * height

def average(numbers):
    # Zwraca średnią arytmetyczną z listy liczb
    if not numbers:
        raise ValueError("Lista nie może być pusta")
    return sum(numbers) / len(numbers)

def factorial(n):
    # Oblicza silnię liczby całkowitej n
    if n < 0:
        raise ValueError("n musi być nieujemne")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result