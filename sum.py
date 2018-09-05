#sum of n natural numbers
sum=0
print("Enter the n number:\t")
n=input()
print('the sum of n natural numbers is: \n')
for i in range(n):
    if i==5:
        print("I got no:5")
        continue
    sum += i
    print(sum)
