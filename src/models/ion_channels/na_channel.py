# src/models/ion_channels/na_channel.py

import numpy as np

class SodiumChannel:
    """Model of the sodium ion channel."""
    def __init__(self):
        # Sodium channel gating variables
        self.m = 0.05
        self.h = 0.6

    def alpha_m(self, V):
        """Rate constant for activation gating variable m."""
        return 0.1 * (V + 40) / (1 - np.exp(-(V + 40) / 10))

    def beta_m(self, V):
        """Rate constant for deactivation gating variable m."""
        return 4.0 * np.exp(-(V + 65) / 18)

    def alpha_h(self, V):
        """Rate constant for inactivation gating variable h."""
        return 0.07 * np.exp(-(V + 65) / 20)

    def beta_h(self, V):
        """Rate constant for deactivation gating variable h."""
        return 1 / (1 + np.exp(-(V + 35) / 10))

    def update_gating_variables(self, V, dt):
        """Update the gating variables m and h."""
        m_next = self.alpha_m(V) * (1 - self.m) - self.beta_m(V) * self.m
        h_next = self.alpha_h(V) * (1 - self.h) - self.beta_h(V) * self.h
        
        self.m += m_next * dt
        self.h += h_next * dt

    def current(self, V, E_Na):
        """Calculate the sodium current through the channel."""
        g_Na_max = 120  # Maximum conductance (mS/cm^2)
        I_Na = g_Na_max * (self.m**3) * self.h * (V - E_Na)
        return I_Na
