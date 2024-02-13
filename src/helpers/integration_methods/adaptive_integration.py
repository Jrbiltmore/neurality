# src/helpers/integration_methods/adaptive_integration.py

import numpy as np

def adaptive_euler_method(f, y0, t, tol=1e-3):
    """Adaptive Euler's method for numerical integration with error control.
    
    Parameters:
    - f: The derivative function of y, f(t, y).
    - y0: Initial value of y.
    - t: Array of time points for which to solve for y.
    - tol: Tolerance for local error estimate.
    
    Returns:
    - y: Integrated values of y over time t.
    """
    y = [y0]
    current_t = t[0]
    for next_t in t[1:]:
        dt = next_t - current_t
        y_est = y[-1] + dt * f(current_t, y[-1])
        # Error estimation
        half_step = y[-1] + dt/2 * f(current_t, y[-1])
        error = np.abs(half_step - y_est)
        # Adjust step size based on error
        while error > tol:
            dt = dt / 2
            y_est = y[-1] + dt * f(current_t, y[-1])
            half_step = y[-1] + dt/2 * f(current_t, y[-1])
            error = np.abs(half_step - y_est)
        y.append(y_est)
        current_t = next_t
    return np.array(y)

def adaptive_runge_kutta_4(f, y0, t, tol=1e-3):
    """Adaptive fourth-order Runge-Kutta method for numerical integration with error control.
    
    Parameters:
    - f: The derivative function of y, f(t, y).
    - y0: Initial value of y.
    - t: Array of time points for which to solve for y.
    - tol: Tolerance for local error estimate.
    
    Returns:
    - y: Integrated values of y over time t.
    """
    y = [y0]
    current_t = t[0]
    for next_t in t[1:]:
        dt = next_t - current_t
        k1 = f(current_t, y[-1])
        k2 = f(current_t + dt/2, y[-1] + dt/2 * k1)
        k3 = f(current_t + dt/2, y[-1] + dt/2 * k2)
        k4 = f(next_t, y[-1] + dt * k3)
        y_est = y[-1] + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)
        # Error estimation
        error = np.abs(y_est - y[-1])
        # Adjust step size based on error
        while error > tol:
            dt = dt / 2
            k1 = f(current_t, y[-1])
            k2 = f(current_t + dt/2, y[-1] + dt/2 * k1)
            k3 = f(current_t + dt/2, y[-1] + dt/2 * k2)
            k4 = f(current_t + dt, y[-1] + dt * k3)
            y_est = y[-1] + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)
            error = np.abs(y_est - y[-1])
        y.append(y_est)
        current_t = next_t
    return np.array(y)
