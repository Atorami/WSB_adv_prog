import re
from datetime import datetime

def is_valid_email(email):
    # Sprawdzenie poprawnośći adresu e-mail
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def convert_date_format(date_str):
    # Konwertuje datę z DD-MM-YYYY na YYYY-MM-DD
    try:
        date = datetime.strptime(date_str, "%d-%m-%Y")
        return date.strftime("%Y-%m-%d")
    except ValueError:
        raise ValueError("Niepoprawny format daty")
    
