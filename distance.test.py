
from models import Pos, EvacuationMap
from distance import find_route

# optimize distance 

start = (0, 0)
end = (6, 0)

test1 = [
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

route = find_route(Pos(x=1, y=1), Pos(x=6, y=6), EvacuationMap(ev_map=test1))
print(route)