import random
import math
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import time
from NeuronsGraph import NeuronsGraph


def plot_potentials_ts(potentials_ts: list[list[int]], spike_threshold: int):
    potentials_ts = np.array(potentials_ts)

    n_series = potentials_ts.shape[1]

    fig, axes = plt.subplots(n_series, 1, figsize=(15, 2 * n_series), sharex=True)

    time_steps = np.arange(len(potentials_ts))
    # ylim=(0, spike_threshold)
    for i in range(n_series):
        axes[i].plot(time_steps, potentials_ts[:, i], label=f'Neurone {i + 1}')
        axes[i].legend()
        axes[i].grid(True)

    for ax in axes:
        ax.set_ylim(0, spike_threshold+0.3)  # Set y-axis limits
        ax.tick_params(axis='both', labelsize=14)  # Increase tick label font size

    plt.xlabel("Temps", fontsize=16)

    plt.tight_layout()

    plt.show()


if __name__ == '__main__':
    random.seed(1)

    N_NEURONS = 5
    N_ITERATIONS = 100

    EDGE_PROBABILITY = 1.0
    SPIKE_THRESHOLD = 3  # theta

    # Sum of following probabilities must be less than 1
    SPIKE_PROBA = 0.3  # beta
    DEACTIVATION_PROBA = 0.1  # lambda

    initial_membrane_potential = [random.randint(0, SPIKE_THRESHOLD) for _ in range(N_NEURONS)]
    initial_synapses_activation = [bool(random.randint(0, 1)) for _ in range(N_NEURONS)]
    neurons_graph = NeuronsGraph(N_NEURONS, initial_membrane_potential, initial_synapses_activation, EDGE_PROBABILITY)

    cumulated_spikes_nb_ts = [0] * N_ITERATIONS
    spikes = 0

    potentials_ts = [initial_membrane_potential] * N_ITERATIONS
    activations_ts = [initial_synapses_activation] * N_ITERATIONS

    time_before = time.time()

    neurons_graph.draw()

    for i in tqdm(range(1, N_ITERATIONS)):

        for j, n in enumerate(neurons_graph):
            random_float = random.random()
            if random_float < SPIKE_PROBA:
                spikes += 1
                if n.can_spike(SPIKE_THRESHOLD):
                    if n.is_synapse_activated:
                        n.reset_membrane_potential()
                        neurons_graph.propagate_spike(n, SPIKE_THRESHOLD)
                    else:
                        n.activate()
                else:
                    pass
            elif SPIKE_PROBA < random_float < DEACTIVATION_PROBA and n.is_synapse_activated:
                n.deactivate()
            else:
                pass

        cumulated_spikes_nb_ts[i] = spikes
        potentials_ts[i] = neurons_graph.get_potentials()
        activations_ts[i] = neurons_graph.get_synapses_activation()

    time_after = time.time()
    simulation_duration = time_after - time_before
    print(f"Simulation duration = {simulation_duration} sec")

    plot_potentials_ts(potentials_ts, SPIKE_THRESHOLD)
