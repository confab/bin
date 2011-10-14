#!/usr/bin/env python
# -*- coding: utf-8 -*-



from random import choice, random
    
bins = ['00', '01', '10', '11']
vals = ['-', 'A', 'B', 'C']
    
def decode(chromo):
    return ''.join(vals[bins.index(chromo[i:i+2])] for i in range(0, len(chromo), 2))
    
def fitness(decd):
    #return max((2*decd.count('A'))+(3*decd.count('B'))+(4*decd.count('C')), 1)
    a = decd.count('A')
    b = decd.count('B')
    c = decd.count('C')
    try: return (a*b)/c
    except ZeroDivisionError: return a*b

def fitness_list(chromos):
    return [[i, fitness(decode(i))] for i in chromos]

def selection(fitness_list, xover=0.7, mutate=0.01):
    total_fitness = sum([i[1] for i in fitness_list])
    pool = []
    for i in fitness_list:
        pool += [i[0]] * int((i[1]/total_fitness)*100)
    new_pop = []
    while len(new_pop) < len(fitness_list):
        chosen = [choice(pool), choice(pool)]
        # Crossover
        if random() < xover:
            x_point = int(random() * len(chosen[0])) + 1
            chosen = [chosen[0][:x_point] + chosen[1][x_point:], chosen[1][:x_point] + chosen[0][x_point:]]
        # Mutate
        for i in [0, 1]:
            for j in range(len(chosen[i])):
                if random() < mutate:
                    chosen[i] = chosen[i][:j] + '10'.strip(chosen[i][j]) + chosen[i][j+1:]
        new_pop += chosen
    return new_pop

def initiate(length=64, size=35):
    pop = []
    while len(pop) < size:
        chromo = ''
        for i in range(length):
            chromo += choice(bins)
        pop.append(chromo)
    return pop

def main():
    pop = initiate()
    gen = 0
    while True:
        gen += 1
        fit = sum([i[1] for i in fitness_list(pop)])
        print('Generation:', gen)
        print('Total fitness:', fit)
        for i in pop:
            print(decode(i))
        input()
        pop = selection(fitness_list(pop))
        
if __name__ == '__main__':
	main()

