import requests
from bs4 import BeautifulSoup

# Pobiera stronę internetową pod wskazanym adresem URL
url = 'https://portal.wsb.pl/'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

# Wyszukuje i wypisuje wszystkie formularze na stronie oraz ich pola input
print("Forms found on page:")
for form in soup.find_all('form'):
    print("Form action:", form.get('action'))
    for inp in form.find_all('input'):
        print("  Input:", inp.get('name'))

# Sprawdza i wypisuje wybrane nagłówki bezpieczeństwa HTTP
print("\nSecurity headers:")
for header in ['X-Frame-Options', 'Content-Security-Policy', 'X-XSS-Protection', 'Strict-Transport-Security']:
    print(f"{header}: {resp.headers.get(header)}")