# Enter your code here. Read input from STDIN. Print output to STDOUT
num = input().split()
d = int(num[0])
t = int(num[1])
p = int(num[2])

panjang_cat1 = 3.14 * d * t * p
panjang_cat2 = 22/7 * d * t * p

if d % 7 == 0:
    print(panjang_cat2)
else:
    print(panjang_cat1)