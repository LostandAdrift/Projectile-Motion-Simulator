import functions as f
import matplotlib.pyplot as plt
import numpy as np

class Projectile:
    """Class to represent an object in projectile motion."""

    def __init__(self, initial_velocity, initial_height, initial_angle):
        self.initial_velocity = initial_velocity
        self.initial_height = initial_height
        self.initial_angle = initial_angle

        # Calls various functions in functions.py to caclulate different properties.
        # To see these values when called, add them to show_metrics.    
        self.horizontal_velocity = f.find_initial_horizontal_velocity(initial_velocity, initial_angle)
        self.vertical_velocity = f.find_intial_vertical_velocity(initial_velocity, initial_angle)
        self.time_to_max_height = f.find_time_to_max_height(self.vertical_velocity)
        self.max_height = f.find_max_height(self.time_to_max_height, self.vertical_velocity, self.initial_height, self.initial_angle)
        self.total_flight_time = f.find_total_flight_time(self.time_to_max_height, self.max_height)
        self.range = f.find_range(self.horizontal_velocity, self.total_flight_time, self.initial_angle)
        self.impact_velocity = f.find_impact_velocity(self.horizontal_velocity, self.max_height)
    
        # Print out metrics for user
        self.show_metrics()

        # Return plot  of height vs time.
        self.plot_flight_path()

    def plot_flight_path(self):
        """Returns a plot of the projectile's flight."""
        x_coord = np.linspace(0, self.total_flight_time, num=25)
        y_coord = (self.vertical_velocity * x_coord) - (.5 * 9.81 *(x_coord**2)) + self.initial_height
        fig, ax = plt.subplots()
        ax.set_title("Projectile Height VS Time")
        ax.set_xlabel("Time (seconds)")
        ax.set_ylabel("Height (meters)")
        ax.plot(x_coord, y_coord)
        plt.show()
    
    def show_metrics(self):
        """Print out metrics for the user. Metrics are rounded to two decimal places here for cleanliness.
            Functions are left unrounded to avoid decimal errors during calculations."""
    
        print("\nTotal Time of Flight: ", round(self.total_flight_time, 2), " seconds.")
        print("Max Height: ", round(self.max_height,2) , " meters.")
        print("Range : ", round(self.range,2) , " meters.")
        print("Impact velocity: ", round(self.impact_velocity, 2), " m/s.")