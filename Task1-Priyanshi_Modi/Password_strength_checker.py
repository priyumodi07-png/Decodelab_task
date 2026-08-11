import hmac

def check_password_strength(password: str) -> str:
    if len(password) < 8:
        return "Weak (Too short)"

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)
    has_unicode = any(ord(char) > 127 for char in password)

    leaked_passwords = {"password", "123456", "qwerty", "letmein", "admin", "welcome"}
    if password.lower() in leaked_passwords:
        return "Weak (Common leaked password)"

    score = sum([has_upper, has_lower, has_digit, has_symbol, has_unicode])

    if score >= 4 and len(password) >= 12:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"

def verify_password(input_password: str, stored_password: str) -> bool:
    return hmac.compare_digest(input_password, stored_password)

if __name__ == "__main__":
    pwd = input("Enter a password: ")
    print(f"Strength → {check_password_strength(pwd)}")

    stored = "StrongPass!2026"
    if verify_password(pwd, stored):
        print("Secure comparison → Password matches stored value")
    else:
        print("Secure comparison → Password does not match")
