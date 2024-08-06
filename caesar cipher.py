import getpass

print("-------------------------------------------- Caesar Cipher Tool --------------------------------------------------")
print("")

def analyze_message(message):
    num_letters = sum(c.isalpha() for c in message)
    num_digits = sum(c.isdigit() for c in message)
    num_special = len(message) - num_letters - num_digits

    print(f"Check whether the message you provided was correct or not using the following hints:")
    print(f"\nFirst and Last characters of the message: {message[:1]}***{message[-1]}")
    print(f"Total number of characters entered: {len(message)}")
    print(f"Number of alphabetical letters: {num_letters}")
    print(f"Number of digits: {num_digits}")
    
    if num_special > 0:
        print(f"Number of special characters: {num_special}")
        print("Special characters are present in the message.")
    else:
        print("No special characters in the message.")

def caesar_cipher(text, shift, action):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            if action == 'e':
                result_char = chr((ord(char) - start + shift) % 26 + start)
            elif action == 'd':
                result_char = chr((ord(char) - start - shift) % 26 + start)
            else:
                raise ValueError("Invalid action. Use 'e' to Encrypt or 'd' to Decrypt")
            result += result_char
        else:
            result += char
    return result

def main():
    while True:
        action = input("Do you want to encrypt or decrypt a message? Input 'e' for Encryption, 'd' for Decryption, or 'q' to Quit: ").lower()
        if action == 'q':
            print("Exiting the program. Goodbye!")
            return
        elif action in ['e', 'd']:
            break
        else:
            print("Invalid action. Please choose 'e', 'd', or 'q'.")

    if action == 'q':
        return

    # Use of getpass to make the message input invisible
    message = getpass.getpass(prompt="Enter the message: ")

    if action != 'q':
        analyze_message(message)

        # Use of getpass to make the shift value input invisible
        shift = int(getpass.getpass(prompt="Enter the shift value (invisible, type carefully): "))

        if action == 'e':
            result = caesar_cipher(message, shift, 'e')
            print("\nEncrypted Message:", result)
        elif action == 'd':
            result = caesar_cipher(message, shift, 'd')
            print("\nDecrypted Message:", result)

if __name__ == "__main__":
    main()
