current_users = ['admin', 'bob', 'jackson','John','Mike','Dustin']
new_users = ['Alice','ada','lovelace','mike','Dustin']

for name in new_users:
    if any(name.lower() == u.lower() for u in new_users):
        print(f"The username {name} is available.")
    else:
        print(f"The username {name} has been used.")