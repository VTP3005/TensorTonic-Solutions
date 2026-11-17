import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    x=np.array(x)
    y=np.array(y)
    euclidean_distance=np.sqrt(np.sum((x-y)**2))
    return float(euclidean_distance)
    pass