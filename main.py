def caesar(message: str, offset: int) -> None:
    """
    Encrypts a message using the Caesar cipher with the given offset.

    Args:
        message (str): The message to be encrypted.
        offset (int): The number of characters to shift each character by.

    Returns:
        None: Prints the encrypted text.
    """
    # Define the alphabet for the Caesar cipher
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    # Iterate through each character in the message
    for char in message.lower():
        # If the character is a space, append it to the encrypted text as is
        if char == ' ':
            encrypted_text += char
        else:
            # Find the index of the character in the alphabet
            index = alphabet.find(char)
            # Calculate the new index after shifting by the offset
            new_index = (index + offset) % len(alphabet)
            # Append the encrypted character to the encrypted text
            encrypted_text += alphabet[new_index]
    
    # Print the original and encrypted text
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

# Get user input for the message and the shift offset
text = input("Enter your message: ")
shift = int(input("Enter how many characters to be shifted: "))

# Encrypt the message using the Caesar cipher with the given shift offset
caesar(text, shift)
