import ParticleSwarm as ps

# köşe koordinatları
a: float = 0
b: float = 4
c: float = 4.4723317897697
d: float = 0

def problem1(X):
    global a, b, c, d
    
    x1 = (-b * c + c * d + a * d + b * d) / (X[0] * a - X[0] * c - b + d)
    y1 = X[0] * x1

    x2 = (c * (d - b) + d * (a - c)) / (X[1] * a - X[1] * c + d - b)
    y2 = X[1] * x2
    
    s = abs(a * d - b * c) / 2
    s1  = abs(a * y1 - b * x1) / 2
    s2 = abs(x1 * y2 - x2 * y1) / 2
    s3 = abs(d * x2 - c * y2) / 2

    return abs(s1 - s / 3) + abs(s2 - s / 3) + abs(s3 - s / 3)

dimensions=2
dimension_bounds=[-6,6]
bounds=[0]*dimensions #creating 5 dimensional bounds
for i in range(dimensions):
    bounds[i]=dimension_bounds

#creates bounds [[x1,x2],[x3,x4],[x5,x6]....]    
    
p=60 #shouldn't really change 
vmax=(dimension_bounds[1]-dimension_bounds[0])*0.75
c1=2.8 #shouldn't really change
c2=1.3 #shouldn't really change
tol=0.00000000000001

ps.particleswarm(problem1, bounds,p,c1,c2,vmax,tol)