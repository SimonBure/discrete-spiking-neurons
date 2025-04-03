

class Neuron:
    membrane_potential: int
    is_synapse_activated: bool

    def __init__(self, membrane_potential: int, synapse_activation: bool):
        self.membrane_potential = membrane_potential
        self.is_synapse_activated = synapse_activation

    def __repr__(self):
        activated_str = "Active" if self.is_synapse_activated else "Inactive"
        return f"{activated_str} neuron with membrane potential = {self.membrane_potential}."

    def deactivate(self):
        self.is_synapse_activated = False

    def can_spike(self, spike_threshold: int) -> bool:
        return self.membrane_potential == spike_threshold

    def spike(self):
        self.membrane_potential = 0
        if not self.is_synapse_activated:
            self.is_synapse_activated = True


if __name__ == "__main__":
    pass
