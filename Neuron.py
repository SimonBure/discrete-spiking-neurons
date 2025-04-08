
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

    def get_id(self) -> int:
        return self.id

    def get_membrane_potential(self) -> float:
        return self.membrane_potential

    def activate(self):
        self.is_synapse_activated = True

    def deactivate(self):
        self.is_synapse_activated = False

    def can_spike(self, spike_threshold: int) -> bool:
        return self.membrane_potential == spike_threshold

    def reset_membrane_potential(self):
        self.membrane_potential = 0

    def increase_membrane_potential(self, spike_threshold: int):
        self.membrane_potential = min(self.membrane_potential + 1, spike_threshold)


if __name__ == "__main__":
    pass
