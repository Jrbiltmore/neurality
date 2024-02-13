# src/helpers/data_processing/spike_analysis.py

import numpy as np
from scipy.signal import find_peaks

class SpikeAnalysis:
    """Tools for analyzing spikes in neural simulation data."""
    
    def __init__(self, data, threshold=-55):
        """
        Parameters:
        - data: A numpy array or a pandas Series containing the membrane potential of a neuron.
        - threshold: The voltage threshold for spike detection.
        """
        self.data = data
        self.threshold = threshold
    
    def detect_spikes(self):
        """Detect spikes based on the membrane potential exceeding the threshold.
        
        Returns:
        - spikes: Indices of the time points where spikes occur.
        """
        spikes, _ = find_peaks(self.data, height=self.threshold)
        return spikes
    
    def calculate_isis(self, time):
        """Calculate inter-spike intervals (ISIs) from detected spikes.
        
        Parameters:
        - time: A numpy array or a pandas Series containing the corresponding time points for the data.
        
        Returns:
        - isis: Inter-spike intervals in milliseconds.
        """
        spikes = self.detect_spikes()
        spike_times = time[spikes]
        isis = np.diff(spike_times)
        return isis
    
    def spike_rate(self, total_time):
        """Calculate the average spike rate over the simulation duration.
        
        Parameters:
        - total_time: Total duration of the simulation in milliseconds.
        
        Returns:
        - rate: Average spike rate in Hz.
        """
        num_spikes = len(self.detect_spikes())
        rate = num_spikes / (total_time / 1000.0)  # Convert ms to seconds for Hz
        return rate
    
    def isi_histogram(self, bins=50):
        """Generate a histogram of inter-spike intervals.
        
        Parameters:
        - bins: Number of bins for the histogram.
        
        Returns:
        - hist: The values of the histogram.
        - bin_edges: The edges of the bins.
        """
        isis = self.calculate_isis(np.arange(len(self.data)))
        hist, bin_edges = np.histogram(isis, bins=bins)
        return hist, bin_edges
