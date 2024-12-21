different_elements: list = [27, "moiz", 6, "Rehman", "94"]

def get_list_number(list: list, index: int):
    try:
        return list[index]
    except IndexError:
        return 'list index out of range'

def update_list_number(list: list, index: int, next_value):
    try:
        list[index] = next_value
        return list
    except:
        return 'list index out of range'

def copy_list(list: list, start_index: int, end_index: int):
    try:
        return list[start_index:end_index]
    except Exception as e:
        return e

print("Current list:", different_elements)
print("Choose an operation: access, modify, slice")
operation = input("Enter operation: ")

if operation == "access":
    index = int(input("Enter index to access: "))
    print(get_list_number(different_elements, index))
elif operation == "modify":
    index = int(input("Enter index to modify: "))
    new_value = input("Enter new value: ")
    print(update_list_number(different_elements, index, new_value))
elif operation == "slice":
    start = int(input("Enter start index: "))
    end = int(input("Enter end index: "))
    print(copy_list(different_elements, start, end))
else:
    print("Invalid operation.")