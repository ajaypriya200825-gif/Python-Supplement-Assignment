# Problem 10: Remove duplicates from a list
# Find and fix the error

numbers = [2, 3, 3, 4, 5, 5, 6]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print(f"Unique numbers: {unique}")
