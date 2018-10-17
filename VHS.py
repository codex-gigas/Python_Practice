new=3.00
old=2.00
a=int(input('enter no of new videos: '))
b=int(input('enter no of old videos: '))
c=int(input('Enter no of nights you wanna keep: '))
total_cost = ((new*a) + (old*b))*c
print('\nWe are giving new videos $3 per night',end=' ')
print('and old videos $2 per night \n')
d=((new*a) + (old*b))
print('So,\n$3 * ' + str(a) + ' + ' + '$2 * ' + str(b) + ' = ' + str(d))
print("\nNo of nights is " + str(c))
print('\nTherefore, ...')
print('Your Total Cost will be $' + str(total_cost))