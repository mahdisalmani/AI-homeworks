import random, re
import numpy as np
from math import exp
import matplotlib.pyplot as plt

global dna_length
dna_length = int(input())
population_size = int(input())
iteration = int(input())

global nucleotide
nucleotide = {x for x in input().split()}

global constraints
constraints = []
while True:
    line = input()
    if not line:
        break
    constraints.append([line.split()[0], int(line.split()[1])])

def generate_random_dna():
    generated_dna = []
    for counter in range(dna_length):
        generated_dna += random.sample(nucleotide, 1)
    
    return "".join(generated_dna)

#population = [generate_random_dna() for x in range(population_size)]

def calculate_fitness(dna):
    fitness = 0 
    for constraint in constraints:
        fitness += len(re.findall(constraint[0], dna)) * constraint[1]
    return fitness

def calculate_probability(scores):
    # ans = [0] * len(scores)
    ans = []
    min_score = min(scores)
    temp = list(map(lambda x: (x - min_score + 1)**2,scores))
    sum_total = sum(temp)
    for score in temp:
        ans.append(score / sum_total)
    # total_prob = ((len(scores) + 1) * len(scores)) / 2
    # temp = [[x, scores[x]] for x in range(len(scores))]
    # temp.sort(key= lambda x: x[1])
    # for counter in range(len(scores)):
    #     ans[temp[counter][0]] = (counter + 1) / total_prob
    return ans

def selection(population):
    scores = list(map(calculate_fitness, population))
    probability = calculate_probability(scores)
    new_population = list(np.random.choice(population, population_size, p=probability))
    return new_population

def mutation(population):
    new_population = []
    for index in range(population_size):
        if np.random.choice([True, False], 1, [0.3, 0.7])[0]: #person is selected
            random_index = random.randint(0, dna_length - 1)
            new_population.append(population[index][:random_index] + (random.sample(nucleotide, 1)).pop()  
                            + population[index][random_index + 1:])
        else:
            new_population.append(population[index])
    return new_population

def cross_over(population):
    new_population = []
    for index in range(0, population_size, 2):
        second_index = (index + 2) % population_size
        pivot = random.randint(0, population_size - 1)
        new_population.append(population[index][:pivot] + population[second_index][pivot:])
        new_population.append(population[second_index][:pivot] + population[index][pivot:])
    return new_population

def genetic_algorithm():
    population = [generate_random_dna() for x in range(population_size)]
    history = []
    for counter in range(iteration):
        population = mutation(cross_over(selection(population)))
        history.append(max(list(map(calculate_fitness, population))))
    return history, population

history, population = genetic_algorithm()
best = history[-1]
print(best)
for person in population:
    if calculate_fitness(person) == best:
        print(person)
        break
plt.plot(range(0, len(history)), history)
plt.show()
