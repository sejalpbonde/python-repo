'''
num = int(input("Enter a positive number: "))
if num < 0:
    print("Enter a positive number")
else: 
    sum = 0
    while (num > 0):
        sum = sum + num
        num = num - 1
    print("The sum is", sum)
'''


n = int(input("Enter a number: "))
sum = (n*(n+1))/2
print(int(sum))