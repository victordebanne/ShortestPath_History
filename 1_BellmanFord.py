"""
implementation de l'algorithme de Bellman-Ford à double relaxation
"""

import random as r 
import matplotlib.pyplot as plt

def norm(u, v):
    return ((v[0] - u[0])**2 + (v[1] - u[1])**2)**0.5



class Node():
    def __init__(self, position):
        self.position = position
        self.links = []
        self.dists = []
        self.dist_to_B = 1000
        
class Network():
    def __init__(self, A, B, size):
        self.size = size + 2
        self.nodes = []
        self.nodes = [Node(B), Node(A)]
        self.path = []
        self.ops = 0
        for i in range(size):
            x = r.uniform(0, 10)
            y = r.uniform(0, 10)
            self.nodes.append(Node([x,y]))
            
    def create_graph(self):
        for i in range(self.size - 1):
            for j in range(i + 1, self.size):
                if i == j : 
                    pass
                else : 
                    distance = norm(self.nodes[j].position, self.nodes[i].position)
                    threshold = 3
                    if distance < threshold : 
                        self.nodes[i].links.append(self.nodes[j])
                        self.nodes[j].links.append(self.nodes[i])
                        
                        self.nodes[i].dists.append(distance)
                        self.nodes[j].dists.append(distance)
                
    def find_path(self):
        self.nodes[0].dist_to_B = 0

        changed = True
        while changed : 
            changed = False 
            for i in range(1, self.size):
                for j in range(len(self.nodes[i].links)):
                    self.ops += 1
                    dist_to_neighbor = self.nodes[i].dists[j] 
                    neighbor_to_B = self.nodes[i].links[j].dist_to_B
                    current_to_B = self.nodes[i].dist_to_B 
                    if dist_to_neighbor + neighbor_to_B < current_to_B : 
                        self.nodes[i].dist_to_B = dist_to_neighbor + neighbor_to_B
                        changed = True
                    if dist_to_neighbor + current_to_B < neighbor_to_B :
                        self.nodes[i].links[j].dist_to_B = dist_to_neighbor + current_to_B
                        changed = True
                    
        self.path.append(self.nodes[1])
        while self.path[-1].dist_to_B != 0 : 
            index_min = 0
            for i in range(1, len(self.path[-1].links)):
                
                self.ops += 1
                current = self.path[-1].links[index_min].dist_to_B 
                new = self.path[-1].links[i].dist_to_B
                if new < current :
                    index_min = i 
            if self.path[-1].links[index_min] in self.path : 
                break
            else :
                self.path.append(self.path[-1].links[index_min])
                    
    def display_graph(self):
        for i in range(self.size):
            for j in range(len(self.nodes[i].links)):
                x1 = self.nodes[i].position[0]
                x2 = self.nodes[i].links[j].position[0]
                y1 = self.nodes[i].position[1]
                y2 = self.nodes[i].links[j].position[1]
                x = [x1, x2]
                y = [y1, y2]
                plt.plot(x, y)
        #plt.show()
        
    def display_nodes(self):
        for i in range(self.size):
            plt.scatter(self.nodes[i].position[0], self.nodes[i].position[1])
        plt.show()
        
    def display_path(self):
        for i in range(len(self.path) - 1):
            x1 = self.path[i].position[0]
            x2 = self.path[i + 1].position[0]
            y1 = self.path[i].position[1]
            y2 = self.path[i + 1].position[1]
            x = [x1, x2]
            y = [y1, y2]
            plt.plot(x, y, linewidth = 3, color = 'black')
        plt.show()
        
    
        

A = [0, 0]
B = [10, 10]
N = Network(A, B, 100)
N.display_nodes()
N.create_graph()
N.display_graph()
N.find_path()
N.display_path()
print(N.ops)







