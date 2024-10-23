"""
Solutions to module 4
Review date:
"""

student = "Yashaswi Sood"
reviewer = ""

import random as r
import matplotlib.pyplot as plt 
import numpy as np

def approximate_pi(n):
    #Square of size 2,2 centred at (0,0)
    #Generating points inside square
    square, itr = [], 0
    while itr<=n:    
        square.append([r.uniform(-1, 1), r.uniform(-1, 1)])
        itr+=1   
    #If inside circle equation of circle is obeyed
    #Filtering points inside circle
    circle, not_circle = [], []
    radii = lambda a,b: a**2+b**2
    for i in square:
            if radii(i[0], i[1]) <= 1:
                circle.append(i)
            else:
                not_circle.append(i)
    #Estimating pi by dividing areas:
    pi = 4*(len(circle)/n)
    #Plot
    plot(circle, not_circle, n)
    return pi

#Plotting results
def plot(a, b, n):
    cir_x, cir_y = zip(*a)
    ncir_x, ncir_y = zip(*b)
    plt.scatter(cir_x, cir_y, color='red', label='Circle', s = 1)
    plt.scatter(ncir_x, ncir_y, color='blue', label='Square', s = 1)
    plt.title('Circle and Square points')
    plt.savefig(f"plot{n}.png")

#MAIN
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        estpi = approximate_pi(n)
        print(f"For n={n}, The estimation of pi is {estpi}.")

if __name__ == '__main__':
	main()
