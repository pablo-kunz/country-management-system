# Country Data Management System 🌍

**Integrative Final Project (TPI) — Programming 1**
Universidad Tecnológica Nacional (UTN) — Programming Technician Degree

**Developed by:** Pablo Kunz & Magali Tron

---

## Description

Console-based application built in Python for managing country data (name, population, area, and continent). The system applies core programming concepts including lists, dictionaries, functions, conditionals, sorting algorithms, and basic statistics.

Data is stored in a CSV file (`paises.csv`), which is loaded at startup and updated when changes are saved.

---

## Project Structure
├── main.py            # Entry point: main menu and program flow

├── archivos.py        # CSV reading and writing

├── gestion.py         # Add, update, and search countries

├── filtros_orden.py   # Filtering and sorting logic

├── estadisticas.py    # Statistics calculations

├── paises.csv         # Base country dataset

└── README.md

## Requirements

- Python 3.x (no external libraries required)

---

## How to Run

1. Clone or download this repository.
2. Make sure all files are in the same folder.
3. Run from the terminal:

```bash
python3 main.py
```

---

## Features

1. Display all countries
2. Add a new country (empty fields not allowed)
3. Update population and area of a country
4. Search country by name (partial or exact match)
5. Filter by continent (case-insensitive, accent-insensitive)
6. Filter by population range
7. Filter by area range
8. Sort countries by name, population, or area (ascending/descending)
9. Show statistics (highest/lowest population, averages, countries per continent)
10. Save changes to CSV file
11. Exit (auto-saves before closing)

---

## Example Output

===== COUNTRY MANAGEMENT =====

Show all countries
Add country

...
Show statistics
Exit

Select an option: 9

--- STATISTICS ---

Country with highest population: Brazil (213,993,437 inhabitants)

Country with lowest population: Australia (25,690,000 inhabitants)

Average population: 99,711,304.50 inhabitants

Average area: 3,454,273.00 km²
Countries per continent:

Americas: 2

Asia: 1

Europe: 1

Africa: 1

Oceania: 1

---

## CSV Format

nombre,poblacion,superficie,continente

Argentina,45376763,2780400,América

Japan,125800000,377975,Asia

---

## Documentation

📄 [Full project documentation (PDF)](Documentacion_TPI_Programacion1.pdf)

