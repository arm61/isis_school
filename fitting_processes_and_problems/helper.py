import numpy as np
from typing import Tuple

def mutation(p: np.ndarray, b: np.ndarray, km: float) -> np.ndarray:
    """
    :param p: Population vector
    :param b: Best population member
    :param km: Mutation constant
    :returns: Mutant vector
    """
    m = np.zeros_like(p)
    R = np.random.randint(p.shape[1], size=(2, p.shape[1]))
    for j in range(p.shape[1]):
        m[:, j] = b + km * (p[:, R[0, j]] - p[:, R[1, j]])
    return m


def recombination(p: np.ndarray, m: np.ndarray, kr: float) -> np.ndarray:
    """
    :param p: Population vector
    :param m: Mutant member
    :param km: Recombination constant
    :returns: Offspring vector
    """
    o = np.array(p)
    rand = np.random.rand(p.shape[0], p.shape[1])
    o[rand < kr] = m[rand < kr]
    return o


def selection(p: np.ndarray, o: np.ndarray, f: callable) -> np.ndarray:
    """
    :param p: Population vector
    :param o: Offspring vector
    :param f: Objective function
    :returns: New parent population
    """
    new_p = np.array(p)
    for j in range(p.shape[1]):
        p_fom = f(p[:, j])
        o_fom = f(o[:, j])
        if o_fom < p_fom:
            new_p[:, j] = o[:, j]
    return new_p


def differential_evolution(f: callable, bounds: Tuple[Tuple[float]], km: float=0.5, kr: float=0.5, iterations: int=100, popsize: int=8) -> np.ndarray:
    """
    :param f: Objective function
    :param bounds: Min and Max values for parameters
    :param km: Mutation constant
    :param km: Recombination constant
    :param iterations: Number of iterations
    :param popsize: Size of the populations
    :returns: A genelogy for the parameter values
    """
    population = np.zeros((len(bounds), 8))
    for j in range(len(bounds)):
        population[j] = np.random.uniform(*bounds[j], 8)
    history = population
    best = population[:, np.argmin(f(population.T))]
    i = 0
    while i < iterations:
        mutant = mutation(population, best, km)
        offspring = recombination(population, mutant, kr)
        for j in range(len(bounds)):
            offspring[j, np.where(offspring >= bounds[j][1]) 
                      or np.where(offspring < bounds[j][0])] = np.random.uniform(bounds[j][0], bounds[j][1], 1)
        selected = selection(population, offspring, f)
        history = np.append(history, selected)
        history = np.reshape(history, (i + 2, *population.shape))
        population = np.array(selected)
        best = population[:, np.argmin(f(population.T))]
        i += 1
    return history