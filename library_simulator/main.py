"""
Main entry point for the library simulation.

This script initializes the Simulator class and runs the simulation
for a predefined number of days. Designed to be executed directly
from the command line or an IDE to observe library activity over time.
"""

from simulator import Simulator

def main():
    """
    Initializes and runs the simulation for a fixed duration (30 days).
    """
    sim = Simulator()
    sim.run(days=30)

if __name__ == "__main__":
    main()