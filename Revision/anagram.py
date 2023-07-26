x = sorted(input("Enter the second string: ").replace(" ", "").lower())
y = sorted(input("Enter the second string: ").replace(" ", "").lower())
if x == y:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
