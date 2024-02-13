# src/stimulus/stimulus_generator.py

import numpy as np

class StimulusGenerator:
    """Generates external stimuli for neuron simulations."""
    def __init__(self, duration, timestep):
        self.duration = duration  # Total duration of the stimulus (ms)
        self.timestep = timestep  # Time resolution (ms)
        self.time = np.arange(0, self.duration, self.timestep)
        
    def constant_current(self, amplitude):
        """Generates a constant current stimulus."""
        return np.full(len(self.time), amplitude)

    def sinusoidal_current(self, amplitude, frequency):
        """Generates a sinusoidal current stimulus."""
        return amplitude * np.sin(2 * np.pi * frequency * self.time)

    def random_noise(self, mean, std):
        """Generates a random noise current stimulus."""
        return np.random.normal(mean, std, len(self.time))

    def patterned_input(self, pattern, repeats):
        """Generates a repeating patterned current stimulus."""
        pattern_length = len(pattern)
        total_length = pattern_length * repeats
        if total_length > len(self.time):
            raise ValueError("Pattern repeats exceed stimulus duration.")
        patterned_stimulus = np.tile(pattern, repeats)
        return np.pad(patterned_stimulus, (0, len(self.time) - total_length), 'constant')
