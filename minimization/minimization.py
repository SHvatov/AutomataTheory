class FiniteStateMachine:
    possible_fsa_keys = {'Q', 'A', 'T', 'S', 'F'}

    def __init__(self, Q, A, T, S, F):
        super(FiniteStateMachine, self).__setattr__('fsa', {key: None for key in FiniteStateMachine.possible_fsa_keys})
        self.fsa['Q'], self.fsa['A'], self.fsa['T'], self.fsa['S'], self.fsa['F'] \
            = Q, A, T, S, F

    def __getattr__(self, item):
        if item in FiniteStateMachine.possible_fsa_keys:
            return self.fsa[item]

    def __setattr__(self, key, value):
        if key in FiniteStateMachine.possible_fsa_keys:
            self.fsa[key] = value

    def reverse(self):
        rfsa = FiniteStateMachine(list(self.Q), list(self.A), [], list(self.F), list(self.S))
        rfsa.T = [[[] for i in range(0, len(self.A))] for j in range(0, len(self.Q))]
        for state in range(0, len(self.Q)):
            for value in range(0, len(self.A)):
                for transition_state in self.T[state][value]:
                    rfsa.T[transition_state][value].append(state)
        return rfsa

    def determine(self):
        def reachable(q, l):
            reachable_states = []
            for value in range(0, len(self.A)):
                ts = set()
                for i in q[l]:
                    ts |= set(self.T[i][value])
                if not ts:
                    reachable_states.append([])
                    continue
                try:
                    i = q.index(ts)
                except ValueError:
                    i = len(q)
                    q.append(ts)
                reachable_states.append([i])
            return reachable_states

        dfsa = FiniteStateMachine([], list(self.A), [], [0], [])

        states = [set(self.S)]
        while len(dfsa.T) < len(states):
            dfsa.T.append(reachable(states, len(dfsa.T)))

        dfsa.Q = range(0, len(states))
        dfsa.F = [states.index(i) for i in states if set(self.F) & i]

        return dfsa

    def minimize(self):
        return self.reverse().determine().reverse().determine()

    def save(self, filename):
        file = open(filename, 'w')
        file.write('digraph fa {\nrankdir=LR;\nnode[shape=doublecircle];')

        for i in self.F:
            file.write('"' + str(self.Q[i]) + '";')
        file.write('\nnode[shape=circle];\n')

        for state in range(0, len(self.Q)):
            for value in range(0, len(self.A)):
                for transition_state in self.T[state][value]:
                    file.write('"' + str(self.Q[state]) + '"' + '->' + '"' + \
                               str(self.Q[transition_state]) + '"')
                    file.write('[label="' + str(self.A[value]) + '"];\n')

        file.write('}\n')
        file.close()


if __name__ == '__main__':
    f = FiniteStateMachine([0, 1, 2, 3], ['a', 'b'], [[[1, 2], [2]], [[2], [3]], [[1, 2], [3]], [[], []]], [0], [3])
    f.minimize().save("test.gv")
