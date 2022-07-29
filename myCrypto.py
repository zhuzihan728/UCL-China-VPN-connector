import base64
from Crypto.Cipher import AES

key = "itsmechabunny19c"

def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes

def encrypt_oracle(text):
    iv = "0000000000000000"
    aes = AES.new(add_to_16(key), AES.MODE_CBC, add_to_16(iv))
    bs = AES.block_size
    def pad2(s): return s + (bs - len(s) %
                                bs) * chr(bs - len(s) % bs)  # PKS7

    encrypt_aes = aes.encrypt(str.encode(pad2(text)))

    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')
    print(encrypted_text)
    return encrypted_text


def decrypt_oracle(text):
    iv = "0000000000000000"
    aes = AES.new(add_to_16(key), AES.MODE_CBC, add_to_16(iv))
    base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
    decrypted_text = str(aes.decrypt(base64_decrypted),
                            encoding='utf-8') 

    def unPad(s): return s[0:-ord(s[-1])]

    return unPad(decrypted_text)