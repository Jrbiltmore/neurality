# src/helpers/data_recorder.py

import numpy as np
import pandas as pd

class DataRecorder:
    """Class for recording and exporting simulation data."""
    def __init__(self):
        self.data = {
            'time': [],
            'V_m': [],
            'gating_variables': {}
        }
    
    def record(self, time, V_m, gating_vars=None):
        """Record the neuron's membrane potential and optionally gating variables at a given time."""
        self.data['time'].append(time)
        self.data['V_m'].append(V_m)
        if gating_vars:
            for var_name, var_value in gating_vars.items():
                if var_name not in self.data['gating_variables']:
                    self.data['gating_variables'][var_name] = []
                self.data['gating_variables'][var_name].append(var_value)
    
    def export_to_csv(self, filename):
        """Export recorded data to a CSV file."""
        df = pd.DataFrame(self.data)
        gating_vars_df = pd.DataFrame(self.data['gating_variables'])
        full_df = pd.concat([df[['time', 'V_m']], gating_vars_df], axis=1)
        full_df.to_csv(filename, index=False)
    
    def reset(self):
        """Reset the recorder to record a new simulation."""
        self.data = {
            'time': [],
            'V_m': [],
            'gating_variables': {}
        }
