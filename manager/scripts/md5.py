import hashlib
def strtomd5(str):
    h1=hashlib.md5()
    h1.update(str.encode(encoding='utf-8'))
    md5code=h1.hexdigest()
    return md5code
