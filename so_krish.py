def check(n):
    if n==0 or n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 6
    if n==4:
        return 24
    if n==5:
        return 120 
    if n==6:
        return 720
    if n==7:
        return 5040
    if n==8:
        return 40320
    if n==9:
        return 362880

for _ in range(int(input())):
    n=int(input())
    nn=n
    sum=0
    while n>0:
        sum+=check(n%10)
        n//=10
    print("Yes" if sum==nn else "No")