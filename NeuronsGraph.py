import random
import networkx as nx
import matplotlib.pyplot as plt
from Neuron import Neuron


class NeuronsGraph:
    size: int
    neurons: list[Neuron]
    graph: nx.Graph
    edge_probability: float

    def __init__(self, size: int, initial_membranes_potentials: list[int], initial_synapses_activations: list[bool],
                 edge_probability: float):
        self.size = size
        self.edge_probability = edge_probability

        neurons_id = range(0, size)
        self.neurons = [Neuron(i, p, a) for i, p, a  in zip(neurons_id, initial_membranes_potentials, initial_synapses_activations)]

        self.graph = nx.erdos_renyi_graph(size, edge_probability, directed=True)

        # Fill the graph with neurons
        for neuron, node in zip(self.neurons, self.graph.nodes):
            self.graph.nodes[node]['label'] = {neuron.id: neuron.membrane_potential}
            self.graph.nodes[node]['neuron'] = neuron

    def __getitem__(self, index: int) -> Neuron:
        return self.neurons[index]

    def __repr__(self):
        s = ""
        for node in self.graph.nodes():
            neuron = self.graph.nodes[node]['neuron']
            s += str(neuron) + "\n"
        return s

    def draw(self):
        labels = {i: (i, pot) for (i, pot) in enumerate(self.get_potentials())}
        pos = nx.spring_layout(self.graph)
        colors = ['limegreen' if n.is_synapse_activated else 'tomato' for n in self.neurons]
        nx.draw(self.graph, pos, with_labels=True, labels=labels, font_color='black', node_color=colors,
                node_size=500, edge_color='black', arrows=True)
        plt.show()

    def index(self, neuron: Neuron) -> int:
        return neuron.get_id()

    def get_neuron_postsynaptic_neurons(self, neuron: Neuron) -> list[Neuron]:
        neuron_index = self.index(neuron)
        return list(self.graph.successors(neuron_index))

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
    random.seed(0)
    n_neurons = 5
    theta = 3
    initial_membrane_potential = [random.randint(0, theta) for _ in range(n_neurons)]
    initial_synapses_activation = [bool(random.randint(0, 1)) for _ in range(n_neurons)]
    graph = NeuronsGraph(n_neurons, initial_membrane_potential, initial_synapses_activation, 1)

    for neuron in graph:
        print(f"Neuron {neuron.id} postsynaptic neighbours indexes: {graph.get_neuron_postsynaptic_neurons(neuron)}")

    print(graph)

    graph.draw()

