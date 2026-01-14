list = ['a', 'b', 'c', 'd', 'e']
print(f"The guest list is {list}")

wont_come_1 = list.pop(1)
wont_come_2 = list.pop(3)

print(f"{wont_come_1.title()} and {wont_come_2} won't come to our party."
      f"So our new guest list is {list}.")

new_guest_1 = 'f'
new_guest_2 = 'g'
list.append(new_guest_1)
list.append(new_guest_2)

print(f"Luckily,here come the new guests {new_guest_1} and {new_guest_2}."
      f"So the new guest list is {list}.")