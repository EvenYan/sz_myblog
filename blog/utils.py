import hashlib


def gen_secret(passwd):
    sha = hashlib.sha512()
    sha.update(passwd.encode('utf-8'))
    return sha.hexdigest()