import magic
import sys


def get_ftype(file):
    with open(file, 'rb') as f:
        file = f.read(2048)
        ftype = magic.from_buffer(file)
    return ftype

if __name__ == "__main__":
    if sys.argv[1:]:
        file = sys.argv[1]
        ftype = get_ftype(file)
        print(ftype)
