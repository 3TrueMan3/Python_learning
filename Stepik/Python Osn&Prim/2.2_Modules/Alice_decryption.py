import simplecrypt

with open('Alice_passw/encrypted.bin', 'rb') as inp, open('Alice_passw/passwords.txt', 'r') as passwords:
    encrytpted = inp.read()


   # decryption = simplecrypt.decrypt(passwords, encrytpted)
