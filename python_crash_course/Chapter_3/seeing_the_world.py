places = ['paris', 'newyork', 'shanghai', 'london', 'berlin']

print("\nOriginal:")
print(places)

print("\nSorted:")
print(sorted(places))

print("\nStill original:")
print(f"{places}\n")

print("\nIn the reverse-alphabetical sort:")
print(f"{sorted(places, reverse = 1)}\n")

print("\nStill original:")
print(f"{places}\n")

places.reverse()
print("\nSort in the reverse order:")
print(f"{places}\n")

places.reverse()
print("\nBack to the original order:") # sort 表 结果/行为， order 表 状态
print(f"{places}\n")

places.sort()
print("\nSort alphabetical permannetly:")
print(f"{places}\n")

places.sort(reverse = 1)
print("\nSort in the reverse-alphabetical sort permanently:")
print(f"{places}\n")