#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 17:43:24 2026

@author: victordebanne
"""


class BinaryHeap():
    def __init__(self):
        self.heap = []
        self.size = 0
        #parent de i est (i-1) >> 1
        #enfant de i est (i-1) << 1
        
    def add(self, key, data):
        self.heap.append((key, data))
        self.size += 1
        if self.size != 1 : 
            i = self.size - 1
            changed = True 
            while changed : 
                changed = False
                #si on est à la racine
                if i == 0 : 
                    break
                if self.heap[(i-1) >> 1][0] > self.heap[i][0] : 
                    #swap
                    self.heap[(i-1) >> 1], self.heap[i] = self.heap[i], self.heap[(i-1) >> 1]
                    #on passe au parent
                    i = ((i-1) >> 1)
                    changed = True
                               
    def remove(self):
        if self.size > 0 : 
            self.heap[0] = self.heap[-1]
            self.heap.pop(-1)
            self.size -= 1
            i = 0
            changed = True 
            while changed : 
                changed = False
                left = 2 * i + 1
                right = 2 * i + 2
                smallest_child = left
                if right > self.heapsize - 1 : 
                    break
                if self.size > right : 
                    if self.heap[left][0] > self.heap[right][0] : 
                        smallest_child = right
    
                if self.heap[smallest_child][0] < self.heap[i][0] : 
                    #swap
                    self.heap[smallest_child], self.heap[i] = self.heap[i], self.heap[smallest_child]
                    #on passe à l'enfant
                    i = smallest_child
                    changed = True
            
        
    
if __name__ == "__main__":
    heap = BinaryHeap()
    heap.add(1, "bonjour")
    heap.add(4, "au revoir")
    heap.add(2, "ça va")
    heap.add(3, "et toi")
    
    print(heap.heap)
    
    


        
        
        