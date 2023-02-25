

def factorial(n: int):
    if n>0:
        p = 1
        i = 1
        while(n>=i):
            p *= i
            i += 1
        return p
    elif n == 0:
        return 1
    else:
        print("0>N")
        return -1