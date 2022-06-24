import enc_dnc
import ende_key
import my_key
from pydantic import BaseModel

#암복호화 클래스 객체를 미리 생성한 키를 받아 생성한다.
simpleEnDecrypt = enc_dnc.SimpleEnDecrypt(ende_key.ende_key)

#암호화된 액세스키와 시크릿키를 읽어 복호화 한다.
api_key = simpleEnDecrypt.decrypt(my_key.my_access)
secret_key = simpleEnDecrypt.decrypt(my_key.my_secret)
passphrase = simpleEnDecrypt.decrypt(my_key.my_passphrase)

print(api_key)
print(secret_key)
print(passphrase)