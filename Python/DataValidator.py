import re

def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def is_valid_phone(phone: str) -> bool:
    pattern = r'^\+?[1-9]\d{1,14}$'  
    return bool(re.match(pattern, phone))