# src/neurochemicals/neuromodulators.py

class NeuromodulatorDynamics:
    """Model for simulating the effects of neuromodulators on neural activity."""

    def __init__(self, initial_levels):
        """
        Parameters:
        - initial_levels: Dictionary mapping neuromodulators to their initial concentration levels.
        """
        self.levels = initial_levels.copy()

    def release_neuromodulator(self, neuromodulator, amount):
        """Simulate the release of a neuromodulator into the neural environment.
        
        Parameters:
        - neuromodulator: Name of the neuromodulator being released.
        - amount: Amount of neuromodulator released.
        """
        if neuromodulator in self.levels:
            self.levels[neuromodulator] += amount
        else:
            self.levels[neuromodulator] = amount

    def degrade_neuromodulator(self, neuromodulator, rate):
        """Simulate the degradation or reuptake of a neuromodulator.
        
        Parameters:
        - neuromodulator: Name of the neuromodulator being degraded.
        - rate: Rate of degradation or reuptake.
        """
        if neuromodulator in self.levels:
            self.levels[neuromodulator] -= self.levels[neuromodulator] * rate
            if self.levels[neuromodulator] < 0:
                self.levels[neuromodulator] = 0

    def get_neuromodulator_level(self, neuromodulator):
        """Retrieve the current level of a specific neuromodulator.
        
        Parameters:
        - neuromodulator: Name of the neuromodulator.
        
        Returns:
        - The current level of the neuromodulator.
        """
        return self.levels.get(neuromodulator, 0)

    def modulate_neural_activity(self, neuron, neuromodulator, effect_size):
        """Apply the modulatory effect of a neuromodulator on a neuron's activity.
        
        Parameters:
        - neuron: The neuron being modulated.
        - neuromodulator: Name of the neuromodulator.
        - effect_size: The size of the modulatory effect on the neuron's properties.
        """
        # Example: Modulate neuron's membrane potential based on neuromodulator level
        level = self.get_neuromodulator_level(neuromodulator)
        modulation_effect = level * effect_size
        neuron.membrane_potential += modulation_effect
