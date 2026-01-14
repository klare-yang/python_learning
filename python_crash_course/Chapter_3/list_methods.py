motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(1,'bmw')
print(motorcycles)

del motorcycles[2]
print(motorcycles)

popped_motorcycle = motorcycles.pop(0)
print(motorcycles)
print(popped_motorcycle.title())

expensive_motor = 'bmw'
motorcycles.remove(expensive_motor)
print(f"The {expensive_motor} is too expensive for me.\n")

# ---

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

# sort alphabetically
cars.sort()
print(cars)

# reverse the order
cars.sort(reverse = 1)
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list:")
print(cars)
print(len(cars))