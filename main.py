import random
import math
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

    spikes_ts = [0] * N_ITERATIONS
    potentials_ts = [0] * N_ITERATIONS
    activations_ts = [0] * N_ITERATIONS

    for i in range(N_ITERATIONS):
        spikes = [0] * N_NEURONS
        for j, n in enumerate(neurons_graph):
            if n.can_spike(SPIKE_THRESHOLD):
                if n.is_spiking(spike_proba):
                    neurons_graph.impact_spike(SPIKE_THRESHOLD)
                    n.spike()
                    spikes[j] = 1
                else:
                    pass
            else:
                pass

            if n.is_deactivating(deactivation_proba):
                n.deactivate()
            else:
                pass

            spikes_ts[i] = spikes
            potentials_ts[i] = neurons_graph.get_potentials()
            activations_ts[i] = neurons_graph.get_synapses_activation()

    print(spikes_ts)
