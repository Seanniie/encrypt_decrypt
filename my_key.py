# #-*-coding:utf-8 -*-

# from cryptography.fernet import Fernet

# class SimpleEnDecrypt:
#     def __init__(self, key=None):
#         if key is None: # 키가 없다면
#             key = Fernet.generate_key() # 키를 생성한다
#         self.key = key
#         self.f   = Fernet(self.key)
    
#     def encrypt(self, data, is_out_string=True):
#         if isinstance(data, bytes):
#             ou = self.f.encrypt(data) # 바이트형태이면 바로 암호화
#         else:
#             ou = self.f.encrypt(data.encode('utf-8')) # 인코딩 후 암호화
#         if is_out_string is True:
#             return ou.decode('utf-8') # 출력이 문자열이면 디코딩 후 반환
#         else:
#             return ou
        
#     def decrypt(self, data, is_out_string=True):
#         if isinstance(data, bytes):
#             ou = self.f.decrypt(data) # 바이트형태이면 바로 복호화
#         else:
#             ou = self.f.decrypt(data.encode('utf-8')) # 인코딩 후 복호화
#         if is_out_string is True:
#             return ou.decode('utf-8') # 출력이 문자열이면 디코딩 후 반환
#         else:
#             return ou

# simpleEnDecrypt = SimpleEnDecrypt(b'Z6k1HV6E77zT6arfFKcpM7YSK5oMs603cbqO1dURv-I=') #ende_key.py 에 있는 키를 넣으세요

# access = "werwerwerwer123123123"
# secret = "cvxcvzxcvzcvqweqweqwe123123123"
# passphrase = "bdcbcvbxb12312312"

# print("access_key: ", simpleEnDecrypt.encrypt(access))
# print("scret_key: ", simpleEnDecrypt.encrypt(secret))
# print("passphrase: ", simpleEnDecrypt.encrypt(passphrase))

my_access = "gAAAAABitTYp2uv5oPY7_qKEshRzxcPDdtQF3iqwv-WVKkvxdDe7k-DHyfF43lNLdqKSbQsfhFzxkYHsvvFfh9isQkNpdv243kRXErZKSsum8Se9y7hN0zs=" 
my_secret = "gAAAAABitTYpWAb-6M8lwZebIY32e4ivg_IL-pRW09gRqeTWeiW7urrbm6k8cBpuecpTj8qBFin4c4lBMBlHczPjweMNKWWQJenfpzflC_QMHCaik-j-3Jk=" 
my_passphrase = "gAAAAABitTYpqcTJKdtKZ6CIrFFhrtC6unrtFHDDZwtnNpYmZqgOjzxRR1dMh7yyBPZIIUMHdbg6pJpFGXXSSUzvCflZXJFrAHQ0BODXFIeV0rF5G6rXkmM="
