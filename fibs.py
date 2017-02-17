def isPrime(n):
    t= n;
    p=1
    for i in range(2, t):
        if(t%i==0):
            p=0
    if(p==1):
        print("BuzzFizz")
m = raw_input("num??")
n= int(m)
num1 = 1
num2 = 1
count=0
while (count <n):
    count=count+1
    if(n%2==0):
        num1 = num1+num2
        num =num1
    else:
        num2 =num1+num2
        num=num2
    n=n+1
print(num)
if(num%3==0):
    print("Buzz ")
if(num%5==0):
    print("Fizz ")
if(num%15==0):
    print("FizzBuzz ")
isPrime(num)
