"""
Solutions to module 4
Review date:
"""

student = "Yashaswi Sood"
reviewer = ""

import math as m
import random as r


def squarer(cnought):
    temp = 0
    for i in cnought:
        temp+=i**2
    #Returns for one point
    return temp

def sphere_volume(n, d):
    #Generating random points
    coords = [[r.uniform(-1, 1) for i in range(d)] for j in range(n)]
    #Obtaining norm of coords
    normlist = map(squarer, coords)
    #To check if inside hypersphere
    insph = lambda x: x if x <=1 else None
    #Return coords that fall inside the hypersphere
    hs = list(filter(insph, normlist))  
    #Calculating volume
    net = (2*1)**d
    covered = len(hs)/n
    return net*covered   

def hypersphere_exact(n,d):
    return (m.pi**(d/2))/(m.gamma((d/2)+1))*(1**d) #Since, r = 1
    
def main():
    #Inputs
    n = [100000, 100000]
    d = [2, 11]
    #Radius of sphere
    rad = [1,1]
    inp = zip(n,d,rad)

    for i in inp:
        volume = sphere_volume(i[0], i[1])
        print(f"Volume of hypersphere is approximated as: {volume} units")
        print(f"Actual volume of hypersphere is: {hypersphere_exact(i[0], i[1])}")

if __name__ == '__main__':
	main()