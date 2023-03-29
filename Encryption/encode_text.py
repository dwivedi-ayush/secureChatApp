import sys
import rsa

def encode(msg):
    # publicKey, privateKey = rsa.newkeys(2048)
    # with open("Public_key.pem",'wb') as f:
    #     f.write(publicKey.save_pkcs1("PEM"))
    # with open("Private_key.pem",'wb') as f:
    #     f.write(privateKey.save_pkcs1("PEM"))
    
    
    # # rsa.encrypt method is used to encrypt string with public key string should be encode to byte string before encryption
    # e = rsa.encrypt(msg.encode(),publicKey)
    

    # return e
    return msg


msg = sys.argv[1]
print(encode(msg))
