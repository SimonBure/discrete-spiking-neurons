from random import random


class Neuron:
    id: int
    membrane_potential: int
    is_synapse_activated: bool
    postsynaptic_neurons: list

    def __init__(self, id: int, membrane_potential: int, synapse_activation: bool):
        self.id = id
        self.membrane_potential = membrane_potential
        self.is_synapse_activated = synapse_activation

    def __repr__(self):
        activated_str = "active" if self.is_synapse_activated else "Inactive"
        return f"Neuron {self.id} is {activated_str} with membrane potential = {self.membrane_potential}."

    @staticmethod
    def is_spiking(spike_proba: float) -> bool:
        return random() < spike_proba

    @staticmethod
    def is_deactivating(deactivation_proba: float) -> bool:
        return random() < deactivation_proba

    def get_id(self) -> int:
        return self.id

    def get_membrane_potential(self) -> float:
        return self.membrane_potential

    def deactivate(self):
        self.is_synapse_activated = False

    def can_spike(self, spike_threshold: int) -> bool:
        return self.membrane_potential == spike_threshold

    def spike(self):
        self.membrane_potential = 0


if __name__ == "__main__":
    pass
