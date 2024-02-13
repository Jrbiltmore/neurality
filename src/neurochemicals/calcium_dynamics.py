# src/neurochemicals/calcium_dynamics.py

import numpy as np

class CalciumDynamics:
    """Model for calcium ion dynamics within neurons."""
    
    def __init__(self, initial_concentration=0.0001, decay_rate=0.001):
        """
        Parameters:
        - initial_concentration: Initial concentration of calcium ions (mol/L).
        - decay_rate: Rate at which calcium concentration decays back to baseline.
        """
        self.concentration = initial_concentration
        self.decay_rate = decay_rate
        self.baseline_concentration = initial_concentration
    
    def influx(self, amount):
        """Simulate an influx of calcium ions into the neuron.
        
        Parameters:
        - amount: The amount of calcium ions entering the neuron (mol/L).
        """
        self.concentration += amount
    
    def efflux(self, amount):
        """Simulate an efflux of calcium ions out of the neuron.
        
        Parameters:
        - amount: The amount of calcium ions exiting the neuron (mol/L).
        """
        self.concentration -= amount
        if self.concentration < self.baseline_concentration:
            self.concentration = self.baseline_concentration
    
    def decay_to_baseline(self, timestep):
        """Decay the calcium concentration back to its baseline over time.
        
        Parameters:
        - timestep: The time step over which to decay the concentration (s).
        """
        decay_amount = (self.concentration - self.baseline_concentration) * np.exp(-self.decay_rate * timestep)
        self.concentration -= decay_amount
        if self.concentration < self.baseline_concentration:
            self.concentration = self.baseline_concentration
    
    def trigger_synaptic_modification(self):
        """Determine if the current calcium concentration can trigger synaptic modification.
        
        Returns:
        - can_modify: Boolean indicating if synaptic modification can occur.
        """
        threshold_for_modification = 0.0002  # mol/L, example threshold
        can_modify = self.concentration > threshold_for_modification
        return can_modify
