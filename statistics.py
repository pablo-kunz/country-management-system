# Module responsible for calculating statistics over the country list


def country_highest_population(countries):
    """Returns the country with the highest population."""
    return max(countries, key=lambda c: c["population"])


def country_lowest_population(countries):
    """Returns the country with the lowest population."""
    return min(countries, key=lambda c: c["population"])


def average_population(countries):
    """Calculates the average population of all countries."""
    total = sum(c["population"] for c in countries)
    return total / len(countries)


def average_area(countries):
    """Calculates the average area of all countries."""
    total = sum(c["area"] for c in countries)
    return total / len(countries)


def count_by_continent(countries):
    """Returns a dictionary with the number of countries per continent."""
    count = {}
    for country in countries:
        continent = country["continent"]
        if continent in count:
            count[continent] += 1
        else:
            count[continent] = 1
    return count


def show_statistics(countries):
    """Calculates and displays all the statistics requested by the project."""
    if not countries:
        print("No countries loaded to calculate statistics.")
        return

    highest = country_highest_population(countries)
    lowest = country_lowest_population(countries)
    avg_pop = average_population(countries)
    avg_area = average_area(countries)
    count = count_by_continent(countries)

    print("\n--- STATISTICS ---")
    print(f"Country with highest population: {highest['name']} ({highest['population']} inhabitants)")
    print(f"Country with lowest population: {lowest['name']} ({lowest['population']} inhabitants)")
    print(f"Average population: {avg_pop:.2f} inhabitants")
    print(f"Average area: {avg_area:.2f} km²")
    print("\nCountries per continent:")
    for continent, amount in count.items():
        print(f"  {continent}: {amount}")
