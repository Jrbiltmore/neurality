# src/stimulus/base_stimulus.py

class BaseStimulus:
    """Base class for all types of stimuli in neural simulations."""
    
    def __init__(self, duration, amplitude):
        """
        Initializes a stimulus object.
        
        Parameters:
        - duration: The duration of the stimulus (in milliseconds).
        - amplitude: The amplitude of the stimulus.
        """
        self.duration = duration
        self.amplitude = amplitude
        self.signal = self.generate_stimulus()

    def generate_stimulus(self):
        """
        Generates the stimulus signal based on duration and amplitude.
        
        This method should be overridden by subclasses to produce specific types of stimuli.
        
        Returns:
        A numpy array representing the stimulus signal over time.
        """
        raise NotImplementedError("Subclass must implement abstract method.")
    
    def apply_to_neuron(self, neuron):
        """
        Applies the stimulus to a neuron.
        
        This method can be customized in subclasses to define how the stimulus interacts with neuron properties.
        
        Parameters:
        - neuron: The neuron object to which the stimulus will be applied.
        """
        raise NotImplementedError("Subclass must implement abstract method.")
