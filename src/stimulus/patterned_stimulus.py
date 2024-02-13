# src/stimulus/patterned_stimulus.py
import numpy as np
from base_stimulus import BaseStimulus

class PatternedStimulus(BaseStimulus):
    """A class for generating patterned stimuli for neural simulations."""
    
    def __init__(self, duration, amplitude, pattern_type='burst', frequency=10, **kwargs):
        """
        Initializes a patterned stimulus object.

        Parameters:
        - duration: The duration of the stimulus (in milliseconds).
        - amplitude: The amplitude of the stimulus.
        - pattern_type: The type of pattern ('burst', 'oscillatory', 'random').
        - frequency: The frequency of the pattern, applicable for 'oscillatory' patterns (in Hz).
        """
        self.pattern_type = pattern_type
        self.frequency = frequency
        super().__init__(duration, amplitude, **kwargs)

    def generate_stimulus(self):
        """Generates a patterned stimulus signal based on specified parameters.

        Overrides the BaseStimulus.generate_stimulus method.

        Returns:
        A numpy array representing the stimulus signal over time.
        """
        time = np.linspace(0, self.duration / 1000, num=int(self.duration))
        if self.pattern_type == 'burst':
            # Generate a burst pattern
            signal = self.amplitude * (np.sin(2 * np.pi * self.frequency * time) > 0).astype(int)
        elif self.pattern_type == 'oscillatory':
            # Generate an oscillatory pattern
            signal = self.amplitude * np.sin(2 * np.pi * self.frequency * time)
        elif self.pattern_type == 'random':
            # Generate a random pattern
            np.random.seed(42)  # For reproducibility
            signal = np.random.normal(loc=0, scale=self.amplitude, size=time.shape)
        else:
            raise ValueError("Unsupported pattern type specified.")
        return signal

    def apply_to_neuron(self, neuron):
        """
        Applies the patterned stimulus to a neuron.

        Overrides the BaseStimulus.apply_to_neuron method.

        Parameters:
        - neuron: The neuron object to which the stimulus will be applied.
        """
        signal = self.generate_stimulus()
        # Assuming the neuron object has a method to receive complex input
        neuron.receive_complex_input(signal)
