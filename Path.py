from matplotlib import pyplot as plt
from random import random, sample, randint

class Path:
    def __init__(self, points, state = None):
        self.N = len(points)
        self.points = points
        if state:
            self.state = state
        else:
            self.state = sample(list(range(self.N)), self.N)

    def plot(self, **kwargs):
        x = [self.points[i][0] for i in self.state] + [self.points[self.state[0]][0]]
        y = [self.points[i][1] for i in self.state] + [self.points[self.state[0]][1]]
        plt.plot(x, y, marker = 'x', **kwargs)

    def mutate(self):
        u = sorted(sample(range(self.N), 2))
        new_state = self.state[:u[0]] + [self.state[i] for i in list(range(u[1], u[0] - 1, -1))] + self.state[u[1] + 1:]
        assert len(new_state) == len(self.state)
        return Path(points = self.points, state = new_state)

    def recombine(self, other):
        adjacency_self = {self.state[i] : [self.state[(i+self.N-1)%self.N], self.state[(i + 1)%self.N]] for i in range(self.N)}
        adjacency_other = {other.state[i]: [other.state[(i + other.N - 1) % other.N], other.state[(i + 1) % other.N]] for i in
                          range(other.N)}
        adjacency = {}
        for i in range(self.N):
            adjacency[i] = set(adjacency_self.get(i) + adjacency_other.get(i))

        child_state = [randint(0, self.N - 1)]
        for i in range(self.N-1):
            adjacent_points = adjacency.pop(child_state[-1])
            if not adjacent_points:
                child_state.extend([x for x in range(self.N) if x not in child_state])
                break
            for key in adjacency:
                if child_state[-1] in adjacency[key]:
                    adjacency[key].remove(child_state[-1])
            min_adjacent_points = min(len(adjacency.get(k)) for k in adjacent_points)

            for j in sample(adjacent_points, len(adjacent_points)):
                if len(adjacency.get(j)) == min_adjacent_points:
                    child_state.append(j)
                    break
        assert len(child_state) == len(self.state)
        return Path(points = self.points, state = child_state)