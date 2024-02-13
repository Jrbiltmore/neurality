# src/models/neuron/izhikevich_model.py

class IzhikevichModel:
    """Implementation of the Izhikevich neuron model."""
    
    def __init__(self, a=0.02, b=0.2, c=-65, d=8, I_ext=5):
        """
        Initializes the Izhikevich neuron model with default parameters.
        
        Parameters:
        - a: The time scale of the recovery variable. Smaller values result in slower recovery.
        - b: The sensitivity of the recovery variable to the subthreshold fluctuations of the membrane potential.
        - c: The after-spike reset value of the membrane potential.
        - d: After-spike reset of the recovery variable.
        - I_ext: External current applied to the neuron (stimulus).
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.I_ext = I_ext
        
        # Initial values
        self.v = c  # Membrane potential
        self.u = b * c  # Recovery variable

    def update(self, dt):
        """
        Update the neuron's state by integrating the Izhikevich equations over a time step dt.
        
        Parameters:
        - dt: Time step for integration (in milliseconds).
        """
        if self.v >= 30:
            # Spike reached, reset variables
            self.v = self.c
            self.u += self.d
        else:
            # Izhikevich model equations
            dv_dt = 0.04*self.v**2 + 5*self.v + 140 - self.u + self.I_ext
            du_dt = self.a * (self.b * self.v - self.u)
            
            # Euler integration
            self.v += dv_dt * dt
            self.u += du_dt * dt

    def get_state(self):
        """
        Returns the current state of the neuron.
        
        Returns:
        - v: Current membrane potential.
        - u: Current recovery variable.
        """
        return self.v, self.u
