travel_log = [
    {
        "country": "France",
        "Visits": 12,
        "Cities": ["paris", "Lille", "Dijon"]
    },
{
        "country": "Germany",
        "Visits": 5,
        "Cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country, visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["Visits"] = visits
    new_country["Cities"] = cities
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)