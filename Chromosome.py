from random import randint, getrandbits, random

class Chromosome:
    def __init__(self, data = None, length = 10):
        if data:
            self.data = data
        else:
            self.data = [randint(0,1) for i in range(length)]

    def recombine(self, other):
        new_data = [self.data[i] if bool(getrandbits(1)) else other.data[i] for i in range(len(other.data))]
        return Chromosome(new_data)

    def mutate(self, rate = 0.01):
        self.data = [(x+1)%2 if random() < rate else x for x in self.data]

    def get_fitness(self):
        return sum(self.data)

    def __repr__(self):
        return str(self.data)


def inspect_chromosome():
    chromy = Chromosome()
    chromo = Chromosome()
    print("Initialised Chromosomes:")
    print(chromy, chromo)
    print("After Recombination:")
    chromex = chromy.recombine(chromo)
    print(chromex)
    print("After 15 Mutations E[n_mut] = 1.5:")
    for i in range(15):
        chromex.mutate()
        print(chromex)

if __name__=='__main__':
    inspect_chromosome()