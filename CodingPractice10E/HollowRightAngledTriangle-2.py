n=int(input())
print("_" * (n+1))
for i in range(n):
    hollow = " " * (n-i-1)
    row="|" + hollow +"/"
    print(row)