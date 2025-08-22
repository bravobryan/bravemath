import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot_real_numbers(selection):
    """
    Create a simple template for plotting real numbers on a horizontal line.
    :param selection: A list or array of two real numbers representing the interval.
    :raises ValueError: If the selection does not contain exactly two values.
    :return: fig, ax - Matplotlib figure and axis objects.

    Example usage:
    >>> selection = [9, 15]
    >>> fig, ax = plot_real_numbers(selection)
    >>> ax.plot(selection[0], [0], marker='o', markersize=20, color='green')
    >>> ax.plot(selection[1], [0], marker='>', markersize=20, color='green')
    >>> ax.plot(selection, [0]*len(selection), marker=None, color='green',  linewidth=5)
    >>> ax.set_title(f'Representing [{selection[0]}, ∞)')
    >>> plt.show()


    #### Created on 2025-08-22 by BravoBryan
    """
    if len(selection) != 2:
            raise ValueError("Selection must contain exactly two values.")
    values = np.sort(np.array(selection))

    range_values = [*range(int(np.min(values)-np.abs(np.mean(values)*0.50)), int(np.max(values)+np.abs(np.mean(values)*0.50)))]

    fig, ax = plt.subplots(figsize=(10, 2))

    ax.plot(range_values, [0] * len(range_values), linestyle="", marker='|', markersize=10, color='black')

    ax.plot(range_values, [0] * len(range_values), linestyle=None, color='black')

    ax.set_ylim(-1, 1)
    ax.set_yticklabels([])
    # plt.show()
    return fig, ax

# Example use case
if __name__ == "__main__":
    selection = [9, 15]

    ## Representing [a, infinity)
    selection = np.sort(np.array(selection))  # Seletion needs to be sorted and have two values.
    fig, ax = plot_real_numbers(selection)
    ax.plot(selection[0], [0], marker='o', markersize=20, color='green')
    ax.plot(selection[1], [0], marker='>', markersize=20, color='green')
    ax.plot(selection, [0]*len(selection), marker=None, color='green', linewidth=5)
    ax.set_title(f'Representing [{selection[0]}, ∞)')
    plt.show()

    ## Representing (-infinity, b)
    selection = np.sort(np.array(selection))  # Seletion needs to be sorted and have two values.
    fig, ax = plot_real_numbers(selection)
    ax.plot(selection[1], [0], marker='o', markersize=20, color='green', markerfacecolor='none')
    ax.plot(selection[0], [0], marker='<', markersize=20, color='green')
    ax.plot(selection, [0]*len(selection), marker=None, color='green', linewidth=5)
    ax.set_title(f'Representing (-∞, {selection[1]}]')

    plt.show()

    ## Representing (-infinity, a] U [b, infinity)
    selection = np.sort(np.array(selection))  # Seletion needs to be sorted and have two values.
    fig, ax = plot_real_numbers(selection)
    # Negative infinity side.
    ax.plot(selection[0], [0], marker='o', markersize=20, color='green')
    ax.plot(selection[0]-(np.abs(np.mean(selection)*0.35)), [0], marker='<', markersize=20, color='green', markerfacecolor='none')
    ax.plot([*range(int(selection[0]-(np.abs(np.mean(selection)*0.35))),
                    selection[0]+1)], [0]*len([*range(int(selection[0]-(np.abs(np.mean(selection)*0.35))), selection[0]+1)]), marker=None, color='green', linewidth=5)
    # Positive infinity side.
    ax.plot(selection[1], [0], marker='o', markersize=20, color='green')
    ax.plot(selection[1]+(np.abs(np.mean(selection)*0.35)), [0], marker='>', markersize=20, color='green', markerfacecolor='none')
    ax.plot([*range(selection[1], int(selection[1]+(np.abs(np.mean(selection)*0.35))+1))],
            [0]*len([*range(selection[1], int(selection[1]+(np.abs(np.mean(selection)*0.35))+1))]), marker=None, color='green', linewidth=5)
    ax.set_title(f'Representing (-∞, {selection[0]}] U [{selection[1]}, ∞)')
    plt.show()