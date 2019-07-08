import sys
import signal
from Path import Path
from TravellingSalesmanProblem import TravellingSalesmanProblem
from random import random
from time import time
import matplotlib.pyplot as plt
import pandas as pd

def experiment(n):
    t = TravellingSalesmanProblem(N=n, pop_size=20)
    start = time()
    fitnesses = [-99999999]
    gradients = []
    s = 1
    while not s < 0.005:
        t.next_generation()
        fitnesses.append(t.fitness(t.get_fittest()))

        gradient = fitnesses[-1] - fitnesses[-2]
        gradients.append(gradient)
        df = pd.DataFrame(gradients)
        s = df[0].rolling(10).mean().iloc[-1]
    t = time()-start
    print('\nn: {}\nExecution time: {:.2f}s'.format(n,t))
    return t

def signal_handler(signal, frame):
    """
    Handles system interrupts.
    Specifically if the script is terminated [Ctrl + C], the results are saved.
    :param signal:
    :param frame:
    :return:
    """
    print('You pressed Ctrl+C!')
    pd.DataFrame(res, columns=['time']).to_msgpack('complexityRuntimes')
    sys.exit(0)


if __name__=='__main__':
    signal.signal(signal.SIGINT, signal_handler)
    res = []
    begin = time()
    i = 2
    while time()-begin < 5*360:
        res.append(experiment(2 ** i))
        i = i+1
    pd.DataFrame(res, columns=['time']).to_msgpack('complexityRuntimes')
    
