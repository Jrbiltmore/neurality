# src/stimulus/sensory_stimulus.py

import numpy as np

class SensoryStimulus:
    """A class to generate and manage sensory stimuli for neural simulations."""
    
    def __init__(self, duration):
        """
        Parameters:
        - duration: The duration of the stimulus (in milliseconds).
        """
        self.duration = duration
        self.signal = None

    def generate_visual_stimulus(self, frequency, amplitude=1.0):
        """Generate a visual stimulus represented as a sine wave.
        
        Parameters:
        - frequency: Frequency of the visual oscillations (in Hz).
        - amplitude: Amplitude of the oscillations.
        """
        time = np.linspace(0, self.duration / 1000, num=int(self.duration))
        self.signal = amplitude * np.sin(2 * np.pi * frequency * time)

    def generate_auditory_stimulus(self, frequency, amplitude=1.0):
        """Generate an auditory stimulus represented as a sine wave.
        
        Parameters:
        - frequency: Frequency of the auditory tone (in Hz).
        - amplitude: Amplitude of the tone.
        """
        time = np.linspace(0, self.duration / 1000, num=int(self.duration))
        self.signal = amplitude * np.sin(2 * np.pi * frequency * time)

    def generate_tactile_stimulus(self, pattern):
        """Generate a tactile stimulus based on a specified pattern.
        
        Parameters:
        - pattern: A list or array representing the tactile stimulus pattern.
        """
        self.signal = np.array(pattern)

    def get_stimulus(self):
        """Retrieve the generated sensory stimulus.
        
        Returns:
        - The sensory stimulus signal.
        """
        return self.signal
