# Module responsible for basic country management: add, update and search

def add_country(countries):
    """
    Asks the user for the data of a new country and adds it to the list.
    Empty fields are not allowed.
    """
    name = input("Country name: ").strip()
    while name == "":
        print("Name cannot be empty.")
        name = input("Country name: ").strip()

    population = ask_for_integer("Population: ")
    area = ask_for_integer("Area (km²): ")

    continent = input("Continent: ").strip()
    while continent == "":
        print("Continent cannot be empty.")
        continent = input("Continent: ").strip()

    new_country = {
        "name": name,
        "population": population,
        "area": area,
        "continent": continent
    }

    countries.append(new_country)
    print(f"Country '{name}' added successfully.")


def ask_for_integer(message):
    """
    Asks the user for an integer, validating that it is correct and >= 0.
    """
    while True:
        value = input(message).strip()
        try:
            number = int(value)
            if number < 0:
                print("Value cannot be negative.")
                continue
            return number
        except ValueError:
            print("Please enter a valid integer.")


def search_country(countries):
    """
    Searches countries by name, allowing partial or exact matches.
    Displays the results found.
    """
    if not countries:
        print("No countries loaded.")
        return

    text = input("Enter the name (or part of the name) to search: ").strip().lower()

    found = [c for c in countries if text in c["name"].lower()]

    if not found:
        print("No countries matched the search.")
        return

    print(f"\nFound {len(found)} countr(y/ies):")
    for country in found:
        display_country(country)


def update_country(countries):
    """
    Allows updating the population and/or area of a country, searched by exact name.
    """
    if not countries:
        print("No countries loaded.")
        return

    name = input("Enter the exact name of the country to update: ").strip()

    found_country = None
    for c in countries:
        if c["name"].lower() == name.lower():
            found_country = c
            break

    if found_country is None:
        print("No country found with that name.")
        return

    print("Current data:")
    display_country(found_country)

    new_population = ask_for_integer("New population: ")
    new_area = ask_for_integer("New area (km²): ")

    found_country["population"] = new_population
    found_country["area"] = new_area

    print("Data updated successfully.")


def display_country(country):
    """
    Displays a country's data in a readable format.
    """
    print(f"- {country['name']} | Population: {country['population']} | "
          f"Area: {country['area']} km² | Continent: {country['continent']}")


def display_country_list(countries):
    """
    Displays all countries in the list.
    """
    if not countries:
        print("No countries loaded.")
        return

    for country in countries:
        display_country(country)
