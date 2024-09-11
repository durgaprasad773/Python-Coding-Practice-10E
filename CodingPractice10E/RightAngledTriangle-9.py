n=int(input())
for i in range(1,n+1):
    if i==1:
        print(". " * i)
    elif i == n:
        print(". " * n)
    else:
        zero="0 " * (i-2)
        row=". " + zero + "."
        print(row)