#abcd... = an + bn + cn + dn + ...
'''
In case of an Armstrong number of 3 digits, the sum of cubes of each digit is equal to the number itself. For example:

153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.
'''

num = int(input("Enter a number: "))
sum = 0

#find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

#display the result
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

    '''
    153 % 10 = 3
    sum = sum + 3 cube :: 0 = 0 + 9 => sum = 27
    temp = 15

    digit = 15 % 10 = 5
    sum = 27 + 125 = 152
    temp = 1

    digit = 1 % 10 = 1
    sum = 152 + 1
    temp = 0
    





    '''