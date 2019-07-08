from random import random, choice
from Path import Path


class TravellingSalesmanProblem:
    def __init__(self, N=10, pop_size=10, points = None):
        self.N = N
        if points:
            self.points = points
            self.N=len(points)
        else:
            self.points = [(random(), random()) for i in range(self.N)]
        self.paths = [Path(self.points) for i in range(pop_size)]
        self.distances = [[self.dist(self.points[i], self.points[j]) for j in range(self.N)] for i in range(self.N)]

    def fitness(self, path):
        return -sum(self.distances[path.state[i - 1]][path.state[i]] for i in range(self.N))

    def next_generation(self):
        candidates = self.paths + \
                     [choice(self.paths).recombine(choice(self.paths)) for i in range(len(self.paths))] + \
                     [choice(self.paths).mutate() for i in range(3 * len(self.paths))]
        candidates = sorted(candidates, key=self.fitness, reverse=True)
        self.paths = candidates[:len(self.paths)]

    def get_fittest(self):
        return sorted(self.paths, key=self.fitness, reverse=True)[0]

    @staticmethod
    def dist(point_a, point_b):
        dx = point_a[0] - point_b[0]
        dy = point_a[1] - point_b[1]
        return (dx ** 2 + dy ** 2) ** 0.5