# src/models/neuron/fhn_model.py

import numpy as np

class FitzHughNagumoModel:
    """Implementation of the FitzHugh-Nagumo neuron model."""
    
    def __init__(self, a=0.7, b=0.8, tau=12.5, I_ext=0.0):
        """
        Initializes the FHN neuron model with default parameters.
        
        Parameters:
        - a: Parameter controlling the threshold for excitation.
        - b: Recovery rate parameter.
        - tau: Timescale parameter for the recovery variable.
        - I_ext: External current applied to the neuron (stimulus).
        """
        self.a = a
        self.b = b
        self.tau = tau
        self.I_ext = I_ext
        
        # Initial values
        self.v = np.array([0.0])  # Membrane potential
        self.w = np.array([0.0])  # Recovery variable

    def update(self, dt):
        """
        Update the neuron's state by integrating the FHN equations over a time step dt.
        
        Parameters:
        - dt: Time step for integration (in milliseconds).
        """
        v, w = self.v[-1], self.w[-1]
        
        # FitzHugh-Nagumo Equations
        dv_dt = v - (v**3 / 3) - w + self.I_ext
        dw_dt = (v + self.a - self.b * w) / self.tau
        
        # Euler integration
        v_next = v + dv_dt * dt
        w_next = w + dw_dt * dt
        
        # Append the next state to the history
        self.v = np.append(self.v, v_next)
        self.w = np.append(self.w, w_next)

    def get_state(self):
        """
        Returns the current state of the neuron.
        
        Returns:
        - v: Current membrane potential.
        - w: Current recovery variable.
        """
        return self.v[-1], self.w[-1]
