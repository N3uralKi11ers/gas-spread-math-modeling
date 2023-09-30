from typing import List
from models import Gas, EvacuationMap
import time


def update_gas_filling(gas: Gas, evaluation_map: EvacuationMap, num_iters: int, diagonal_spread: bool = False):
    
    def pprint(mat):
        for i in mat:
            print(i)
    
    def get_neighbours(x, y):
        res = []
        neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        
        if diagonal_spread:
            neighbours += [(x+1, y+1), (x-1, y+1), (x+1, y-1), (x-1, y-1)]
        
        for xx, yy in neighbours:
            if 0 <= xx < len(evaluation_map.ev_map[0]) and 0 <= yy < len(evaluation_map.ev_map) and evaluation_map.ev_map[yy][xx] == 0:
                res.append((xx, yy))
        return res
    
    queue = [(gas.pos.x, gas.pos.y)]
    
    for _ in range(num_iters):
        for _ in range(len(queue)):
            first_el = queue.pop(0)
            evaluation_map.ev_map[first_el[1]][first_el[0]] = 3
            queue += get_neighbours(first_el[0], first_el[1])
        
        # print(evaluation_map.ev_map)
        pprint(evaluation_map.ev_map)
        print()
        time.sleep(1.0)

    