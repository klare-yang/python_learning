rivers = {
    'nile': 'egype',
    'yangtze': 'china',
    'amazon': 'brazil',
    'seine': 'france'
}
for river, country in rivers.items():
    print(f"\nThe {river.title()} river runs in {country.title()}.")