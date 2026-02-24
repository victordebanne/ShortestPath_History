#include <stdio.h>
#include <stdlib.h>

typedef struct{
    int size;
    int* key;
    int* data; //on peut changer le type en fonction des données (exemple noeud pour Dijkstra)
} BinaryHeap;

void init_heap(BinaryHeap* heap, int heap_size){
    heap->size = 0;
    heap->key = malloc(heap_size * sizeof(int));
    heap->data = malloc(heap_size * sizeof(int));
}

void add(BinaryHeap* heap, int key, int data){
    //ajoute au tas un element
    heap->size++;
    heap->key[heap->size - 1] = key;
    heap->data[heap->size - 1] = data;

    if(heap->size != 1){
        int i = heap->size - 1;
        int changed = 1;
        while(changed){
            changed = 0;
            //si on est à la racine
            if(i == 0) break;
            else if (heap->key[(i-1) >> 1] > heap->key[i]){ 
                //swap
                int a = heap->key[(i-1) >> 1];
                int b = heap->key[i];
                heap->key[(i-1) >> 1] = b;
                heap->key[i] = a;
                int c = heap->data[(i-1) >> 1];
                int d = heap->data[i];
                heap->data[(i-1) >> 1] = d;
                heap->data[i] = c;
                //on passe au parent
                i = ((i-1) >> 1);
                changed = 1;
            }
        }
    }
}

void delete(BinaryHeap* heap){
    //enlève le premier element du tas
    if(heap->size > 0){
        heap->key[0] = heap->key[heap->size -1];
        heap->data[0] = heap->data[heap->size -1];
        heap->size--;
        int i = 0;
        int changed = 1;
        while(changed){
            changed = 0;

            int left = 2 * i + 1;
            int right = 2 * i + 2;
            int smallest_child = left;
            if(left > heap->size - 1) break;
            
            if(heap->size > right){ 
                if(heap->key[left] > heap->key[right]){ 
                    smallest_child = right;
                }
            }
            if(heap->key[smallest_child] < heap->key[i]){ 
                //swap
                int a = heap->key[smallest_child];
                int b = heap->key[i];
                heap->key[smallest_child] = b;
                heap->key[i] = a;
                int c = heap->data[smallest_child];
                int d = heap->data[i];
                heap->data[smallest_child] = d;
                heap->data[i] = c;
                //on passe à l'enfant
                i = smallest_child;
                changed = 1;
            }
        }
    }
}

void print_heap(BinaryHeap* heap){

    for(int i = 0; i < heap->size; i++){
        printf("%d ", heap->key[i]);
    }
    printf("\n");
}

int main(){

    BinaryHeap heap;
    init_heap(&heap, 1000);
    add(&heap, 1, 2);
    add(&heap, 4, 1);
    add(&heap, 2, 2);
    add(&heap, 3, 4);
    print_heap(&heap);
    delete(&heap);
    print_heap(&heap);

    return 0;
}