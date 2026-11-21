from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    x=np.asarray(x,dtype=float)
    mean=np.sum(x)/x.size
    max_freq=max(Counter(x).values())
    mode=min(val for val, freq in Counter(x).items() if freq==max_freq)
    x=np.sort(x)
    if x.size%2!=0:
        med=x[x.size//2]
    else:
        med=(x[x.size//2-1]+x[x.size//2])/2
    return {
        "mean":float(mean),
        "median":float(med),
        "mode":float(mode)
    }
    pass