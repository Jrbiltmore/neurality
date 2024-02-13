# src/stimulus/current_stimulus.py
import numpy as np
from base_stimulus import BaseStimulus

class CurrentStimulus(BaseStimulus):
    """A class for generating current injection stimuli for neural simulations."""

    def __init__(self, duration, amplitude, start_time=0):
        """
        Initializes a current stimulus object.

        Parameters:
        - duration: The duration of the stimulus (in milliseconds).
        - amplitude: The amplitude of the stimulus (in nanoamperes, nA).
        - start_time: The start time of the stimulus within the simulation (in milliseconds).
        """
        self.start_time = start_time
        super().__init__(duration, amplitude)

    def generate_stimulus(self):
        """Generates a current stimulus signal based on duration, amplitude, and start time.

        Overrides the BaseStimulus.generate_stimulus method.

        Returns:
        A tuple containing the start time and end time of the stimulus, and the stimulus signal (constant value).
        """
        end_time = self.start_time + self.duration
        # The signal is a constant value equal to the amplitude throughout the stimulus duration
        signal = np.array([self.amplitude for _ in range(self.start_time, end_time)])
        return self.start_time, end_time, signal

    def apply_to_neuron(self, neuron):
        """
        Applies the current stimulus to a neuron.

        Overrides the BaseStimulus.apply_to_neuron method.

        Parameters:
        - neuron: The neuron object to which the stimulus will be applied.
        """
        start_time, end_time, signal = self.generate_stimulus()
        # Assuming the neuron object has a method to receive current input
        neuron.receive_current(start_time, end_time, signal)
