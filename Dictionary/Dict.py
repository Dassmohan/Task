x = {"name":"Mohandass","age":20,"degree":"BE","dept":"CSE","Clg":"VRS"}
while True:
    print("1. Add key - value pair \n2. Delete key - value pair \n3. Get the value of a key \n4. Update the value in key \n5. Exit")
    choice = int(input("Entre your choice:"))

    if choice == 1:
        key = input("Enter the key:")
        value = int(input("Enter the value:"))
        x[key] = value
        print("key value pair added successfully")
        print(x)
    elif choice == 2:
        key = input("Enter the key to delete:")
        if key in x:
            del x[key]
            print("Key - value pair deleted successfully")
            print(x)
        else:
            print("key not found in the dictionary")
    elif choice == 3:
        key = input("Enter the key to get the value:")
        if key in x:
            value = x[key]
            print("value:",value)
            print(x)
        else:
            print("Key not found in the dictionary")
    elif choice == 4:
        key = input("Enter the key:")
        value =int (input("Enter the value:"))
        x[key] = value
        print("Value updated successfully")
        print(x)
    elif choice == 5:
        print("Exiting the program...")
        break
    else:
        print("Invalid choice please enter a valid number")