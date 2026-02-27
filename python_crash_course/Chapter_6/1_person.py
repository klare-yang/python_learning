classmate = {
    'first_name': 'Mingxu',
    'last_name': 'Cui',
    'age': 19,
    'city': 'Dalian',
    }

for key, value in classmate.items():
       print(f"\nKey: {key}")
       print(f"Value: {value}")

for key in classmate.keys():
       print(f"\n{key} is a key.")

for value in classmate.values():
       print(f"\n{value} is a value.")