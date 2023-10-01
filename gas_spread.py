import copy
from typing import List
from models import Gas, EvacuationMap, EvacuationMapTimeSeries, BaseElement, GasSpreadLayers, Pos



def update_gas_filling_layers(
    gases: List[Gas], 
    evacuation_map: EvacuationMap, 
    num_iters: int, 
    diagonal_spread: bool = False,
) -> GasSpreadLayers:
    
    _spread_layers = GasSpreadLayers(layers=[])
    
    def get_neighbours(x, y):
        res = []
        neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        
        if diagonal_spread:
            neighbours += [(x+1, y+1), (x-1, y+1), (x+1, y-1), (x-1, y-1)]
        
        for i, j in neighbours:
            if 0 <= i < len(evacuation_map.ev_map[0]) and 0 <= j < len(evacuation_map.ev_map) \
                and evacuation_map.ev_map[j][i] == BaseElement.free:
                neighbour_pos = (i, j)
                res.append(neighbour_pos)
        return res
    
    queue = []
    
    for gas in gases:
        gas_pos = (gas.pos.x, gas.pos.y)
        queue.append(gas_pos)
    
    for _ in range(num_iters):
        _queue_len = len(queue)
        
        if not _queue_len:
            return _spread_layers
        
        points = []
        
        for _ in range(_queue_len):
            first_el = queue.pop(0)
            point = Pos(x=first_el[0], y=first_el[1])
            points.append(point)
            
            queue += get_neighbours(first_el[0], first_el[1])
        
        _spread_layers.layers.append(points)
        
    return _spread_layers


def update_gas_filling_time_series(
    gases: List[Gas], 
    evacuation_map: EvacuationMap, 
    num_iters: int, 
    diagonal_spread: bool = False,
    break_if_full: bool = False,
) -> EvacuationMapTimeSeries:
    
    _maps = EvacuationMapTimeSeries(maps_series=[])
    
    def get_neighbours(x, y):
        res = []
        neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        
        if diagonal_spread:
            neighbours += [(x+1, y+1), (x-1, y+1), (x+1, y-1), (x-1, y-1)]
        
        for i, j in neighbours:
            if 0 <= i < len(evacuation_map.ev_map[0]) and 0 <= j < len(evacuation_map.ev_map) \
                and evacuation_map.ev_map[j][i] == BaseElement.free:
                neighbour_pos = (i, j)
                res.append(neighbour_pos)
        return res
    
    queue = []
    
    for gas in gases:
        gas_pos = (gas.pos.x, gas.pos.y)
        queue.append(gas_pos)
    
    for _ in range(num_iters):
        _queue_len = len(queue)
        
        if not _queue_len and break_if_full:
            return _maps
        
        for _ in range(_queue_len):
            first_el = queue.pop(0)
            evacuation_map.ev_map[first_el[1]][first_el[0]] = BaseElement.gas
            queue += get_neighbours(first_el[0], first_el[1])
        
        updated_evacuation_map = copy.deepcopy(evacuation_map)
        _maps.maps_series.append(updated_evacuation_map)
    
    return _maps

    