fib1=0
fib2=1
count=0
print("Enter a number\t")
n=input()
print("fibonacci series is\n")
print(fib1)
print(fib2)
count=2
while count<n:
    fib3=fib1+fib2
    count+=1
    print(fib3)
    fib1=fib2
    fib2=fib3
