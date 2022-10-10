import math

def find_initial_horizontal_velocity(initial_velocity, angle):
    """Return the initial horizontal velocity of the projectile
        based on the angle above the x-axis and its initial velocity.
    """
    # Converts the input angle from degrees to radians.
    radian_angle = math.radians(angle)

    # Calcualtes initial horizontal velocity by multiplying initial velocity by the cosine of the angle.
    h_initial_velocity = initial_velocity * math.cos(radian_angle)
    return h_initial_velocity

def find_intial_vertical_velocity(initial_velocity, angle):
    """Returns the intial vertical velocity of the projectile
        based on the angle above the x axis and its initial velocity.
    """
    radian_angle = math.radians(angle)
    y_velocity = initial_velocity * math.sin(radian_angle)
    return y_velocity

def find_time_to_max_height(initial_vertical_velocity):
    """Returns the time the projectile reachs the highest point in its 
        trajectory.
    """
    time_to_max_height= initial_vertical_velocity / (9.81)
    return time_to_max_height

def find_total_flight_time(time_to_max_height, max_height):
    """Returns the total time the projectile is in flight prior to 
        impacting the ground.
    """
    time_of_descent = math.sqrt(2*max_height / 9.81)
    total_flight_time = time_to_max_height + time_of_descent
    return total_flight_time

def find_max_height(time_to_max_height, initial_vertical_velocity, initial_height, initial_angle):
    """Returns the max height the projectile reaches during its flight."""
    
    # Max_height is set equal to the initial height if the angle of the projectile is below the horizontal plane
    if initial_angle == 0:
        max_height = initial_height
    elif (180 < initial_angle <= 360):
        max_height = initial_height
    else:    
        max_height = (initial_vertical_velocity * time_to_max_height) - (.5 * 9.81 * (time_to_max_height**2)) + initial_height
    return max_height

def find_range(horizontal_velocity, total_flight_time, initial_angle):
    """Returns the range (horizontal displacement) of the projectile."""
    # Sets range to zero if angle is completely vertical to avoid rounding errors.
    if initial_angle == 90:
        projectile_range = 0
    else: 
        projectile_range = horizontal_velocity * total_flight_time
    return projectile_range

def find_impact_velocity(horizontal_velocity, max_height):
    """Returns the impact velocity of the projectile. """
    
    # Calculates how long the projectile is in flight
    time_of_descent = math.sqrt(2*max_height / 9.81)

    # Calculates the component vectors
    x_component_of_velocity = horizontal_velocity
    y_component_of_velocity_at_impact = (9.81) * time_of_descent
    
    # Calculates impact velocity by finding square root of the sum of each component squared.
    impact_velocity = math.sqrt(x_component_of_velocity **2 + y_component_of_velocity_at_impact**2)
    return impact_velocity