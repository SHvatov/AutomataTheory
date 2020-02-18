def equivalent(left, right):
    if left.get_alphabet() != right.get_alphabet():
        raise ValueError("Input alphabets must be equal!")

    transitions = []
    previous_states = []
    alphabet = left.get_alphabet()
    states = [(left.get_initial_state(), right.get_initial_state())]

    while len(states) != 0:
        l, r = states.pop()
        previous_states.append((l.name, r.name))

        for value in alphabet:
            next_l, next_r = l.get_next(value), r.get_next(value)
            if (next_l is None and next_r is not None) \
                    or (next_r is None and next_l is not None):
                return False

            if (next_l[0], next_r[0]) not in previous_states:
                transitions.append((next_l[1], next_r[1]))
                states.append((left[next_l[0]], right[next_r[0]]))

    for (l, r) in transitions:
        if l != r:
            return False
    return True
