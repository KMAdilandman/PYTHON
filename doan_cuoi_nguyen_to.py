from math import sqrt
def prime(n):
    if n<2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
for _ in range(int(input())):
    s=input()
    l=len(s)
    sum=int(s[l-4])*1000+int(s[l-3])*100+int(s[l-2])*10+int(s[l-1])
    print("YES" if prime(sum) else "NO")