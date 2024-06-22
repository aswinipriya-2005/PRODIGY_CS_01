def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_message += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                encrypted_message += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_message += char
    return encrypted_message

def caesar_cipher_decrypt(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                decrypted_message += chr((ord(char) - ord('a') - shift_amount) % 26 + ord('a'))
            elif char.isupper():
                decrypted_message += chr((ord(char) - ord('A') - shift_amount) % 26 + ord('A'))
        else:
            decrypted_message += char
    return decrypted_message

def main():
    while True:
        choice = input("Would you like to (E)ncrypt, (D)ecrypt, or (Q)uit? ").strip().upper()
        if choice == 'Q':
            print("Goodbye!")
            break
        if choice not in ('E', 'D'):
            print("Invalid choice, please enter 'E', 'D', or 'Q'.")
            continue

        message = input("Enter your message: ").strip()
        try:
            shift = int(input("Enter the shift value: ").strip())
        except ValueError:
            print("Shift value must be an integer. Please try again.")
            continue

        if choice == 'E':
            result = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted message: {result}")
        elif choice == 'D':
            result = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted message: {result}")

if _name_ == "_main_":
    main()
