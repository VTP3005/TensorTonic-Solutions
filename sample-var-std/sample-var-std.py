import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    x=np.asarray(x, dtype=float)
    x_average=x.mean()
    variance=np.sum((x-x_average)**2)/(x.size-1)
    std_dev=np.sqrt(variance)
    return {
        "variance": float(variance),
        "standard_deviation": float(std_dev)
    }
    pass