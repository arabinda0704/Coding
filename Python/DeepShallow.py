import copy

original = [[1, 2, 3], [4, 5, 6]]
shallow_copied = copy.copy(original)
shallow_copied.append("Python")  # Adding a new element

# Modify the nested list
shallow_copied[0][0] = 99

print(original)  # Output: [[99, 2, 3], [4, 5, 6]]
print(shallow_copied)  # Output: [[99, 2, 3], [4, 5, 6], 'Python']

# Fix: Dynamic iteration based on length
for i in range(len(original)):
    print(id(original[i]), id(shallow_copied[i]))  # Prints object IDs

original1 = [[1, 2, 3], [4, 5, 6]]
deep_copied = copy.deepcopy(original1)

# Modify the nested list
deep_copied[0][0] = 99

print(original1)  # Output: [[1, 2, 3], [4, 5, 6]]
print(deep_copied)  # Output: [[99, 2, 3], [4, 5, 6]]

# Fix: Dynamic iteration based on length
for i in range(len(original1)):
    print(id(original1[i]), id(deep_copied[i]))  # Prints object IDs
