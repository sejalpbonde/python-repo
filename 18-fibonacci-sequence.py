#program to display the fibonacci sequence up to the n-th term
''''
nterms = int(input("Enter the number"))

#first two terms
n1, n2 = 0,1
count = 0
#check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive number")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)

else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
'''

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
    
nterms = 10
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))
        

