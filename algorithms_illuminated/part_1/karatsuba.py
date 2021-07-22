'''
Karatsuba's integer multiplication 
input two n-digits positve integers, where n is a power of 2
output the product of the two integers
'''

x = input('first integer: ')
y = input('second integer: ')
n = len(x)
x = int(x)
y = int(y)

def kara(x,y,n):
    if x//10 == 0:
        return x * y
    else:
        a = x//10**(n//2)
        b = x%10**(n//2)
        c = y//10**(n//2)
        d = y%10**(n//2)
        p = a+b
        q = c+d
        ac = kara(a,c,len(str(a)))
        bd = kara(b,d,len(str(b)))
        pq = kara(p,q,len(str(p)))
        adbc = pq - ac - bd
        return 10**n * ac + 10**(n//2) * adbc + bd

print('result: ' + str(kara(x,y,n)))
        