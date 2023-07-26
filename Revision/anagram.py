x = sorted(input("Enter the first string: ").lower())
y= sorted(input("Enter the second string: ").lower())

if len(x) == len(y):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
