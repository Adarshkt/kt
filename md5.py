import hashlib


def md5():
    a="Adarsh"
    b=a.encode()
    c=hashlib.md5(b)
    hexa=c.hexdigest()
    print(hexa)
    return
md5()