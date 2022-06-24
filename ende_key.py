#-*-coding:utf-8 -*-
#주석풀고 아래 ende_key 주석걸고 암호화 키 생성

from cryptography.fernet import Fernet

Key = Fernet.generate_key()

print(Key)


ende_key = b'Z6k1HV6E77zT6arfFKcpM7YSK5oMs603cbqO1dURv-I='