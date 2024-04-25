def nf(n):
    print("hii")
    if n<=1:
        return n
        print("last")
    else:
        return nf(n-1)+ nf(n-2)
    print(nf(6))
    print("Bye")    