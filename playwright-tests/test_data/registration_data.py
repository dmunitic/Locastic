import time


def generate_unique_email():
    """Generate a unique email using timestamp to avoid duplicates."""
    timestamp = int(time.time() * 1000)
    return f"testuser_{timestamp}@example.com"


VALID_USER = {
    "first_name": "John",
    "last_name": "Doe",
    "email": None,  # Use generate_unique_email() at runtime
    "phone": "555-123-4567",
    "address": "123 Main St",
    "city": "New York",
    "zip_code": "10001",
    "password": "SecurePass123!",
    "confirm_password": "SecurePass123!",
    "accept_terms": True,
    "subscribe_newsletter": False,
}


def get_valid_user():
    """Returns a valid user dict with a fresh unique email."""
    data = VALID_USER.copy()
    data["email"] = generate_unique_email()
    return data


INVALID_EMAILS = [
    "notanemail",          # No @ symbol
    "user@x",              # Missing proper domain/TLD (passes weak regex)
    "@nodomain.com",       # Missing local part
    "user name@email.com", # Spaces in email
]

WEAK_PASSWORDS = [
    "123",   # Too short (below 4 char minimum)
    "1234",  # Meets minimum but far too weak by industry standards
    "abcd",  # No numbers, no special chars, only 4 chars
]
