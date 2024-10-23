
"""
Solutions to module 4
Review date:
"""

student = "Yashaswi Sood"
reviewer = ""

import math as m
import random as r
import concurrent.futures as futures
import time
import numpy

#To check if inside hypersphere
insph = lambda x: x if x <=1 else None

def squarer(cnought):
    #Returns for one point
    return sum(i**2 for i in cnought)

def sphere_volume(n, d): 
    #Generating random points
    coords = [[r.uniform(-1, 1) for i in range(d)] for j in range(n)]
    #Obtaining norm of coords
    normlist = map(squarer, coords)
    #Return coords that fall inside the hypersphere
    hs = list(filter(insph, normlist))  
    #Calculating volume
    net = (2)**d
    covered = len(hs)/n
    return net*covered   

def hypersphere_exact(n,d):
    return (m.pi**(d/2))/(m.gamma((d/2)+1))*(1**d) #Since, r = 1

# parallel code - parallelize for loop
def sphere_volume_parallel1(n, d, np):
    nitr = [n for _ in range(np)]
    ditr = [d for _ in range(np)]
    #using multiprocessor to perform 10 iterations of volume function 
    with futures.ProcessPoolExecutor() as ex:
        results = list(ex.map(sphere_volume, nitr, ditr))
    return numpy.mean(results)

def parallel2inner(coords):
    normlist = map(squarer, coords)
    hs = list(filter(insph, normlist)) 
    return hs

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
    #Creating random coordinates
    coords = [[r.uniform(-1, 1) for i in range(d)] for j in range(n)]
    #Splitting into 10 parts
    splitted = numpy.array_split(coords, np)
    #Running squaring program in parallel
    with futures.ProcessPoolExecutor() as ex:
        resu = list(ex.map(parallel2inner,splitted))
    #Combine lists
    combo = [item for sublist in resu for item in sublist]
    return (len(combo)/n)*((2*1)**d)

def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11
    #Without parallelisation
    start_np = time.perf_counter()
    a = []
    for y in range (10):
        a.append(sphere_volume(n, d))
    print(f"Serial processing: {numpy.mean(a)}")
    end_np = time.perf_counter()
    #With parallelisation - Part : 1
    start_p = time.perf_counter()
    print(f"Parallel processing 1: {(sphere_volume_parallel1(n, d, 10))}")
    end_p = time.perf_counter()
    #Result
    print(f"Time without parallelisation is {round(end_np-start_np, 2)}, and time with parallelisation is {round(end_p-start_p, 2)}.")
    #Implementing splitting of data parallelisation
    start_p2 = time.perf_counter()
    print(f"Parallel processing 2: {(sphere_volume_parallel2(n, d, 10))}")
    end_p2 = time.perf_counter()
    print(f"Time taken for Data Split Parallel : {round(end_p2-start_p2, 2)}")

if __name__ == '__main__':
	main()
