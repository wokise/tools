import hashlib
import magic
import sys


def get_ftype(file):
    with open(file, 'rb') as f:
        content = f.read(2048)
        ftype = magic.from_buffer(content)
    return ftype


def get_hashes(file):
    content = open(file, "rb").read()
    md5 = hashlib.md5(content).hexdigest()
    sha256 = hashlib.sha256(content).hexdigest()
    sha1 = hashlib.sha1(content).hexdigest()
    return {
        'MD5': md5,
        'SHA256': sha256,
        'SHA1': sha1
    }


if __name__ == "__main__":
    if sys.argv[1:]:
        file = sys.argv[1]
        ftype = get_ftype(file)
        hashes = get_hashes(file)
        print('Filetype:', ftype)
        print('\nHashes')
        for key, value in hashes.items():
            print(f'{key}: {value}')
