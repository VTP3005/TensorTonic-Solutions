def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    x=x0
    for i in range(steps):
        dy=2*a*x+b
        x-=lr*dy
    return x
    pass