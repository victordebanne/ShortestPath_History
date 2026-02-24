"""
Evolution vers Dijkstra avec un tas binaire
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
        self.visited = False
        
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
            
        #---HEAP---
        self.heap = []
        self.heapsize = 0
        
    def add(self, node):
        self.heap.append(node)
        self.heapsize += 1
        if self.heapsize != 1 : 
            i = self.heapsize - 1
            changed = True 
            while changed : 
                changed = False
                #si on est à la racine
                if i == 0 : 
                    break
                if self.heap[(i-1) >> 1].dist_to_B > self.heap[i].dist_to_B : 
                    #swap
                    self.heap[(i-1) >> 1], self.heap[i] = self.heap[i], self.heap[(i-1) >> 1]
                    #on passe au parent
                    i = ((i-1) >> 1)
                    changed = True
 
    def remove(self):
        if self.heapsize > 0 : 
            self.heap[0] = self.heap[-1]
            self.heap.pop(-1)
            self.heapsize -= 1
            i = 0
            changed = True 
            while changed : 
                changed = False
                #si on est aux feuilles
                left = 2 * i + 1
                right = 2 * i + 2
                smallest_child = left
                if right > self.heapsize - 1 : 
                    break
                if self.heapsize > right : 
                    if self.heap[left].dist_to_B > self.heap[right].dist_to_B : 
                        smallest_child = right
    
                if self.heap[smallest_child].dist_to_B < self.heap[i].dist_to_B : 
                    #swap
                    self.heap[smallest_child], self.heap[i] = self.heap[i], self.heap[smallest_child]
                    #on passe à l'enfant
                    i = smallest_child
                    changed = True
        
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
        #evolution avec exploration à partir de B 
        #on remonte jusqu'a A
        self.nodes[0].dist_to_B = 0
        self.add(self.nodes[0])
        while self.heap != [] : 
            current = self.heap[0]
            self.remove()
            #si un node est visité alors nous avons trouvé le plus court chemin jusqu'a lui
            #étant donné que le chemin de A vers B est une comninaison linéaire avec des poids de R+
            #des distances des nodes déjà visité 
            #si nous visitons B, alors c'est que nous avins pris le plus court chemin
            if current.visited : 
                continue 
            else : 
                for i in range(len(current.links)):
                    self.ops += 1
                    #on modifie si besoin la distance à l'arrivée
                    dist_to_neighbor = current.dists[i] 
                    neighbor_to_B = current.links[i].dist_to_B
                    current_to_B = current.dist_to_B 
                    
                    if dist_to_neighbor + current_to_B < neighbor_to_B :
                        current.links[i].dist_to_B = dist_to_neighbor + current_to_B
                        self.add(current.links[i])
            current.visited = True
            #on enlève le node de la to_do_list et on passe au suivant
            
        #on fait une descente de gardient depuis le départ   
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







