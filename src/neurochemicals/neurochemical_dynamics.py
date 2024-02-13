# src/neurochemicals/neurochemical_dynamics.py

import numpy as np

class NeurochemicalDynamics:
    """Simulate and analyze neurochemical effects on neurons and networks."""
    
    def __init__(self, initial_concentration=0.0):
        """
        Parameters:
        - initial_concentration: Initial concentration of the neurochemical in the synaptic cleft or intracellularly.
        """
        self.concentration = initial_concentration
    
    def release_neurochemical(self, amount):
        """Simulate the release of a neurochemical.
        
        Parameters:
        - amount: Amount of neurochemical released into the synaptic cleft or cellular environment.
        """
        self.concentration += amount
    
    def degrade_neurochemical(self, rate):
        """Simulate the degradation or reuptake of a neurochemical.
        
        Parameters:
        - rate: Rate of degradation or reuptake.
        """
        self.concentration -= rate * self.concentration
    
    def effect_on_post_synaptic_neuron(self, sensitivity):
        """Calculate the effect of a neurochemical on a post-synaptic neuron, based on its sensitivity.
        
        Parameters:
        - sensitivity: Sensitivity of the post-synaptic neuron to the neurochemical.
        
        Returns:
        - effect: The effect of the neurochemical on the post-synaptic neuron's properties.
        """
        effect = sensitivity * self.concentration
        return effect

class CalciumDynamics(NeurochemicalDynamics):
    """Specific model for calcium signaling dynamics within neurons."""
    
    def __init__(self, initial_ca_concentration=0.1):
        super().__init__(initial_concentration=initial_ca_concentration)
    
    def calcium_influx(self, influx_rate, duration):
        """Simulate calcium influx through channels or pumps.
        
        Parameters:
        - influx_rate: Rate of calcium influx.
        - duration: Duration of the influx.
        """
        self.concentration += influx_rate * duration

    def calcium_efflux(self, efflux_rate, duration):
        """Simulate calcium efflux from the neuron.
        
        Parameters:
        - efflux_rate: Rate of calcium efflux.
        - duration: Duration of the efflux.
        """
        self.concentration -= efflux_rate * duration
