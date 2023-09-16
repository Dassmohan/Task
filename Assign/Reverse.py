x = input("Enter a string: ")
y = x.split()
z = [word[::-1] for word in y]
output = ' '.join(z)
print(output)
