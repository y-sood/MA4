import random as r
itr = 0 
n = 100
x_sqr, y_sqr = [], []
while itr <= n:    
    x_sqr.append(r.uniform(-1, 1))
    y_sqr.append(r.uniform(-1, 1))
    itr+=1
square = zip(x_sqr, y_sqr)
x_cir, y_cir = [],[]
radii = lambda a,b: a**2+b**2
circle = []
for i in square:
        if radii(i[0], i[1]) <= 1:
            circle.append(i)    
       