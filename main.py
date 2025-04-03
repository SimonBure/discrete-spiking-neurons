import random
import math
import matplotlib.pyplot as plt
import numpy as np
from NeuronsGraph import NeuronsGraph


def get_proba_from_rate(rate: float, time_interval: float) -> float:
    return math.exp(-rate * time_interval)


if __name__ == '__main__':
    random.seed(0)

    N_NEURONS = 5
    N_ITERATIONS = 100
    TIME_INTERVAL = 0.1
    max_time = N_ITERATIONS * TIME_INTERVAL

    SPIKE_THRESHOLD = 3  # theta
    SPIKE_RATE = 1.  # beta
    DEACTIVATION_RATE = 1.  # lambda
    spike_proba = get_proba_from_rate(SPIKE_RATE, TIME_INTERVAL)
    deactivation_proba = get_proba_from_rate(DEACTIVATION_RATE, TIME_INTERVAL)

    initial_membrane_potential = [random.randint(0, SPIKE_THRESHOLD) for _ in range(N_NEURONS)]
    initial_synapses_activation = [bool(random.randint(0, 1)) for _ in range(N_NEURONS)]
    neurons_graph = NeuronsGraph(N_NEURONS, initial_membrane_potential, initial_synapses_activation)

    spikes_ts = [[0] * N_NEURONS] * N_ITERATIONS
    potentials_ts = [initial_membrane_potential] * N_ITERATIONS
    activations_ts = [initial_synapses_activation] * N_ITERATIONS

    for i in range(1, N_ITERATIONS):
        spikes = [0] * N_NEURONS
        n_spikes = 0
        index_spikes = []
        for j, n in enumerate(neurons_graph):
            if n.can_spike(SPIKE_THRESHOLD):
                if n.is_spiking(spike_proba):
                    if n.is_synapse_activated:
                        n_spikes += 1
                        index_spikes.append(j)
                        spikes[j] = 1
                    else:
                        n.is_synapse_activated = True

            if n.is_deactivating(deactivation_proba):
                n.deactivate()

        neurons_graph.impact_spike(SPIKE_THRESHOLD, n_spikes)

        for j, n in enumerate(neurons_graph):
            if j in index_spikes:
                n.spike()

        spikes_ts[i] = spikes
        potentials_ts[i] = neurons_graph.get_potentials()
        activations_ts[i] = neurons_graph.get_synapses_activation()

    data = np.array(potentials_ts)

    # Nombre de séries temporelles
    n_series = data.shape[1]  # Nombre de colonnes

    fig, axes = plt.subplots(n_series, 1, figsize=(8, 2 * n_series), sharex=True)

    # Tracer chaque série sur un subplot distinct
    time_steps = np.arange(len(data))  # Axe temporel

    for i in range(n_series):
        axes[i].plot(time_steps, data[:, i], label=f'Neurone {i + 1}')
        axes[i].legend()
        axes[i].grid(True)

    # Ajouter un label global pour l'axe des x
    plt.xlabel("Temps")

    # Ajuster l'espacement entre les subplots
    plt.tight_layout()

    # Afficher le graphique
    plt.show()