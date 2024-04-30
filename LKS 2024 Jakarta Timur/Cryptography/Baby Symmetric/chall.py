from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util import Counter
import base64
import os

FLAG = b"LKSJAKTIM{_____________________________________}" #CENSORED :)
assert len(FLAG) % 16 == 0

def encrypt(srt,key):
	c = Counter.new(128)
	cip = AES.new(key,AES.MODE_CTR,counter=c)
	result = cip.encrypt(srt)
	return base64.b64encode(result)

key = os.urandom(16)
print(encrypt(FLAG,key))
print(encrypt(b"Welcome to the land of P4 JakartaTimur Indonesia", key))
print(encrypt(b"May the best of you win into the next LKSP level",key))


#Output:
# b'uPFkG+d2LPMyzKebNR/kIaOvHSHQRQCtvbRfABhTVrLs93jbAjXJkPRA1P/UUuuM'
# b'o99bMslQHZoL2LawOxOqLK6tAF7UTRCK1tVQMixxcJTS1WTaGSKbuPhN1/jFWKOQ'
# b'udtOcdJVHZod0uWwcxnsYLasEV7MQl76i5tuPGdkaoWT72jPGHD3usV5mPrFXa+d'
