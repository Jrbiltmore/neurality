# src/helpers/integration_methods.py

import numpy as np

def euler_method(f, y0, t):
    """Euler's method for numerical integration.
    
    Parameters:
    - f: The derivative function of y, f(t, y).
    - y0: Initial value of y at t0.
    - t: Array of time points for which to solve for y.
    
    Returns:
    - y: Integrated values of y over time t.
    """
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(1, len(t)):
        dt = t[i] - t[i-1]
        y[i] = y[i-1] + f(t[i-1], y[i-1]) * dt
    return y

def runge_kutta_4(f, y0, t):
    """Fourth-order Runge-Kutta method for numerical integration.
    
    Parameters:
    - f: The derivative function of y, f(t, y).
    - y0: Initial value of y at t0.
    - t: Array of time points for which to solve for y.
    
    Returns:
    - y: Integrated values of y over time t.
    """
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(1, len(t)):
        dt = t[i] - t[i-1]
        k1 = f(t[i-1], y[i-1])
        k2 = f(t[i-1] + dt/2, y[i-1] + dt/2 * k1)
        k3 = f(t[i-1] + dt/2, y[i-1] + dt/2 * k2)
        k4 = f(t[i], y[i-1] + dt * k3)
        y[i] = y[i-1] + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)
    return y
