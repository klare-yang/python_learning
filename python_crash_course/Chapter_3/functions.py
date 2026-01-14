motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print (motorcycles)

motorcycles.insert(1,'bwm')
print(motorcycles)

del motorcycles[2]
print(motorcycles)

popped_motorcycle = motorcycles.pop(0)
print(motorcycles)
print(popped_motorcycle.title())

expensive_motor = 'bwm'
motorcycles.remove(expensive_motor)
print(f"The {expensive_motor} is too expensive for me.")

# ---

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.sort()
print(cars)

cars.sort(reverse = 1)
print(cars)