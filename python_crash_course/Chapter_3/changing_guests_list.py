guest_list = ['a', 'b', 'c', 'd', 'e']
print(f"\nThe guest list is {guest_list}")

wont_come_1 = guest_list.pop(1)
wont_come_2 = guest_list.pop(3)

print(f"{wont_come_1.title()} and {wont_come_2} won't come to our party.\n"
      f"So our new guest list is {guest_list}.\n")

new_guest_1 = 'f'
new_guest_2 = 'g'
guest_list.append(new_guest_1)
guest_list.append(new_guest_2)

print(f"Luckily,here come the new guests {new_guest_1} and {new_guest_2}.\n"
      f"So the new guest list is {guest_list}.\n")

# Demonstrate how to modify a guest list using list methods