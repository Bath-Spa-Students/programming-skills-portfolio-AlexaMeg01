spots = {
    'Fox Village': 'Japan',
    'Park Plaza Westminster Bridge London': 'London',
    'Adventureland': 'Canada',
    'Mount Mayon': 'Philippines',
    'Yangtze': 'China',
    }

for vacation, country in spots.items():
    print("The " + vacation.title() + " flows through " + country.title() + ".")

print("\nThe following rivers are included in this data set:")
for vacation in spots.keys():
    print("- " + vacation.title())

print("\nThe following countries are included in this data set:")
for country in spots.values():
    print("- " + country.title())