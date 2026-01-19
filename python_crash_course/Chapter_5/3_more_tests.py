car = 'bwm'
cars = ['BWM', 'audi', 'toyota', 'subaru']

print(car != 'audi')
print('bwm' in [c.lower() for c in cars])
print('ducati' not in cars)

print(car == 'audi')
print('bwm' not in [c.lower() for c in cars])
print('subaru' not in cars)