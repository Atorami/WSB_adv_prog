# awesome_lib

**awesome_lib** biblioteka Pythona zawierająca zestaw przydatnych funkcji do przetwarzania danych, operacji matematycznych i manipulacji tekstem

##  Główne możliwości

- Walidacja danych (np. adresów e-mail)
- Proste operacje matematyczne (dodawanie, pole figury)
- Przetwarzanie tekstu (sprawdzanie palindromów, odwracanie tekstu)

##  Struktura modułów

- **math_tools.py** – proste działania matematyczne: dodawanie, obliczanie pola.
- **text_processing.py** – operacje na tekście: sprawdzanie palindromu, odwracanie tekstu.
- **data_utils.py** – przetwarzanie danych: walidacja adresów e-mail.

##  Instalacja

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/twoja-nazwa-uzytkownika/awesome_lib.git
   cd awesome_lib

##  Testy jednostkowe
    ```bash
    python -m unittest discover tests 


###  Przykład uruchomienia testów dla jednego modułu:

    ```bash
    python -m unittest tests.test_math_tools

### Przykłady użycia
    ```python
    # math_tools
    from awesome_lib.math_tools import add_numbers, calculate_area

    print(add_numbers(3, 7))         # ➜ 10
    print(calculate_area(5, 4))      # ➜ 20

    # text_processing
    from awesome_lib.text_processing import is_palindrome, reverse_text

    print(is_palindrome("kajak"))    # ➜ True
    print(reverse_text("Python"))    # ➜ "nohtyP"

    # data_utils
    from awesome_lib.data_utils import validate_email

    print(validate_email("test@test.com"))   # ➜ True
    print(validate_email("niepoprawny-email"))  # ➜ False

## Wymagania
- Python 3.7+
- Moduły z biblioteki standardowej (np. re, unittest)

## Autor
- A. Martsinkevich
- Rok: 2025
- Wersja: 1.0.0

## Licencja

Projekt udostępniany na licencji MIT – możesz używać, kopiować, modyfikować i rozpowszechniać bez ograniczeń.