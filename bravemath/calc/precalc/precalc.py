import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot_real_numbers(values, selection):
    """
    Plot a horizontal line with selected values and their distance.
    Parameters:
    - values: A list or array of real numbers.
    - selection: A list or array containing exactly two values from `values`.   
    Raises:
    - ValueError: If `selection` does not contain exactly two values or if `values` contains non-numeric types.
    """
    if len(selection) != 2:
        raise ValueError("Selection must contain exactly two values.")


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

    plt.show()

##### Example usage: ######
if __name__ == '__main__':
    values = np.random.randint(-25, 25, size=10)
    selection = np.random.choice(values, size=2, replace=False)

    plot_real_numbers(values, selection)
