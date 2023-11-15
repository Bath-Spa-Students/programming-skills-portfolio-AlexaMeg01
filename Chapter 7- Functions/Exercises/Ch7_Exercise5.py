def describe_city(city, country='Philippinese'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('Manila')
describe_city('iloilo city', 'bago city')
describe_city('bayawan city')
