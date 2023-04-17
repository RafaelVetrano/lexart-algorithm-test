# Get an array containing just the letters

array = ["a", 10, "b", "hola", 122, 15]

letters_array = []

for element in array:
    if isinstance(element, str):
        letters_array.append(element)

print("Array with only letters:", letters_array)
