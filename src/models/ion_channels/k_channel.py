# src/models/ion_channels/k_channel.py

import numpy as np

class PotassiumChannel:
    """Model of the potassium ion channel."""
    def __init__(self):
        # Potassium channel gating variable
        self.n = 0.32

    def alpha_n(self, V):
        """Rate constant for activation gating variable n."""
        return 0.01 * (V + 55) / (1 - np.exp(-(V + 55) / 10))

    def beta_n(self, V):
        """Rate constant for deactivation gating variable n."""
        return 0.125 * np.exp(-(V + 65) / 80)

    def update_gating_variables(self, V, dt):
        """Update the gating variable n."""
        n_next = self.alpha_n(V) * (1 - self.n) - self.beta_n(V) * self.n
        
        self.n += n_next * dt

    def current(self, V, E_K):
        """Calculate the potassium current through the channel."""
        g_K_max = 36  # Maximum conductance (mS/cm^2)
        I_K = g_K_max * (self.n**4) * (V - E_K)
        return I_K
