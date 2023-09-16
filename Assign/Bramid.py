x=int(input ("Enter a digit:"))
for i in range(x):
    for j in range(x-i-1):
        print(" ", end="")
    for j in range(i+1):
        print(chr(ord('A')+j), end="")
    for j in range(i,0,-1):
        print(chr(ord('A')+j-1), end="")
    print()
