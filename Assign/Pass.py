marks_input = input("Enter marks: ")
marks_list = marks_input.split(',')
result = []
for mark in marks_list:
    mark = int(mark)
    if mark >= 35:
        result.append("Pass")
    else:
        result.append("Fail")
print(', '.join(result))
