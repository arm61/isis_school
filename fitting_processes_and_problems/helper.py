import numpy as np

def mutation(p, b, km):
    m = np.zeros_like(p)
    R = np.random.randint(p.shape[1], size=(2, p.shape[1]))
    for j in range(p.shape[1]):
        m[:, j] = b + km * (p[:, R[0, j]] - p[:, R[1, j]])
    return m


def recombination(p, m, kr):
    o = np.array(p)
    rand = np.random.rand(p.shape[0], p.shape[1])
    o[rand < kr] = m[rand < kr]
    return o


def selection(p, o, f):
    new_p = np.array(p)
    for j in range(p.shape[1]):
        p_fom = f(p[:, j])
        o_fom = f(o[:, j])
        if o_fom < p_fom:
            new_p[:, j] = o[:, j]
    return new_p


def differential_evolution(f, bounds, km=0.5, kr=0.5, max_iter=100, popsize=8):
    population = np.zeros((len(bounds), 8))
    for j in range(len(bounds)):
        population[j] = np.random.uniform(*bounds[j], 8)
    history = population
    best = population[:, np.argmin(f(population.T))]
    i = 0
    while i < max_iter:
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