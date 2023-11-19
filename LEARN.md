# BIM Pathfinding with Graph Algorithms

Welcome! This repository contains a Python implementation of a 2D Building Information Modeling (BIM) pathfinding tool using graph algorithms. If you're already familiar with Python and want to make modifications to the code, you're in the right place.

## Features

### MatrixGUI Class

The `MatrixGUI` class serves as the main interface for the BIM tool. Key features include:

- **Graphical Representation:** The building layout is displayed as a matrix of colored squares on a canvas.
- **Color-Coded Elements:** Different colors represent distinct elements within the building (e.g., walls, paths, start, and end points).
- **User Interaction:** Click on squares to modify their color, allowing for easy editing of the building layout.
- **Get Matrix Button:** Retrieve the matrix representation of the building, incorporating any user modifications.
- **Delete Path Button:** Clear the pathfinding results by removing any designated paths in the matrix.
- **Start and End Points:** Red and green squares mark the start and end points for pathfinding.

### Graph Class

The `Graph` class implements a basic graph data structure with functionalities for adding nodes, edges, and finding the shortest path using Dijkstra's algorithm. This class is utilized in the pathfinding process.

### Pathfinding Algorithm

The pathfinding algorithm is based on Dijkstra's algorithm, implemented in the `Graph` class. It calculates the shortest path between the designated start and end points on the matrix.

### Image Conversion Functions

Utility functions are provided to convert between the matrix representation and image files. The `matrix_to_bmp` function converts a matrix to a .bmp image, and `rgb_image_to_list` converts an image file back to a categorized pixel list.
