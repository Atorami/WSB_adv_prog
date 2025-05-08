# Tworzenie dwóch list
# Dokumentacja: https://docs.python.org/3/library/functions.html#zip

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

# Łączenie list za pomocą funkcji zip()
# Dokumentacja: https://docs.python.org/3/library/random.html#module-random
combined = list(zip(list1, list2))
print("Combined list:", combined)

# Wykorzystanie funkcji z modułu random
import random
random_number = random.randint(1, 100)
print("Random number:", random_number)

# Obsługa wyjątku try-except
# Dokumentacja: https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
try:
    result = 10 / 0 
except ZeroDivisionError as e:
    print("Error:", e)
