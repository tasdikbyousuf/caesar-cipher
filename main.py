def caesar(message: str, offset: int) -> None:
    """
    Encrypts a message using the Caesar cipher with the given offset.

    Args:
        message (str): The message to be encrypted.
        offset (int): The number of characters to shift each character by.

    Returns:
        None: Prints the encrypted text.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

text = input("Enter your message: ")
shift = int(input("Enter how many characters to be shifted: "))

caesar(text, shift)
