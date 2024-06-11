# Author: John Aaron B. Llobrera
    # Affiliation: BS Statistics, Institute of Statistics, University of the Philippines Los Baños
    # E-Mail: jbllobrera@up.edu.ph
# Description:
    # This script decrypts an encrypted file using the Fernet encryption scheme.

from cryptography.fernet import Fernet

# Read the key from the key file
with open('encryption_key.key', 'rb') as key_file: # update encryption_key with the appropriate name of the key file
    key = key_file.read()

# Initialize Fernet with the key
fernet = Fernet(key)

# File to decrypt and rewrite
file_path = 'filename.txt'  # update filename with the name of the file you want to decrypt

# Open the encrypted file
with open(file_path, 'rb') as enc_file:
    encrypted_data = enc_file.read()

# Decrypt the file
decrypted_data = fernet.decrypt(encrypted_data)

# Write the decrypted data back to the file
with open(file_path, 'wb') as dec_file:
    dec_file.write(decrypted_data)

print("File decrypted and rewritten successfully.")
