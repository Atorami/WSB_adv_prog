def is_palindrome(text):
   # Sprawdza, czy tekst jest palindromem
    cleaned = ''.join(text.lower().split())
    return cleaned == cleaned[::-1]

def clean_text(text):
    # Usuwa znaki specjalne i cyfry z tekstu.
    return ''.join(filter(str.isalpha, text))

def count_words(text):
    # Zlicza liczbę słów w tekście.
    return len(text.strip().split())