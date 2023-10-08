num_list = [12, 55, 42, 67, 89, 34, 45, 36]


count = 0


for index, num in enumerate(num_list):
    if num == 36:
        count += 1  


print("Total occurrences of 36:", count)