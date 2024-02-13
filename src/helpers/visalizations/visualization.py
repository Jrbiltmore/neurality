# src/helpers/visualization/visualization.py

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.gridspec import GridSpec

def plot_membrane_potential(time, V_m, title="Membrane Potential Over Time"):
    plt.figure(figsize=(12, 6))
    plt.plot(time, V_m, label='Membrane Potential (mV)')
    plt.title(title)
    plt.xlabel('Time (ms)')
    plt.ylabel('Membrane Potential (mV)')
    plt.legend()
    plt.grid(True)
    plt.show()

def dynamic_membrane_potential(time, V_m, interval=50, title="Dynamic Membrane Potential"):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_title(title)
    ax.set_xlabel('Time (ms)')
    ax.set_ylabel('Membrane Potential (mV)')
    line, = ax.plot([], [], lw=2)

    def init():
        ax.set_xlim(np.min(time), np.max(time))
        ax.set_ylim(np.min(V_m) - 5, np.max(V_m) + 5)
        return line,

    def update(frame):
        line.set_data(time[:frame], V_m[:frame])
        return line,

    ani = FuncAnimation(fig, update, frames=len(time), init_func=init, blit=True, interval=interval)
    plt.show()

def phase_space_plot(V_m, gating_var, gating_var_label="n", title="Phase Space Plot"):
    plt.figure(figsize=(8, 8))
    plt.plot(V_m, gating_var, label=gating_var_label)
    plt.title(title)
    plt.xlabel('Membrane Potential (mV)')
    plt.ylabel(f'Gating Variable ({gating_var_label})')
    plt.legend()
    plt.grid(True)
    plt.show()

def network_connectivity_diagram(adjacency_matrix, title="Network Connectivity"):
    fig, ax = plt.subplots(figsize=(8, 8))
    cmap = plt.get_cmap('viridis', np.max(adjacency_matrix) - np.min(adjacency_matrix) + 1)
    mat = ax.matshow(adjacency_matrix, cmap=cmap)
    plt.colorbar(mat, ticks=np.arange(np.min(adjacency_matrix), np.max(adjacency_matrix) + 1))
    ax.set_title(title)
    ax.set_xlabel('Neuron Index')
    ax.set_ylabel('Neuron Index')
    plt.show()

def combined_view(time, V_m, spikes, activity_matrix, title="Combined Simulation View"):
    fig = plt.figure(constrained_layout=True, figsize=(15, 10))
    fig.suptitle(title)
    gs = GridSpec(3, 1, figure=fig)

    ax1 = fig.add_subplot(gs[0, 0])
    ax1.plot(time, V_m, label='Membrane Potential')
    ax1.set_ylabel('Membrane Potential (mV)')
    ax1.legend()

    ax2 = fig.add_subplot(gs[1, 0])
    ax2.eventplot(spikes, color='black')
    ax2.set_ylabel('Spike Train')
    ax2.set_xlim(np.min(time), np.max(time))

    ax3 = fig.add_subplot(gs[2, 0])
    im = ax3.imshow(activity_matrix, aspect='auto', origin='lower', cmap='viridis', interpolation='none')
    fig.colorbar(im, ax=ax3, orientation='vertical', label='Activity Level')
    ax3.set_xlabel('Time (ms)')
    ax3.set_ylabel('Neuron Index')

    plt.show()

def plot_raster(spikes, title="Raster Plot of Neuronal Spikes"):
    """Generate a raster plot for neuronal spikes.
    
    Parameters:
    - spikes: Dictionary or list containing spike times for each neuron.
    - title: Title of the plot.
    """
    plt.figure(figsize=(12, 6))
    for neuron_id, spike_times in enumerate(spikes):
        plt.scatter(spike_times, [neuron_id] * len(spike_times), s=10, marker='|')
    plt.title(title)
    plt.xlabel('Time (ms)')
    plt.ylabel('Neuron ID')
    plt.show()

def plot_frequency_spectrum(signal, sampling_rate, title="Frequency Spectrum"):
    """Plot the frequency spectrum of a signal.
    
    Parameters:
    - signal: The neural signal (e.g., membrane potential) array.
    - sampling_rate: Sampling rate of the signal in Hz.
    - title: Title of the plot.
    """
    plt.figure(figsize=(12, 6))
    freqs, psd = signal.welch(signal, sampling_rate)
    plt.semilogy(freqs, psd)
    plt.title(title)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power Spectral Density')
    plt.xlim([0, freqs.max()])
    plt.show()

def plot_synaptic_weights_over_time(weights, title="Synaptic Weight Changes"):
    """Visualize changes in synaptic weights over time.
    
    Parameters:
    - weights: A 2D numpy array or list of lists where each row represents weight changes over time for a synapse.
    - title: Title of the plot.
    """
    plt.figure(figsize=(12, 6))
    for synapse_weights in weights:
        plt.plot(synapse_weights)
    plt.title(title)
    plt.xlabel('Time (Arbitrary Units)')
    plt.ylabel('Synaptic Weight')
    plt.show()

def heatmap_neuronal_feature_encoding(feature_responses, feature_labels, neuron_labels, title="Neuronal Feature Encoding"):
    """Generate a heatmap showing how neurons respond to different features.
    
    Parameters:
    - feature_responses: A 2D numpy array where each row represents a neuron, and each column a feature response.
    - feature_labels: List of names/labels for each feature.
    - neuron_labels: List of neuron identifiers.
    - title: Title of the heatmap.
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    cax = ax.matshow(feature_responses, interpolation='nearest', cmap='viridis')
    fig.colorbar(cax)
    
    ax.set_xticklabels([''] + feature_labels, rotation=90)
    ax.set_yticklabels([''] + neuron_labels)
    
    plt.title(title)
    plt.xlabel('Feature')
    plt.ylabel('Neuron')
    plt.show()

