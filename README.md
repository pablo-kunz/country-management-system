# Gestión de Datos de Países en Python

Trabajo Práctico Integrador (TPI) — Programación 1
Tecnicatura Universitaria en Programación a Distancia (UTN)

## Integrantes

- Pablo Kunz
- Magali Tron

## Descripción

Aplicación de consola desarrollada en Python que permite gestionar información
de países (nombre, población, superficie y continente), aplicando listas,
diccionarios, funciones, condicionales, ordenamientos y estadísticas básicas.

Los datos se almacenan en un archivo CSV (`paises.csv`), que se carga al
iniciar el programa y se actualiza al guardar los cambios.

## Estructura del proyecto

```
├── main.py            # Punto de entrada: menú principal
├── archivos.py        # Carga y guardado del CSV
├── gestion.py         # Agregar, actualizar y buscar países
├── filtros_orden.py   # Filtros y ordenamientos
├── estadisticas.py    # Cálculo de estadísticas
├── paises.csv         # Dataset base de países
└── README.md
```

## Requisitos

- Python 3.x (no requiere librerías externas)

## Cómo ejecutar

1. Cloná o descargá este repositorio.
2. Asegurate de que todos los archivos estén en la misma carpeta.
3. Ejecutá desde la terminal:

```bash
python3 main.py
```

## Funcionalidades

El programa ofrece un menú con las siguientes opciones:

1. Mostrar todos los países
2. Agregar país (no permite campos vacíos)
3. Actualizar población y superficie de un país
4. Buscar país por nombre (coincidencia parcial o exacta)
5. Filtrar por continente (sin distinguir mayúsculas ni tildes)
6. Filtrar por rango de población
7. Filtrar por rango de superficie
8. Ordenar países por nombre, población o superficie (ascendente/descendente)
9. Mostrar estadísticas (mayor/menor población, promedios, países por continente)
10. Guardar cambios en el archivo CSV
0. Salir (guarda automáticamente antes de cerrar)

## Ejemplo de uso

```
===== GESTIÓN DE PAÍSES =====
1. Mostrar todos los países
2. Agregar país
...
9. Mostrar estadísticas
0. Salir
Seleccione una opción: 9

--- ESTADÍSTICAS ---
País con mayor población: Brasil (213993437 hab.)
País con menor población: Australia (25690000 hab.)
Promedio de población: 99711304.50 hab.
Promedio de superficie: 3454273.00 km²

Cantidad de países por continente:
  América: 2
  Asia: 1
  Europa: 1
  África: 1
  Oceanía: 1
```

## Formato del CSV

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
```

## Documentación

📄 Documento PDF: [PDF_TPI_Programacion.pdf](PDF_TPI_Programacion.pdf)

## Repositorio

https://github.com/pablokunz10/tpi_gestion_paises_python
  
🎥 Video explicativo: 

https://1drv.ms/v/c/cd1ae98356cd39a2/IQCF03g-nHQ_Q710jXxUhlRhAa8IJzWy8_5_3-UpzObDmuc?e=FwtJDT


Programación 1 — Tecnicatura Universitaria en Programación a Distancia (UTN)
