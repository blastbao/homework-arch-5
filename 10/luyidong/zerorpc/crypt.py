from Crypto import Random
from Crypto.Cipher import AES 
import base64

BS = 16
#Padding data  è®¡ç®æ°æ®å¤§å°ï¼åä¸åæ´ï¼ï¼é¿åº¦ä¸è¶³16byteéè¡¥é½ï¼chræ ¹æ®æ°å­å¤§å°è¿è¡ASCIIè½¬å
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
#unpadding data  padéè¿ç®
unpad = lambda s : s[0:-ord(s[-1])]
#å å¯çå¯é¥ï¼é¿åº¦16byte
KEY = "1234456twedfdsgf"

def encrypt( raw ):
    raw = pad(raw)
    iv = Random.new().read( AES.block_size )
    cipher = AES.new( KEY, AES.MODE_CBC, iv )
    return base64.b64encode( iv + cipher.encrypt( raw ) ) 

def decrypt( enc ):
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(KEY, AES.MODE_CBC, iv )
    return unpad(cipher.decrypt( enc[16:] ))
