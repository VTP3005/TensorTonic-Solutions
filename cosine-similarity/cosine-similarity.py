import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    a=np.array(a)
    b-np.array(b)
    if np.linalg.norm(a)*np.linalg.norm(b)==0:
        return float(0)
    return float(a@b/(np.linalg.norm(a)*np.linalg.norm(b)))
    pass