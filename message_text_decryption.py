for person, messages in message_data.items():
    for message in messages:
        ciphertext = bytes.fromhex(message["message"])
        decrypted_message = decrypt_message(ciphertext, shared_secret_key)
        message["message"] = decrypted_message

print("Decrypted message_data dictionary:")
print(message_data)