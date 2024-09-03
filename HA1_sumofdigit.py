n=int(input("Enter a Number"))
s=0
rem = 0 
while n>0 :
    rem = n%10
    s = int(s+rem)
    n = int(n/10)
print(s,"=Sum")
input()
