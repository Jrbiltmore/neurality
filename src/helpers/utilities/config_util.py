# src/helpers/utilities/config_util.py

import json

class Config:
    """Class for loading and accessing configuration settings."""
    
    def __init__(self, config_path):
        """
        Parameters:
        - config_path: Path to the JSON configuration file.
        """
        self.config_path = config_path
        self.settings = self.load_config()
    
    def load_config(self):
        """Load the configuration settings from a JSON file."""
        with open(self.config_path, 'r') as config_file:
            return json.load(config_file)
    
    def get(self, key, default=None):
        """Retrieve a value from the configuration settings.
        
        Parameters:
        - key: Key for the setting to retrieve.
        - default: Default value to return if the key is not found.
        """
        return self.settings.get(key, default)
