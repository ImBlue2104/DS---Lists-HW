import math
list = [4,36, 12,11,7, 18]

print("All elements in list squared:")
for element in list:
    sqr = math.pow(element, 2)
    print(sqr)


print("\nAll elements in list sorted based on odd and even: ")
even = []
odd =[]
for element in list:
    if element % 2 == 0:
        even.append(element)
    else:
        odd.append(element)
print("All even nums:", even)
print("All odd nums:", odd)