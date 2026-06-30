# Module responsible for reading and writing the CSV file containing country data

import csv


def load_countries(file_name):
    """
    Reads the CSV file and returns a list of dictionaries, each representing a country.
    If the file doesn't exist or has formatting errors, returns an empty list.
    """
    countries = []
    try:
        with open(file_name, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    country = {
                        "name": row["nombre"].strip(),
                        "population": int(row["poblacion"]),
                        "area": int(row["superficie"]),
                        "continent": row["continente"].strip()
                    }
                    countries.append(country)
                except (ValueError, KeyError):
                    print(f"Warning: skipped a row with invalid format: {row}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Starting with an empty list.")
    except Exception as e:
        print(f"Unexpected error while reading the file: {e}")

    return countries


def save_countries(file_name, countries):
    """
    Saves the list of countries to the CSV file, overwriting its content.
    """
    try:
        with open(file_name, "w", newline="", encoding="utf-8") as f:
            fields = ["nombre", "poblacion", "superficie", "continente"]
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            for country in countries:
                writer.writerow({
                    "nombre": country["name"],
                    "poblacion": country["population"],
                    "superficie": country["area"],
                    "continente": country["continent"]
                })
        print("Data saved successfully.")
    except Exception as e:
        print(f"Error while saving the file: {e}")
