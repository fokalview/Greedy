# NAME: Mikal Brown
# COURSE: CS5007
# HOMEWIRK: 5 TSP Solver
# DATE: April 15, 2025


# Imports
import pandas as pd # For CSV handling
import mpu # For haversine distance calculation
import random # For random sampling
import os # For file and folder operations
from typing import List # Type hinting because we’re classy
import matplotlib.pyplot as plt # Plotting our adventure
from datetime import datetime # For time-stamping our travel log

# This City class holds info about each city used through the program.
class City:
    def __init__(self, name: str, state_name: str, county_name: str, lat: float, lng: float, population: int, military: bool, timezone: str):
        self.name = name
        self.state_name = state_name
        self.county_name = county_name
        self.lat = lat
        self.lng = lng
        self.population = population
        self.military = military
        self.timezone = timezone

    # Calculate distance between this city (n) and City (m).
    def distance_to(self, other_city) -> float:
        return mpu.haversine_distance(
            (self.lat, self.lng),
            (other_city.lat, other_city.lng)
        )

class Tour:#   stores the tour of cities
    def __init__(self, cities: List[City]):
        self.cities = cities

    def total_distance(self) -> float: # Total distance we travel around the loop.
        total = 0.0
        for i in range(len(self.cities)):
            total += self.cities[i].distance_to(self.cities[(i + 1) % len(self.cities)])
        return total

# The brains: finds a quick (not best) tour by being greedy.
class TSPSolver:
    @staticmethod
    def greedy_solver(cities: List[City]) -> Tour:
        if not cities:
            return Tour([])

        unvisited = cities.copy()
        tour = [unvisited.pop(0)] #start at the topof the cities list

        while unvisited:
            last = tour[-1] #calls last visited city
            nearest = min(unvisited, key=lambda city: last.distance_to(city)) #finds the closest city 
            tour.append(nearest) #adds a close city
            unvisited.remove(nearest) #removes the added city (nearest)
        return Tour(tour)

# Optional visualization trip plotted out.
def visualize_tour(tour: Tour):
    plt.figure(figsize=(10, 6)) #sets up the cartesaian plane
    # Travel plot made up of red dots
    lats = [city.lat for city in tour.cities]
    lngs = [city.lng for city in tour.cities]
    plt.scatter(lngs, lats, c='red')
    
    # Plotting the path 
    path = tour.cities + [tour.cities[0]]
    path_lngs = [city.lng for city in path]
    path_lats = [city.lat for city in path]
    plt.plot(path_lngs, path_lats, 'b-')

    for city in tour.cities: # A for loop to pull names from the CSV
        plt.annotate(city.name, (city.lng, city.lat))
    # plot title and labels
    plt.title(f"TSP Tour - Total Distance: {tour.total_distance():.2f} km")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.show()

# Save road trip into a text file.
def save_travel_log(tour: Tour, total_distance: float, seed: str):
    os.makedirs("travel_log", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    log_path = f"travel_log/travel_log_{seed or 'random'}.txt"

    visit_counts = {}
    # Using "a" mode here so we can append new trips to the travel_log.txt file.
    # (If you want to reset the travel log every run, change "a" to "w" here.)
    with open(log_path, "a", encoding='utf-8') as log_file: #travel log
        log_file.write("Travel Log – TSP Tour\n")
        log_file.write("------------------------\n")
        log_file.write(f"Generated: {timestamp}\n")
        if seed:
            log_file.write(f"Random Seed Used: {seed}\n")
        log_file.write(f"Cities Visited: {len(tour.cities)}\n\n")
        log_file.write("Starting Tour...\n\n")

        for idx, city in enumerate(tour.cities, start=1):
            count = visit_counts.get(city.name, 0)
            visit_counts[city.name] = count + 1

            line = f"{idx}. {city.name}, {city.state_name} (Lat: {city.lat}, Lon: {city.lng})"
            if count > 0:
                line += f" (visited {count + 1} times)"
            if city.military:
                line += " (Military City)"

            log_file.write(line + "\n")
            log_file.write(f"   County: {city.county_name}\n")
            log_file.write(f"   Population: {city.population:,}\n")
            log_file.write(f"   Timezone: {city.timezone}\n\n")

        log_file.write(f"Total Distance: {total_distance:.2f} km\n")
        log_file.write("Tour Completed.\n")

    print(f"\nTravel log saved to {log_path}")

# The main event
def main():
    print("Traveling Salesman Problem Solver")

    try:  #checks to make sure the CSV can load
        df = pd.read_csv("uscities.csv")
    except FileNotFoundError:
        print("Error: uscities.csv file not found.")
        return

    n = int(input("How many cities to visit? "))
    seed = input("Random seed (optional): ")

    if seed:
        random.seed(int(seed))

    # Sample 'n' random cities from the dataset
    sample = df.sample(n)
    cities = [
        City(
            row['city'],
            row['state_name'],
            row['county_name'],
            row['lat'],
            row['lng'],
            int(row['population']) if not pd.isna(row['population']) else 0,
            str(row['military']).upper() == 'TRUE',
            row['timezone']
        ) for _, row in sample.iterrows()
    ]

    # Solve the TSP using greedy approach
    solver = TSPSolver()
    tour = solver.greedy_solver(cities)

    print(f"\nTotal Tour Distance: {tour.total_distance():.2f} km")
    print("Tour Order:")
    for city in tour.cities:
        print(f"- {city.name}")

    # Save the travel log
    save_travel_log(tour, tour.total_distance(), seed)

    # Ask if user wants to visualize
    if input("\nShow tour visualization? (y/n): ").lower() == 'y':
        visualize_tour(tour)

# Launch the adventure!
if __name__ == "__main__":
    main()
