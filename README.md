🧭 Greedy TSP Solver
A lightweight Python program that solves the Traveling Salesman Problem using a greedy nearest-neighbor algorithm. This tool is perfect for understanding basic route optimization and comparing against more advanced TSP solutions.

🚀 Features
Greedy Algorithm: Uses a nearest-neighbor strategy to build a quick and simple route.

Distance Matrix Input: Accepts custom input for easy testing and experimentation.

Route Output: Displays the final path and total travel distance.

Minimal Setup: No external libraries required — just run it with Python.

🛠️ Technologies Used
Python: Main programming language

Built-in Libraries: math, itertools, etc. (depending on your exact implementation)

📂 Project Structure
Copy
Edit
GreedyTSP/
├── greedy_tsp.py
greedy_tsp.py: The main script that reads the distance matrix and returns the computed route using the greedy method.

📸 Example Output
pgsql
Copy
Edit
Start at City 0  
Visit City 3  
Visit City 2  
Visit City 1  
Return to City 0  
Total distance: 142.7
📈 Future Enhancements
CSV/JSON input support

Graphical route visualization

Performance comparison with brute-force and dynamic programming approaches

