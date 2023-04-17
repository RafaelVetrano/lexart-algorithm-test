array = ["a", 10, "b", "hola", 122, 15]

highest_number = None

for element in array:
    if isinstance(element, (int, float)):
        if highest_number is None or element > highest_number:
            highest_number = element

if highest_number is not None:
    print("Highest number in the array:", highest_number)
else:
    print("No numbers found in the array.")
