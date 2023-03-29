import sys
import rsa


def decode(msg):
    # with open("Private_key.pem",'rb') as f:
    #     p = rsa.PrivateKey.load_pkcs1(f.read())
    # # print(p)
    # d = rsa.decrypt(msg, p)
    # # print("decrypted message: ", decMessage)
    # return d
    return msg


msg = sys.argv[1]
print(decode(msg))
