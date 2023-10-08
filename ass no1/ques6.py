num_list = [12, 55, 42, 67, 89, 34, 56, 36]

count = 0

for index, num in enumerate(num_list):
    if num == 36:
        print("Number found at position:", index)
        count += 1 
    else:
        print("Number not found at position:", index)

print("Total occurrences of 36:", count)