# src/neurochemicals/gene_expression.py

class GeneExpression:
    """Model for simulating activity-dependent gene expression in neurons."""

    def __init__(self, baseline_expression_levels):
        """
        Parameters:
        - baseline_expression_levels: Dictionary mapping gene names to their baseline expression levels.
        """
        self.expression_levels = baseline_expression_levels.copy()

    def update_expression(self, activity_indicators):
        """Update gene expression levels based on neuronal activity indicators.
        
        Parameters:
        - activity_indicators: Dictionary mapping activity indicators (e.g., 'calcium') to their levels.
        """
        for gene, baseline_level in self.expression_levels.items():
            # Example: Adjust gene expression based on calcium levels
            if 'calcium' in activity_indicators:
                calcium_level = activity_indicators['calcium']
                self.expression_levels[gene] = self.calculate_expression_change(gene, baseline_level, calcium_level)

    def calculate_expression_change(self, gene, baseline_level, calcium_level):
        """Calculate the change in gene expression level based on calcium levels.
        
        This is a simplified model where the change in expression is directly proportional to calcium levels above a threshold.
        
        Parameters:
        - gene: The name of the gene.
        - baseline_level: Baseline expression level of the gene.
        - calcium_level: Current calcium level in the neuron.
        
        Returns:
        - new_expression_level: Updated expression level of the gene.
        """
        threshold = 0.0002  # Example threshold for calcium level to affect gene expression
        if calcium_level > threshold:
            # Example modulation: Increase expression linearly based on calcium level above threshold
            increase_factor = (calcium_level - threshold) * 1000  # Simplified factor for demonstration
            new_expression_level = baseline_level * (1 + increase_factor)
            return new_expression_level
        return baseline_level

    def get_expression_levels(self):
        """Return the current expression levels of genes."""
        return self.expression_levels
