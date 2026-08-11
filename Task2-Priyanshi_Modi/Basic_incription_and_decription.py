def encrypt(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result

def decrypt(ciphertext: str, shift: int) -> str:
    result = ""
    for char in ciphertext:
        if char.isupper():
            result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += char
    return result

if __name__ == "__main__":
    plaintext = input("Enter text to encrypt: ")
    shift = int(input("Enter shift key (e.g., 3): "))

    encrypted = encrypt(plaintext, shift)
    decrypted = decrypt(encrypted, shift)

    print(f"Plaintext → {plaintext}")
    print(f"Encrypted → {encrypted}")
    print(f"Decrypted → {decrypted}")
