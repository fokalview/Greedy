Homework 5 – Traveling Salesman Problem Solver (TSP)
Author: Mikal Brown
Course: CS5007 – Systems Programming
Date: April 15, 2025


DESCRIPTION:

This program solves a basic version of the Traveling Salesman Problem (TSP) using a greedy nearest-neighbor algorithm.
It randomly selects 'n' cities from a dataset (uscities.csv) and computes a tour that visits each city once and returns to the starting city.
Includes a visual tour plot using matplotlib.


FEATURES:

Reads data from a CSV File
Allows for Tour Cities and Seed to be controlled by the user
Greedy (nearest-neighbor) algorithm
Optional:
   Visualization of the tour path using matplotlib
   Travel Log Saves the trip details to a text file
        Handles military cities and timezone info

FILES INCLUDED:

homework5_tsp.py: main script
uscities.csv: dataset with U.S. city names and coordinates
README.txt: current file

REQUIRED LIBARIES: 
pandas : For CSV handling
mpu: For haversine distance calculation
matplotlib: plots the adventure

INSTALLATION:
Quicky install libraries form terminal: 
	pip install pandas mpu matplotlib
If needed you could also install a virtual python environment
   Windows:
       python -m venv venv
       .\venv\Scripts\activate


HOW TO RUN:
Make sure uscities.csv and homework5_tsp.py are in the same folder.
Run the program:
    homework5_tsp.py
When prompted:
    Enter number of cities to visit (e.g., 5)
    Enter a random seed (optional) for more consistent results on reruns
    Type 'y' to visualize the route
    Type 'n' to skip visualization
Check the travel_log folder for a text file with your trip details.


SAMPLE OUTPUT:
Travel Log – TSP Tour
------------------------
Generated: 2025-04-26 17:15
Cities Visited: 3

Starting Tour...

1. Thendara, New York (Lat: 43.701, Lon: -74.9971)
   County: Herkimer
   Population: 64
   Timezone: America/New_York

2. Sullivan, Illinois (Lat: 39.5951, Lon: -88.6084)
   County: Moultrie
   Population: 4,532
   Timezone: America/Chicago

3. Glasgow Village, Missouri (Lat: 38.7578, Lon: -90.1984)
   County: St. Louis
   Population: 5,036
   Timezone: America/Chicago

NOTES:
 The tour is not optimal; it’s a greedy approximation.

WAYS I CAN IMPROVE THE CODE:

Add more commands for flexibility (e.g., number of cities, exclude military cities)
Include more cities in the dataset for a larger sample size
Add a GUI

QUESTIONS?
Email: mhbrown@wpi.edu

