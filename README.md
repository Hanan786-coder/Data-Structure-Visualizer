# Data Structure & Algorithm Visualizer

> An interactive educational tool for visualizing data structures and sorting algorithms in real-time using **Python** and **Pygame**

**A comprehensive platform for learning fundamental computer science concepts through step-by-step animated demonstrations.**

## Overview

This visualizer is designed to help students, developers, and educators understand how data structures work and how algorithms execute. By providing interactive, real-time visualizations, it transforms abstract concepts into tangible, observable processes—making complex computer science fundamentals accessible and engaging.

## Features

### **Data Structures**
- **Linked Lists**: Singly, Doubly, and Circular implementations
- **Queues**: Standard and Circular queue visualizations
- **Heaps**: Min Heap and Max Heap implementations
- **Stack**: Push, Pop, and Peek operations
- **Binary Tree**: Tree structure visualization and traversals

### **Sorting Algorithms**
- **Bubble Sort**: Visualization of the bubble sort algorithm
- **Selection Sort**: Step-by-step selection sort with ascending/descending modes
- **Insertion Sort**: Insertion sort algorithm animation
- **Merge Sort**: Complete merge sort execution with tree visualization

### **Interactive Controls**
- **Play/Pause**: Control animation speed
- **Step Navigation**: Move forward and backward through algorithm steps
- **Reset**: Restart the visualization anytime
- **Mode Toggle**: Switch between different sorting modes (e.g., ascending/descending)
- **Intuitive UI**: Clean, user-friendly interface with organized menu system

## Requirements

- **Python** 3.13.5 or higher
- **Pygame** 2.6.1

## Installation

1. **Clone or download the project**:
```bash
git clone <https://github.com/Hanan786-coder/Data-Structure-Visualizer>
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install pygame==2.6.1
```

## Running the Application

Execute the main application:
```bash
python main.py
```

The visualizer will launch with an interactive menu. Use the buttons to navigate between different categories and select a data structure or algorithm to visualize.

## Project Structure

```
DSA Project/
│
├── core/
│   ├── Colors.py                         # Color palette & definitions
│   └── button_template.py                # Reusable button component
│
├── visualizations/
│   ├── algorithms/
│   │   ├── bubble_sort_viz.py            # Bubble sort with comparisons
│   │   ├── insertion_sort.py             # Insertion sort implementation
│   │   ├── mergesort.py                  # Merge sort with tree breakdown
│   │   └── SelectionSort.py              # Selection sort with min/max modes
│   │
│   └── data_structures/
│       ├── linked_lists/
│       │   ├── CircularLinkedList.py     # Circular linked list structure
│       │   ├── DoublyLinkedList.py       # Doubly linked list visualization
│       │   └── SinglyLinkedList.py       # Singly linked list with node operations
│       ├── queues/
│       │   ├── circular_queue_viz.py     # Circular queue implementation
│       │   └── queue_viz.py              # Queue (FIFO) operations
│       ├── stack/
│       │   └── stack_viz.py              # Stack (LIFO) operations
│       └── trees_and_heaps/
│           ├── max_heap.py               # Max-heap properties & heapify
│           ├── min_heap.py               # Min-heap properties & heapify
│           └── tree2.py                  # Binary tree structure & traversals
│
├── main.py                               # Application entry point & UI manager
├── requirements.txt                      # Project dependencies
├── ScienceGothic-Regular.ttf             # Custom typography
└── README.md
```

## How to Use

### Getting Started
1. Run `python main.py` to launch the application
2. Select from the main menu: **Data Structures** or **Algorithms**

### Navigating Data Structures
Browse through organized categories:
- **Linked Lists** – Singly, Doubly, and Circular implementations
- **Queues** – Standard and Circular queue operations
- **Heaps** – Min and Max heap visualizations
- **Stack** – Push, Pop, and stack operations
- **Binary Tree** – Tree structures and traversals

Each visualization demonstrates:
- How elements are stored and organized
- Operations performed on the data structure
- Memory relationships and node connections

### Navigating Sorting Algorithms
Select any sorting algorithm to visualize the complete execution:
- Watch each comparison and swap in real-time
- Understand the algorithm's decision-making process
- Compare efficiency across different algorithms

### Playback Controls
Control the visualization with these interactive buttons:

| Button | Function |
|--------|----------|
| **◀ Prev** | Move to previous step |
| **Play/Pause** | Start/stop animation |
| **Next ▶** | Move to next step |
| **Reset** | Restart with new data |
| **← Back/Menu** | Return to previous menu |
| **Mode Toggle** | Switch between sort directions (when available) |

## Technology Stack

| Component | Version/Details |
|-----------|---|
| **Language** | Python 3.13.5 |
| **Graphics Library** | Pygame 2.6.1 |
| **Architecture** | Object-Oriented Design (OOP) |
| **Font** | ScienceGothic-Regular.ttf |

## Learning Outcomes

Master these fundamental concepts through interactive visualization:

**Data Structure Concepts:**
- How linked lists manage memory with node pointers
- Queue operations (FIFO principle) and circular variants
- Heap properties and heapification process
- Stack operations (LIFO principle) and recursion
- Binary tree structure and traversal algorithms

**Algorithm Analysis:**
- Sorting algorithm step-by-step execution flow
- Comparison and swapping operations
- Time complexity differences between algorithms
- Practical efficiency impact on real-world scenarios

## About the Project

This project was created as a collaborative effort to make learning data structures and algorithms more intuitive and engaging through interactive visualization.

## Development Team

The following developers contributed to this project:

| Developer | GitHub Profile |
|-----------|---|
| **Abdul Hanan** | [@Hanan786-coder](https://github.com/Hanan786-coder) |
| **Muhammad Ahmed** | [@MuhammadAhmadgeek](https://github.com/MuhammadAhmadgeek) |
| **Muhammad Muazzam Shafiq** | [@MuazzamShafiq](https://github.com/MuazzamShafiq) |
| **Muhammad Saad Rehman** | [@saadrehman034](https://github.com/saadrehman034) |

---

<div align="center">

**Happy Learning!** 

*Transform abstract concepts into visual experiences and master fundamental computer science principles.*

</div>
