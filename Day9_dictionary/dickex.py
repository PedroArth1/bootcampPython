country = input("country: ") # Add country name
visits = int(input("visits: "))
list_of_cities = eval(input("list of cities: "))

travel_log = [
    {
        "country":"France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

def add_new_country(country, visits, list_of_cities):
    new_country = {
        "country": country,
        "visits": visits,
        "cities": list_of_cities
    }
    travel_log.append(new_country)



add_new_country(country, visits, list_of_cities)
print(f"i've been to {travel_log[2]['country']} {travel_log[2]['visits']}")
print(f"My favourite city was {travel_log[2]['cities'][0]}")