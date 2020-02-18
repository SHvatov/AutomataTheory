class State:
    def __init__(self, name, initial=False):
        self.name = name
        self.initial = initial
        self.transitions = dict()

    def add_transition(self, value, dst, output):
        self.transitions[value] = (dst, output)

    def get_next(self, value):
        if value in self.transitions.keys():
            return self.transitions[value]
        return None

    def __str__(self):
        output = f"\nState[{self.name}, {self.initial}]:"
        for value, state in self.transitions.items():
            output += f"\n\t{value} -> {state[0]}, {state[1]}"
        return output

    def __eq__(self, other):
        return self.name == other.name \
            and self.transitions == other.transitions \
            and self.initial == other.intial


class Automate:
    def __init__(self, in_alphabet, states, out_func, transition_func, initial_state):
        self.states = []
        self.initial_state = initial_state
        self.alphabet = set(in_alphabet)

        temp_states = [State(name, name == initial_state) for name in set(states)]
        for state in temp_states:
            for value in self.alphabet:
                next_state = transition_func(state.name, value)

                if next_state not in set(states):
                    raise ValueError(f"Next state [{next_state}] was not mentioned in the state list!")

                if next_state is not None:
                    output = out_func(state.name, value)
                    state.add_transition(value, next_state, output)
            self.states.append(state)

    def __getitem__(self, name):
        if name in [s.name for s in self.states]:
            return next(filter(lambda s: s.name == name, self.states))
        return None

    def __str__(self):
        output = "Automate:"
        for state in self.states:
            output += str(state)
        return output

    def get_initial_state(self):
        return next(filter(lambda s: s.initial, self.states))

    def get_states(self):
        return self.states[:]

    def get_alphabet(self):
        return self.alphabet
