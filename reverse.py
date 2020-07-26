


def pal_rev():
    while True:
        n = int(input())

        b = str(n)
        m = int(b[::-1])
        n += m
        print(n)
    # return n 


pal_rev()