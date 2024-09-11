n=int(input())
for i in range(n):
    if i==0 or i==(n-1):
        print("* " * n)
    else:
        row = "* " + ("0 " * (n-2)) + "*"
        print(row)