#python program to swap two variables

x = 5
y = 10

temp = x 
x = y
y = temp

print('The Value of X after swapping: {}'.format(x))
print('The Value of y after swapping: {}'.format(y))



a = 54
b = 69

a,b = b,a
print(a)
print(b)