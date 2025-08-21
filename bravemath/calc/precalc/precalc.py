import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot_real_numbers(selection):
    """
    Plot a horizontal line with selected values and their distance.
    Parameters:
    - selection: A list or array of two real numbers representing the interval.
    This function will plot the interval and annotate the midpoint, radius, and distance between the two values.
    It will also plot the range of values between the two selected numbers.
    
    Updated: 
        - 2025-08-20: Created the function.
    
    """
    if len(selection) != 2:
        raise ValueError("Selection must contain exactly two values.")
    values = np.array(selection)

    mid_selection = np.mean(selection)
    range_values = [*range(np.min(values), np.max(values)+1, 1)]

    fig, ax = plt.subplots(figsize=(10, 2))

    # Annotate each value on the x-axis
    for i, value in enumerate(values):
        ax.annotate(str(value), (value, 0), textcoords="offset points", xytext=(0,10), ha='center')

    ax.plot(values, [0] * len(values), linestyle='-', marker='o', markersize=10, color='Red')
    ax.plot(range_values, [0] * len(range_values), linestyle=None, marker='|', markersize=10, color='Black')

    ax.annotate(f"{selection[0]}", (selection[0], 1), textcoords="offset points", xytext=(0,10), ha='center', color='Black')
    ax.annotate(f"{selection[1]}", (selection[1], 1), textcoords="offset points", xytext=(0,10), ha='center', color='Black')
    ax.annotate(f'Distance: {np.abs(selection[1]-selection[0])}', (mid_selection, 1), textcoords="offset points", xytext=(0,15), ha='center', color='Black')
    ax.plot(selection, [1] * len(selection), linestyle='-', marker='|', markersize=10, color='Black')

    ax.set_ylim(-1, 2)
    ax.set_yticklabels([])

    # Plot the midpoint
    ax.annotate(f'Midpoint: {mid_selection}', (mid_selection, 1), textcoords="offset points", xytext=(0,25), ha='center', color='Blue')
    ax.plot([mid_selection], [1], marker='o', markersize=10, color='Blue')

    # Plot the radius
    ax.annotate(f'Radius: {np.abs(selection[1]-selection[0])/2}', (mid_selection, 1), textcoords="offset points", xytext=(0,-15), ha='center', color='Green')
    ax.plot([mid_selection - np.abs(selection[1]-selection[0])/2, mid_selection + np.abs(selection[1]-selection[0])/2], [1, 1], linestyle='--', color='Green')

    # Add the title and labels
    ax.set_title(f'Defining [{selection[0]}, {selection[1]}] as an interval')

    plt.show()

##### Example usage: ######
if __name__ == '__main__':
    values = np.random.randint(-25, 25, size=2)

    plot_real_numbers(values)
