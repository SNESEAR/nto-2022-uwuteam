from base64 import b64decode as decode
from Cryptodome.Cipher import AES
from glob import glob

files = glob("*.*")
files.remove("decrypter.py")

key = decode("XBiCgzoS309lK6RWDfmn0+jUhCkmcG71VHKvonaNmVY=")
iv = decode("3PoFUYMIhaWpYPaA5URy5g==")
for file in files:
    with open(file, "rb") as f:
        data = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    result = cipher.decrypt(data)[len(iv):]
    with open(f"decrypt/{file.rsplit('.', 1)[0]}", "wb") as f:
        f.write(result)