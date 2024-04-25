def fact(n):
    print("Hello")
    if(n==0):
        return 1
    return n*fact(n-2)
print(fact(8))
print("Hi")