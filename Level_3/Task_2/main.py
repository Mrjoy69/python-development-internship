from cryptography.fernet import Fernet, InvalidToken


def generate_key():
    """Generate and save a secret encrption key."""

    try:

        with open("secret.key", "rb") as key_file:
            key_file.read()

        print("An encryption key already exists.")

    except FileNotFoundError:

        key = Fernet.generate_key()

        with open("secret.key", "xb") as key_file:
            key_file.write(key)

        print("\nEncription key generated successfully!\n")

def load_key():
    """Load the saved encrytion key."""

    with open("secret.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(filename):
    """Encrypt a file and save the encrypted contents"""

    try:

        key = load_key()
        fernet = Fernet(key)
    
        with open(filename, "rb") as file:
            original_data = file.read()
    
        encrypted_data = fernet.encrypt(original_data)
    
        with open(filename + ".encrypted", "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)
    
        print(f"\nFile '{filename}' Encrypted successfully!\n")
        
    except FileExistsError:
        print("\nError: The file or encryption key could not be found\n")

    except OSError as error:
        print(f"\nFile error: {error}\n")

    
def decrypt_file(filename):
    """Decrypt and encrypted file and save the recovered contents."""

    try:

        key = load_key()
        fernet = Fernet(key)
    
        with open(filename, "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()
    
        decrypted_data = fernet.decrypt(encrypted_data)
    
        output_filename = filename.removesuffix(".encrypted") + ".decrypted"
    
        with open(output_filename, "wb") as decrypted_file:
            decrypted_file.write(decrypted_data)
    
        print(f"\nFile '{filename}' decrypted successfully!\n")
        print(f"\nDecrypted file saved as '{output_filename}'.\n")

    except FileNotFoundError:
        print("\nError: The encrypted file or encryption key could not be found.\n")

    except InvalidToken:
        print("\nError: Decryption failed. The key may be incorrect, or the file may be corrupted\n")

    except OSError as error:
        print(f"\nfile error: {error}\n")


def main():
    """Display the menu and handle user choices"""

    while True:
        print("\n=================================")
        print("   FILE ENCRYPTION APPLICATION")
        print("=================================")
        print("1. Generate encryption key")
        print("2. Encrypt a file")
        print("3. Decrypt a file")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()


        if choice == "1":
            generate_key()

        if choice == "2":
            filename = input("Enter the file to encrypt: ").strip()
            encrypt_file(filename)

        elif choice == "3":
            filename = input("Enter the encrypted file to decrypt: ").strip()
            decrypt_file(filename)

        elif choice == "4":
            print("\nThank you for using the application.\n")
            break

        else:
            print("\nInvalid choice. Please enter 1,2, 3, or 4.\n")


if __name__ == "__main__":
    main()