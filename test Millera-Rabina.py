import random
print('podaj liczbe do sprawdzenia')
n=int(input())
print('podaj parametr określający prawd. pomyłki')
t=int(input())
r=n-1
s=0
while r%2==0:
    s=s+1
    r=r/2
odp=0
for i in range(t):
    a=random.randrange(2,n-1)
    y=pow(a,r,n)
    if (y!=1 & y!=(n-1)):
        j=1
        while (j<=s-1 and y!=n-1):
            y=pow(y,2,n)
            if y==1:
                odp=odp+1
            j=j+1
        if y!=n-1:
            odp=odp+1

if odp==0:
    print('n jest liczbą pierwszą')
else:
    print('n jest liczbą złożoną')