# src/helpers/data_processing/signal_processing.py

import numpy as np
from scipy.signal import butter, lfilter, detrend, hilbert

class SignalProcessing:
    """Signal processing tools for neural simulation data."""
    
    def __init__(self, data):
        """
        Parameters:
        - data: A numpy array or a pandas Series containing the signal to be processed.
        """
        self.data = data
        
    def butter_lowpass_filter(self, cutoff, fs, order=5):
        """Apply a low-pass Butterworth filter to the signal.
        
        Parameters:
        - cutoff: The cutoff frequency of the filter in Hz.
        - fs: The sampling rate of the signal in Hz.
        - order: The order of the filter.
        
        Returns:
        - y: The filtered signal.
        """
        nyq = 0.5 * fs
        normal_cutoff = cutoff / nyq
        b, a = butter(order, normal_cutoff, btype='low', analog=False)
        y = lfilter(b, a, self.data)
        return y
    
    def remove_trend(self):
        """Remove linear trend from the signal.
        
        Returns:
        - y: The detrended signal.
        """
        y = detrend(self.data)
        return y
    
    def hilbert_transform(self):
        """Apply the Hilbert transform to the signal to obtain its analytic signal.
        
        Returns:
        - amplitude_envelope: The amplitude envelope of the signal.
        - instantaneous_phase: The instantaneous phase of the signal.
        - instantaneous_frequency: The instantaneous frequency of the signal, derived from the phase.
        """
        analytic_signal = hilbert(self.data)
        amplitude_envelope = np.abs(analytic_signal)
        instantaneous_phase = np.unwrap(np.angle(analytic_signal))
        instantaneous_frequency = np.diff(instantaneous_phase) / (2.0*np.pi)
        return amplitude_envelope, instantaneous_phase[:-1], instantaneous_frequency
    
    def bandpass_filter(self, lowcut, highcut, fs, order=5):
        """Apply a bandpass filter to the signal.
        
        Parameters:
        - lowcut: The lower boundary of the filter in Hz.
        - highcut: The upper boundary of the filter in Hz.
        - fs: The sampling rate of the signal in Hz.
        - order: The order of the filter.
        
        Returns:
        - y: The filtered signal.
        """
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        b, a = butter(order, [low, high], btype='band')
        y = lfilter(b, a, self.data)
        return y
