lower = int(input("Please enter the lower value: "))
upper = int(input("Please enter the upper vlaue: "))

print(f"Prime numbers between {lower} and {upper} are: ")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range (2,num):
            if (num % i) == 0:
                break
        else:
            print(num)