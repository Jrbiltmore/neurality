# src/helpers/data_processing/data_analyzer.py

import numpy as np
import pandas as pd
from scipy import signal
from scipy.stats import pearsonr

class DataAnalyzer:
    """Advanced tools for analyzing neural simulation data."""
    
    def __init__(self, data):
        """
        Parameters:
        - data: A pandas DataFrame containing simulation data with 'time' and 'V_m' columns at minimum.
        """
        self.data = data
        
    def spectral_analysis(self, sampling_rate):
        """Perform spectral analysis to identify dominant frequencies in the neuron's activity.
        
        Parameters:
        - sampling_rate: Sampling rate of the data in Hz.
        
        Returns:
        - frequencies: Array of frequencies.
        - power: Power spectral density of the data.
        """
        f, Pxx_den = signal.periodogram(self.data['V_m'], sampling_rate)
        return f, Pxx_den
    
    def cross_correlation(self, other_data, lag_max=None):
        """Calculate cross-correlation with another dataset to find relationships in activity.
        
        Parameters:
        - other_data: Another pandas Series or array to correlate with.
        - lag_max: Maximum lag to compute correlation for, in data points.
        
        Returns:
        - correlation: Cross-correlation values for different lags.
        """
        correlation = np.correlate(self.data['V_m'], other_data, mode='full', method='auto')
        if lag_max:
            mid = len(correlation) // 2
            correlation = correlation[mid - lag_max: mid + lag_max + 1]
        return correlation
    
    def pearson_correlation_coefficient(self, other_data):
        """Calculate the Pearson correlation coefficient with another dataset.
        
        Parameters:
        - other_data: Another pandas Series or array to correlate with.
        
        Returns:
        - r: Pearson correlation coefficient.
        """
        r, _ = pearsonr(self.data['V_m'], other_data)
        return r
    
    def identify_network_activity_patterns(self, threshold=-55):
        """Identify patterns of network activity based on threshold crossings.
        
        Parameters:
        - threshold: Voltage threshold to identify significant activity.
        
        Returns:
        - pattern_times: Times where the network activity crosses the threshold.
        """
        crossings = np.diff((self.data['V_m'] > threshold).astype(int), prepend=0)
        pattern_times = self.data['time'][crossings == 1]
        return pattern_times.values
