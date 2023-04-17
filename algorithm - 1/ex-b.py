
array = ["a", 10, "b", "hola", 122, 15]

numbers_array = []

for element in array:
    if isinstance(element, (int, float)):
        numbers_array.append(element)

print("Array with only numbers:", numbers_array)