# Enter your code here. Read input from STDIN. Print output to STDOUT
x = input().split()
y = int(input())

x.sort(reverse=True)

if y > len(x):
    print("Maaf negara terlalu kuat")
elif y < len(x):
    print(x[y])
else:
    print('Semua sudah terjajah')

