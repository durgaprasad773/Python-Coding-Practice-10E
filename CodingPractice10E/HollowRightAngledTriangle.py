n=int(input())
for i in range(n):
    if i ==0:
        print("* ")
    elif i==(n-1):
        print("* " * n)
    else:
        hollow = "  " * (i-1)
        row = "* " + hollow +"*"
        print(row)