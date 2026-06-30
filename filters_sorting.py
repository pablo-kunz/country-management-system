# Module responsible for filtering and sorting the country list based on different criteria

import unicodedata
from management import display_country, ask_for_integer


def remove_accents(text):
    """
    Removes accents from a text, so comparisons work regardless
    of whether the user types them or not.
    """
    normalized = unicodedata.normalize("NFD", text)
    return "".join(c for c in normalized if unicodedata.category(c) != "Mn")


def filter_by_continent(countries):
    """
    Filters and displays the countries that belong to a given continent.
    Case-insensitive and accent-insensitive.
    """
    if not countries:
        print("No countries loaded.")
        return

    continent = input("Enter the continent to filter by: ").strip().lower()
    continent = remove_accents(continent)

    result = [
        c for c in countries
        if remove_accents(c["continent"].lower()) == continent
    ]

    if not result:
        print("No countries found for that continent.")
        return

    print(f"\nCountries in {continent.capitalize()}:")
    for country in result:
        display_country(country)


def filter_by_population_range(countries):
    """
    Filters and displays the countries whose population is within a given range.
    """
    if not countries:
        print("No countries loaded.")
        return

    minimum = ask_for_integer("Minimum population: ")
    maximum = ask_for_integer("Maximum population: ")

    if minimum > maximum:
        print("Minimum value cannot be greater than maximum.")
        return

    result = [c for c in countries if minimum <= c["population"] <= maximum]

    if not result:
        print("No countries found in that population range.")
        return

    print("\nCountries found:")
    for country in result:
        display_country(country)


def filter_by_area_range(countries):
    """
    Filters and displays the countries whose area is within a given range.
    """
    if not countries:
        print("No countries loaded.")
        return

    minimum = ask_for_integer("Minimum area (km²): ")
    maximum = ask_for_integer("Maximum area (km²): ")

    if minimum > maximum:
        print("Minimum value cannot be greater than maximum.")
        return

    result = [c for c in countries if minimum <= c["area"] <= maximum]

    if not result:
        print("No countries found in that area range.")
        return

    print("\nCountries found:")
    for country in result:
        display_country(country)


def sort_countries(countries):
    """
    Sorts the country list by the criterion chosen by the user:
    name, population or area. Allows ascending or descending order.
    """
    if not countries:
        print("No countries loaded.")
        return

    print("\nSort by:")
    print("1. Name")
    print("2. Population")
    print("3. Area")

    option = input("Select an option: ").strip()

    criteria = {
        "1": "name",
        "2": "population",
        "3": "area"
    }

    if option not in criteria:
        print("Invalid option.")
        return

    order = input("Order (A = ascending, D = descending): ").strip().upper()

    if order not in ("A", "D"):
        print("Invalid order option.")
        return

    key = criteria[option]
    reverse = (order == "D")

    sorted_countries = sorted(countries, key=lambda c: c[key], reverse=reverse)

    print("\nSorted countries:")
    for country in sorted_countries:
        display_country(country)
