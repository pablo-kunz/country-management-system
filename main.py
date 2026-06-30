# Main file of the country management system
# Contains the menu and the main program flow


from file_handler import load_countries, save_countries
from management import add_country, search_country, update_country, display_country_list
from filters_sorting import (
    filter_by_continent,
    filter_by_population_range,
    filter_by_area_range,
    sort_countries
)
from statistics import show_statistics


FILE_NAME = "countries.csv"


def show_menu():
    """Displays the main menu options."""
    print("\n===== COUNTRY MANAGEMENT =====")
    print("1. Show all countries")
    print("2. Add country")
    print("3. Update a country's population and area")
    print("4. Search country by name")
    print("5. Filter by continent")
    print("6. Filter by population range")
    print("7. Filter by area range")
    print("8. Sort countries")
    print("9. Show statistics")
    print("10. Save changes to file")
    print("0. Exit")


def main():
    """Main function: loads data, runs the menu and saves changes on exit."""
    countries = load_countries(FILE_NAME)

    while True:
        show_menu()
        option = input("Select an option: ").strip()

        if option == "1":
            display_country_list(countries)
        elif option == "2":
            add_country(countries)
        elif option == "3":
            update_country(countries)
        elif option == "4":
            search_country(countries)
        elif option == "5":
            filter_by_continent(countries)
        elif option == "6":
            filter_by_population_range(countries)
        elif option == "7":
            filter_by_area_range(countries)
        elif option == "8":
            sort_countries(countries)
        elif option == "9":
            show_statistics(countries)
        elif option == "10":
            save_countries(FILE_NAME, countries)
        elif option == "0":
            save_countries(FILE_NAME, countries)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
