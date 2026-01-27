name_list = ['admin', 'bob', 'jackson']

def check(list):
    if list:
        for name in list:
            if name == 'admin':
                print(f"Hello {name},woould you like to see a status report?")
            else:
                print(f"Hello {name},thank you for logging again.")
    else:
        print("We need to find some user.")

check(name_list)

# for name in name_list:
#     del name_list[0]

# name_list.clear()
# del name_list[0:]

check(name_list)