:

📌 Directed DFS Path Finder
📖 Overview

This project implements a Directed Depth-First Search (DFS) algorithm to find the shortest path between two nodes under specific constraints, along with a custom-built graph structure.

It is inspired by concepts from MIT’s 6.0002: Introduction to Computational Thinking.

🧱 Project Components
Graph Implementation

The graph is built from scratch using:

Node – represents a building
WeightedEdge – represents a connection with:
total distance
outdoor distance
Digraph – stores nodes and edges using an adjacency list
Path Finding Algorithm
get_best_path – a recursive DFS helper that explores all valid paths
directed_dfs – initializes the search and enforces constraints
🎯 Goal

Find the shortest path from a start node to an end node such that:

Total distance ≤ max_total_dist
Outdoor distance ≤ max_dist_outdoors

If no valid path satisfies these constraints, the function raises a ValueError.

⚙️ How It Works
The algorithm uses DFS with recursion to explore possible paths
At each step, it tracks:
the current path
total distance traveled
outdoor distance traveled
Paths that exceed constraints are pruned early to improve efficiency
Among all valid paths, the algorithm keeps the shortest one
📂 Input Format

The graph is loaded from a file where each line contains:

From To TotalDistance OutdoorDistance

Example:

32 76 54 23

Each line represents a directed edge between two nodes.

🧪 Example Usage
directed_dfs(graph, "32", "56", 100, 0)

Returns the shortest valid path as a list of node names.

💡 Key Concepts
Depth-First Search (DFS)
Recursion and backtracking
Graph data structures
Constraint-based pathfinding
Avoiding shared mutable state in recursion
🚀 Takeaway

This project demonstrates how combining graph structures with DFS and constraint handling can solve complex pathfinding problems efficiently while maintaining clear and structured code.
