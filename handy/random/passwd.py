import random
import string

def randomPW(N):
    return ''.join(random.choice(string.ascii_uppercase +\
                                 string.ascii_lowercase + \
                                 string.printable + \
                                 string.digits) for _ in range(N))

if __name__ == "__main__":
    print randomstr(10)