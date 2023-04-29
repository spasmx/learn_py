def get_city_country(city: str, country: str, population: int = None) -> str:
    if population:
        return f'{city.title()}, {country.title()}=population {population}'
    return f'{city.title()}, {country.title()}'

