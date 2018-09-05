def sqrte(n):
    for i in range(n):
        if n==i*i:
            print(float(i))
            break
    return float(i)

p=input("Enter a number : ")
sqrte(p)
