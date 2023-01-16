import random
import time
import matplotlib.pyplot as plt
# ------------------------------------------------------------------------------
a = 6
b = 7
c = 10

def problem2(X):
    global a, b, c
    u = X[0]
    m = X[1]

    x1 = u / (m**2 + 1)
    y1 = m * x1

    x2 = a * u / (a + m * b)
    y2 = b * u / (a + m * b)

    x3 = b * c / (b - m * (a - c))
    y3 = m * x3

    s = b * c / 2
    s1 = (x1 * y3  - x3 * y1) / 2
    s2 = u * y1 / 2
    s3 = abs(c * y2 + x2 * y1 - x1 * y2 - u * y1) / 2
    s4 = abs(a * y3 + x3 * y1 + x1 * y2 + x2 * b - a * y2 - x2 * y1 - x1 * y3 - x3 * b) / 2

    q = s / 4
    return abs(s1 - q) + abs(s2 - q) + abs(s3 - q) + abs(s4 - q)


  
bounds = [(-6,6), (-6,6)]  # upper and lower bounds of variables
nv = 2  # number of variables
mm = -1  # if minimization problem, mm = -1; if maximization problem, mm = 1
  
# PARAMETERS OF PSO
particle_size = 120  # number of particles
iterations = 200  # max number of iterations
w = 0.8  # inertia constant
c1 = 1  # cognative constant
c2 = 2  # social constant
  
# Visualization
fig = plt.figure()
ax = fig.add_subplot()
fig.show()
plt.title('Fonksiyonumuzun değerinin iterasyonla değişimi')
plt.xlabel("İterasyon")
plt.ylabel("Fonksiyonumuz")
# ------------------------------------------------------------------------------
class Particle:
    def __init__(self, bounds):
        self.particle_position = []  # particle position
        self.particle_velocity = []  # particle velocity
        self.local_best_particle_position = []  # best position of the particle
        self.fitness_local_best_particle_position = inital_fitness
        self.fitness_particle_position = inital_fitness
        for i in range(nv):
            self.particle_position.append(random.uniform(bounds[1][0], bounds[i][1]))
            self.particle_velocity.append(random.uniform(-1,1))

    

    def evaluate(self, objective_function):
        self.fitness_particle_position = objective_function(self.particle_position)
        if mm == -1:
            if self.fitness_particle_position < self.fitness_local_best_particle_position:
                self.local_best_particle_position = self.particle_position  # update the local best
                self.fitness_local_best_particle_position = self.fitness_particle_position  # update the fitness of the local best
            if mm == 1:
                if self.fitness_particle_position > self.fitness_local_best_particle_position:
                    self.local_best_particle_position = self.particle_position  # update the local best
                    self.fitness_local_best_particle_position = self.fitness_particle_position  # update the fitness of the local best
  
    def update_velocity(self, global_best_particle_position):
        for i in range(nv):
            r1 = random.random()
            r2 = random.random()
  
            cognitive_velocity = c1 * r1 * (self.local_best_particle_position[i] - self.particle_position[i])
            social_velocity = c2 * r2 * (global_best_particle_position[i] - self.particle_position[i])
            self.particle_velocity[i] = w * self.particle_velocity[i] + cognitive_velocity + social_velocity
  
    def update_position(self, bounds):
        for i in range(nv):
            self.particle_position[i] = self.particle_position[i] + self.particle_velocity[i]
  
            # check and repair to satisfy the upper bounds
            if self.particle_position[i] > bounds[i][1]:
                self.particle_position[i] = bounds[i][1]
            # check and repair to satisfy the lower bounds
            if self.particle_position[i] < bounds[i][0]:
                self.particle_position[i] = bounds[i][0]
  
class PSO:
    def __init__(self, objective_function, bounds, particle_size, iterations):
        fitness_global_best_particle_position = inital_fitness
        global_best_particle_position = []
        swarm_particle = []
        for i in range(particle_size):
            swarm_particle.append(Particle(bounds))
        A = []

        for i in range (iterations):
            for j in range(particle_size):
                swarm_particle[j].evaluate(objective_function)

                if mm == -1:
                    if swarm_particle[j].fitness_particle_position < fitness_global_best_particle_position:
                        global_best_particle_position = list(swarm_particle[j].particle_position)
                        fitness_global_best_particle_position = float(swarm_particle[j].fitness_particle_position)
                if mm == 1:
                    if swarm_particle[j].fitness_particle_position > fitness_global_best_particle_position:
                        global_best_particle_position = list(swarm_particle[j].particle_position)
                        fitness_global_best_particle_position = float(swarm_particle[j].fitness_particle_position)
            for j in range(particle_size):
                swarm_particle[j].update_velocity(global_best_particle_position)
                swarm_particle[j].update_position(bounds)
            A.append(fitness_global_best_particle_position)
            ax.plot(A, color="r")
            fig.canvas.draw()
            ax.set_xlim(left=max(0, i-iterations), right=i+3)
            time.sleep(0.01)
        print("Result:")
        print("Optimal Solution", global_best_particle_position)
        print("Objective function value:", fitness_global_best_particle_position)

if mm == -1:
    inital_fitness = float("inf")

if mm == 1:
    inital_fitness = -float("inf")


PSO(problem2,bounds,particle_size,iterations)
plt.show()