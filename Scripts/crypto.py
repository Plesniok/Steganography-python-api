from cryptography.fernet import Fernet
import base64


def prepare_key_and_message_encrypt(message, key):
    key = bytes('example', encoding='utf-8').ljust(32)
    message = message.encode()
# Encode the key using base64
    key = base64.urlsafe_b64encode(key)
    return [message, key]

def prepare_key_and_message_decrypt(message, key):
    key = bytes('example', encoding='utf-8').ljust(32)
# Encode the key using base64
    key = base64.urlsafe_b64encode(key)
    return [message, key]

def encrypt(message, key):    
    # Create a Fernet object with the user-provided key
    [message, key] = prepare_key_and_message_encrypt(message, key)
    fernet = Fernet(key)

    # Encrypt a message
    encrypted_message = fernet.encrypt(message)

    # Decrypt the message

    # Print the results
    print(f"Original message: {message}")
    print(f"Encrypted message: {encrypted_message}")
    return encrypted_message


def decrypt(message, key):    
    # Create a Fernet object with the user-provided key
    [message, key] = prepare_key_and_message_decrypt(message, key)
    fernet = Fernet(key)

    # Encrypt a message

    # Decrypt the message
    decrypted_message = fernet.decrypt(message)

    # Print the results
    print(f"Original message: {message}")
    print(f"Decrypted message: {decrypted_message}")
    return decrypted_message
