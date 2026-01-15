a_list = []
for num in range(1,30,3):
    a_list.append(num)

print("\nThe first three numbers in a_list are:")
slice_list = a_list[:3]
for slice in slice_list:
    print(slice)

print("\nThree numbers from the middle of a_list are:")
slice_list = a_list[3:6]
for slice in slice_list:
    print(slice)

print("\nThe last three numbers in a_list are:")
slice_list = a_list[-3:]
for slice in slice_list:
    print(slice)