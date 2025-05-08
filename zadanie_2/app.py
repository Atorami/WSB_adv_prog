import re
from datetime import datetime

def is_valid_email(email):
    """Sprawdza, czy adres e-mail jest poprawny."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def calculate_rectangle_area(length, width):
    """Oblicza pole prostokąta."""
    if length < 0 or width < 0:
        raise ValueError("Wymiary muszą być nieujemne")
    return length * width

def filter_even_numbers(numbers):
    """Filtruje parzyste liczby z listy."""
    return [n for n in numbers if n % 2 == 0]

def convert_date_format(date_str):
    """Konwertuje datę z formatu 'DD-MM-YYYY' na 'YYYY/MM/DD'."""
    try:
        date_obj = datetime.strptime(date_str, '%d-%m-%Y')
        return date_obj.strftime('%Y/%m/%d')
    except ValueError:
        raise ValueError("Nieprawidłowy format daty. Oczekiwany 'DD-MM-YYYY'.")

def is_palindrome(text):
    """Sprawdza, czy tekst jest palindromem."""
    cleaned_text = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned_text == cleaned_text[::-1]

