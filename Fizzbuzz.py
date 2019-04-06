def fizz_buzz(n):
    return [(not n % 3) * 'Fizz' + (not n % 5) * 'Buzz' or n for n in range(1, n+1)]

b=int(input())
a=[x for x in map(int,input().split(" "))]
for j in a:
    m=fizz_buzz(j)
    for k in m:
        print(k)
