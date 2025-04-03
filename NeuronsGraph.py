import random

from Neuron import Neuron


class NeuronsGraph:
    size: int
    neurons: list[Neuron]

    def __init__(self, size: int, initial_membranes_potentials: list[int], initial_synapses_activations: list[bool]):
        self.size = size
        self.neurons = [Neuron(p, a) for p, a  in zip(initial_membranes_potentials, initial_synapses_activations)]

    def __getitem__(self, index: int) -> Neuron:
        return self.neurons[index]

    def index(self, neuron: Neuron):
        return self.neurons.index(neuron)

    def get_potentials(self) -> list[int]:
        potentials = [0] * self.size
        for i, neuron in enumerate(self.neurons):
            potentials[i] = neuron.membrane_potential

        return potentials

    def get_synapses_activation(self) -> list[bool]:
        synapses_activation = [False] * self.size
        for i, neuron in enumerate(self.neurons):
            synapses_activation[i] = neuron.is_synapse_activated

        return synapses_activation

    def impact_spike(self, spike_threshold: int, n_spikes: int):
        for neuron in self.neurons:
            # The membrane potential cannot be greater than the spike threshold
            neuron.membrane_potential = min(neuron.membrane_potential + n_spikes, spike_threshold)

if __name__ == "__main__":
    n_neurons = 5
    theta = 3
    initial_membrane_potential = [random.randint(0, theta) for _ in range(n_neurons)]
    initial_synapses_activation = [bool(random.randint(0, 1)) for _ in range(n_neurons)]
    graph = NeuronsGraph(n_neurons, initial_membrane_potential, initial_synapses_activation)
    print(graph[0])
    for neuron in graph:
        print(graph.index(neuron))