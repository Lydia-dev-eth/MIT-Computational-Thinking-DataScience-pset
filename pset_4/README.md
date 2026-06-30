# Simulating the Spread of Disease and Bacteria Population

A Python implementation of **Problem Set 4** from **MIT 6.0002 – Introduction to Computational Thinking and Data Science**. This project uses stochastic simulations to model bacterial population dynamics, investigate the effects of antibiotic treatment, and analyze the emergence of antibiotic-resistant bacteria over time.

The project applies object-oriented programming, probabilistic modeling, statistical analysis, and data visualization to simulate realistic biological behavior across multiple independent trials.

---

## Features

### Simple Bacteria Simulation

* Models bacterial birth and death using probabilistic events.
* Simulates population growth under a maximum carrying capacity.
* Updates the bacterial population over discrete timesteps.

### Antibiotic Resistance

* Extends the simulation to support antibiotic-resistant bacteria.
* Models mutation of non-resistant bacteria during reproduction.
* Simulates antibiotic treatment and its effect on bacterial survival.
* Tracks both the total bacterial population and the resistant bacterial population.

### Statistical Analysis

Implements statistical functions to analyze simulation results across multiple trials, including:

* Average population
* Standard deviation
* Standard error of the mean (SEM)
* 95% confidence interval

### Data Visualization

Generates plots using Matplotlib to visualize:

* Average bacterial population over time
* Total population vs. resistant population after antibiotic treatment

---

## Implemented Classes

### `SimpleBacteria`

Represents a single bacterium capable of:

* Random death
* Population-density-dependent reproduction

---

### `Patient`

Maintains a collection of bacteria and updates the population by:

1. Determining surviving bacteria
2. Computing population density
3. Reproducing surviving bacteria
4. Updating the bacterial population

---

### `ResistantBacteria`

Extends `SimpleBacteria` by introducing:

* Antibiotic resistance
* Mutation probability
* Resistance inheritance during reproduction

---

### `TreatedPatient`

Extends `Patient` to model antibiotic treatment.

Additional functionality includes:

* Administering antibiotics
* Eliminating non-resistant bacteria after treatment
* Tracking resistant bacterial populations

---

## Implemented Functions

### Statistical Functions

* `calc_pop_avg()`
* `calc_pop_std()`
* `calc_95_ci()`

These functions compute summary statistics from multiple simulation trials.

---

### Simulation Functions

#### `simulation_without_antibiotic()`

Runs multiple simulations of bacterial population growth without antibiotic treatment and plots the average population over time.

#### `simulation_with_antibiotic()`

Runs multiple simulations where an antibiotic is introduced after a specified number of timesteps. The simulation tracks both:

* Total bacterial population
* Resistant bacterial population

The average results from all trials are displayed on a two-curve plot.

---

## Project Structure

```text
.
├── ps4.py              # Main implementation
├── ps4_tests.py        # Unit tests
├── README.md
```

---

## Requirements

* Python 3.10+
* matplotlib

Install the required dependency:

```bash
pip install matplotlib
```

---

## Running the Project

Run the simulation:

```bash
python ps4.py
```

Run the test suite:

```bash
python ps4_tests.py
```

---

## Python 3.14 Compatibility

The original MIT test suite was written using the deprecated:

```python
unittest.makeSuite()
```

Since this API was removed in Python 3.13+, the test suite was updated for compatibility by replacing it with:

```python
unittest.defaultTestLoader.loadTestsFromTestCase()
```

This preserves the original behavior while allowing the project to run successfully on modern Python versions.

---

## Simulation Workflow

For each simulation timestep, the bacterial population is updated using the following sequence:

1. Determine which bacteria survive.
2. Remove non-resistant bacteria if antibiotics have been administered.
3. Compute the current population density.
4. Allow surviving bacteria to reproduce probabilistically.
5. Update the patient's bacterial population.
6. Record population statistics.

Multiple independent trials are performed to reduce the effects of randomness and produce statistically meaningful averages.

---

## Technologies Used

* Python
* Matplotlib
* Object-Oriented Programming
* Monte Carlo Simulation
* Probability and Statistics

---

## References

* MIT 6.0002 – *Introduction to Computational Thinking and Data Science*
* Problem Set 4 – *Simulating the Spread of Disease and Bacteria Population*

---

## Acknowledgements

This project was completed as part of **MIT 6.0002 – Introduction to Computational Thinking and Data Science**. The implementation follows the original assignment specification while including minor updates for compatibility with modern Python releases.
