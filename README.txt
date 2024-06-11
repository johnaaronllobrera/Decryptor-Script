Author: John Aaron B. Llobrera
Affiliation: BS Statistics, Institute of Statistics, University of the Philippines Los Baños
E-Mail: jbllobrera@up.edu.ph

Description:
This script decrypts an encrypted file using the Fernet encryption scheme.

Usage:
1. Make sure you have the appropriate encryption key file available.
2. Update the `file_path` variable with the name of the file you want to decrypt.
3. Run the script using Python.

Instructions:
1. Read the key from the key file (`encryption_key.key`).
2. Initialize Fernet with the key.
3. Specify the file to decrypt and rewrite.
4. Open the encrypted file and read its contents.
5. Decrypt the file.
6. Write the decrypted data back to the file.
7. The script will print "File decrypted and rewritten successfully."
