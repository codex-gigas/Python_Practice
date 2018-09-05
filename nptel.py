def intreverse(n):
    r=0
    while(n>0):
        r=r*10+n%10
        n=n//10
    return r
def matched(s):
    t=0
    for i in s:
        if i=='(':
            t+=1
        elif i==')':
            t-=1
        if t<0:
            return(False)
    return(t==0)
def isprime(n):
    temp=0
    for i in range(2,n):
        if(n%i==0):
            temp=1
            break
    if(temp==0):
        return True
def sumprimes(l):
    sum=0
    for i in l:
        if(isprime(i) and i>0):
            sum+=i
    return sum

print(intreverse(3680))
print(intreverse(798798))
print(intreverse(7))
print(matched("(7)(a"))
print(matched("a)*(?"))
print(matched("((jkl)78(A)&l(8(dd(FJI:),):)?)"))
print(sumprimes([17,51,29,39]))
print(sumprimes([-3,-5,3,5]))
print(sumprimes([4,6,15,27]))
