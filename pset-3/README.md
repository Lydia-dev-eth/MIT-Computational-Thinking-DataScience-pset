 # MIT 6.0002 – Introduction to Computational Thinking and Data Science  
## Problem Set 3: Robot Room Cleaning Simulation

---

# Description

This project is part of **MIT 6.0002: Introduction to Computational Thinking and Data Science**.

The program simulates autonomous robots cleaning a rectangular room using different movement strategies. It analyzes robot efficiency, compares cleaning algorithms, and visualizes how room shape and robot behavior impact overall cleaning performance.

The simulation uses object-oriented programming, randomized movement, and repeated experimental trials to evaluate cleaning efficiency statistically.

---

# Problem Statement

The objective of this problem set is to model and simulate robotic cleaning behavior in a 2D environment.

The system must:
- Represent rooms divided into tiles containing dirt
- Simulate robots moving around the room
- Allow robots to clean tiles over time
- Support different robot movement strategies
- Compare the efficiency of different robot behaviors
- Analyze cleaning performance under various room configurations

The simulation measures how many time-steps are required to clean a target percentage of the room.

---

# Included Files

| File Name | Description |
|---|---|
| `ps3.py` | Main implementation file containing the room, robot, and simulation logic |
| `ps3_visualize.py` | Visualization module used to animate robot movement and room cleaning |
| `ps3_verify_movement27.py` | Verification and testing utilities for robot movement behavior |
| `README.md` | Project documentation and usage instructions |
| `MIT6_0002F16_ProblemSet3` | Official MIT Problem Set 3 instructions and assignment specification document |

---

# Solution Overview

The solution uses a simulation-based approach built with object-oriented programming principles.

## Main Components

### `Position`
Represents a location in the room using floating-point coordinates.

### `RectangularRoom`
Tracks dirt levels and room boundaries.

### `EmptyRoom`
A room without obstacles.

### `FurnishedRoom`
A room containing furniture tiles that robots cannot enter.

### `Robot`
Base robot class defining shared robot behavior.

### `StandardRobot`
Moves in its current direction and changes direction upon collision.

### `FaultyRobot`
Behaves like a standard robot but may randomly fail to clean tiles.

### `run_simulation()`
Runs multiple trials and calculates the average cleaning time.

---

# Key Features

- Object-oriented simulation design
- Randomized robot movement
- Empty and furnished room support
- Faulty robot behavior simulation
- Statistical performance analysis
- Cleaning efficiency comparison
- Graph plotting and visualization
- Configurable simulation parameters

---

# Tech Stack

## Language
- Python

## Libraries
- `math`
- `random`
- `pylab`

## Concepts
- Object-Oriented Programming
- Simulation Modeling
- Probability and Randomness
- Performance Analysis
- Data Visualization

---

# Getting Started

## Prerequisites

Install Python and required dependencies:

```bash
pip install matplotlib
```

---

# Running the Project

Execute the simulation:

```bash
python ps3.py
```

---

# Example Usage

```python
run_simulation(
    num_robots=3,
    speed=1.0,
    capacity=1,
    width=20,
    height=20,
    dirt_amount=3,
    min_coverage=0.8,
    num_trials=50,
    robot_type=StandardRobot
)
```

---

# Visualization

The project includes graphing utilities for performance analysis.

## Compare Robot Strategies

```python
show_plot_compare_strategies(
    'Robot Strategy Comparison',
    'Number of Robots',
    'Time / Steps'
)
```

## Analyze Room Shape Performance

```python
show_plot_room_shape(
    'Room Shape Performance',
    'Aspect Ratio',
    'Time / Steps'
)
```

---

# Concepts Demonstrated

- Simulation-based experimentation
- Monte Carlo-style repeated trials
- Inheritance and polymorphism
- Abstract class design
- Statistical analysis
- Algorithmic modeling

---

# Future Improvements

Potential future enhancements include:

- Smarter robot navigation
- Pathfinding algorithms
- Multi-room environments
- Dynamic obstacles
- Real-time animation improvements
- AI-driven cleaning strategies
- Parallel robot communication

---

# License

This project is intended for educational and academic purposes.
---

# Description

This project is part of **MIT 6.0002: Introduction to Computational Thinking and Data Science**.

The program simulates autonomous robots cleaning a rectangular room using different movement strategies. It analyzes robot efficiency, compares cleaning algorithms, and visualizes how room shape and robot behavior impact overall cleaning performance.

The simulation uses object-oriented programming, randomized movement, and repeated experimental trials to evaluate cleaning efficiency statistically.

---

# Problem Statement

The objective of this problem set is to model and simulate robotic cleaning behavior in a 2D environment.

The system must:
- Represent rooms divided into tiles containing dirt
- Simulate robots moving around the room
- Allow robots to clean tiles over time
- Support different robot movement strategies
- Compare the efficiency of different robot behaviors
- Analyze cleaning performance under various room configurations

The simulation measures how many time-steps are required to clean a target percentage of the room.

---

# Included Files

| File Name | Description |
|---|---|
| `ps3.py` | Main implementation file containing the room, robot, and simulation logic |
| `ps3_visualize.py` | Visualization module used to animate robot movement and room cleaning |
| `ps3_verify_movement27.py` | Verification and testing utilities for robot movement behavior |
| `README.md` | Project documentation and usage instructions |

---

# Solution Overview

The solution uses a simulation-based approach built with object-oriented programming principles.

## Main Components

### `Position`
Represents a location in the room using floating-point coordinates.

### `RectangularRoom`
Tracks dirt levels and room boundaries.

### `EmptyRoom`
A room without obstacles.

### `FurnishedRoom`
A room containing furniture tiles that robots cannot enter.

### `Robot`
Base robot class defining shared robot behavior.

### `StandardRobot`
Moves in its current direction and changes direction upon collision.

### `FaultyRobot`
Behaves like a standard robot but may randomly fail to clean tiles.

### `run_simulation()`
Runs multiple trials and calculates the average cleaning time.

---

# Key Features

- Object-oriented simulation design
- Randomized robot movement
- Empty and furnished room support
- Faulty robot behavior simulation
- Statistical performance analysis
- Cleaning efficiency comparison
- Graph plotting and visualization
- Configurable simulation parameters

---

# Tech Stack

## Language
- Python

## Libraries
- `math`
- `random`
- `pylab`

## Concepts
- Object-Oriented Programming
- Simulation Modeling
- Probability and Randomness
- Performance Analysis
- Data Visualization

---

# Getting Started

## Prerequisites

Install Python and required dependencies:

```bash
pip install matplotlib
```

---

# Running the Project

Execute the simulation:

```bash
python ps3.py
```

---

# Example Usage

```python
run_simulation(
    num_robots=3,
    speed=1.0,
    capacity=1,
    width=20,
    height=20,
    dirt_amount=3,
    min_coverage=0.8,
    num_trials=50,
    robot_type=StandardRobot
)
```

---

# Visualization

The project includes graphing utilities for performance analysis.

## Compare Robot Strategies

```python
show_plot_compare_strategies(
    'Robot Strategy Comparison',
    'Number of Robots',
    'Time / Steps'
)
```

## Analyze Room Shape Performance

```python
show_plot_room_shape(
    'Room Shape Performance',
    'Aspect Ratio',
    'Time / Steps'
)
```

---

# Concepts Demonstrated

- Simulation-based experimentation
- Monte Carlo-style repeated trials
- Inheritance and polymorphism
- Abstract class design
- Statistical analysis
- Algorithmic modeling

---

 
