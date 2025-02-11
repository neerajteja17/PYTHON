# PYTHON

Python Repository

# Table of Contents

Graph

Leap Year

Numpy

Pandas

Flight Management Front

Flight Management System

Hello World GUI using Tkinter

# Graph
This module provides functionality to work with graphs, including:

Creation of Graphs: Add nodes and edges.
Traversal Algorithms: Depth First Search (DFS), Breadth First Search (BFS).
Visualization: Basic visualization of graphs using matplotlib.

Example Usage:

from graph_module import Graph

graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_edge("A", "B")
print(graph.traverse_dfs("A"))

# Leap Year
This module includes a function to determine whether a given year is a leap year and the ability to create a range of leap years within a specific period.

Features:

Leap Year Check: Determines if a year is divisible by 4, but not by 100, unless divisible by 400.
Range Generator: Generates all leap years in a specified range.

Example Usage:

from leap_year import is_leap_year, generate_leap_years

print(is_leap_year(2024))  # True
print(generate_leap_years(2000, 2050))

# Numpy
This module demonstrates the use of Numpy, a library for numerical computing in Python.

Features:

Array Operations: Creating, indexing, and performing operations on arrays.
Mathematical Functions: Linear algebra, statistical operations, etc.

Example Usage:

import numpy as np

arr = np.array([1, 2, 3, 4])
print(np.mean(arr))  # 2.5

# Pandas
This module showcases how to use Pandas for data manipulation and analysis.

Features:

DataFrames: Create, read, and modify tabular data.
Data Cleaning: Handle missing values, filtering, and transformation.

Example Usage:

import pandas as pd

data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)
print(df.head())

# Flight Management Front
A front-end interface for the flight management system.

Features:

User Interface: Displays flight schedules and booking options.
Integration: Connects to the flight management backend.
Current State: This module is under development. Updates will be provided soon.

# Flight Management System
A back-end system to manage flights, including scheduling, ticketing, and passenger management.

Features:

Add Flights: Add and manage flight schedules.
Passenger Details: Manage passenger information.

Example Usage:

from flight_management import FlightManager

manager = FlightManager()
manager.add_flight("FL001", "NYC", "LAX", "2025-01-01 10:00")
print(manager.get_flights())

# Hello World GUI using Tkinter
A simple GUI application to display "Hello World!" using the Tkinter library.

Features:

Graphical Interface: Creates a window with a button.
Interactivity: Clicking the button displays a message.
Code Example:

import tkinter as tk

def display_message():
    label.config(text="Hello World!")

root = tk.Tk()
root.title("Hello World GUI")

label = tk.Label(root, text="")
label.pack()

button = tk.Button(root, text="Click Me", command=display_message)
button.pack()

root.mainloop()

# Explanation:

tk.Tk(): Initializes the main window.
Label: Displays text in the window.
Button: Triggers an action when clicked.
mainloop(): Starts the Tkinter event loop to display the GUI.

Feel free to contribute or provide suggestions for improvement!
