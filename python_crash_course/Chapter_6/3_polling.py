namelist = ['jake', 'peter', 'john', 'harry', 'jackson', 'jenny']

FavouriteLanguagePolling = {
    'jake': 'c',
    'john': 'python',
    'harry': 'rust',
    'jenny': 'python'
    }

print("\nThe following languages are mentioned:")
for language in set(FavouriteLanguagePolling.values()):
    print(f"{language}")

# for name, language in FavouriteLanguagePolling.items():
#     if name in namelist:
#         print(f"\nHi, {name.title()}!\nThank you for polling!\nYour favourite language is {language.title()}.")
#     else:
#         print(f"\nHi, {name}!\nPlease take a vote.")

for name in namelist:
    if name in FavouriteLanguagePolling:
        print(f"\nHi, {name.title()}!")
        print("Thank you for polling!")
        print(f"Your favourite language is {FavouriteLanguagePolling[name].title()}.")
    else:
        print(f"\nHi, {name.title()}!")
        print("Please take a vote.")
        