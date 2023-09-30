from models import Gas, Pos, EvacuationMap, GasType
from gas_spread import update_gas_filling

test1 = [
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

test2 = [[0]*50 for _ in range(9)]

test3 = [
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
]

gases = [
    Gas(pos=Pos(x=5, y=5), gas=GasType.test_gas),
    Gas(pos=Pos(x=1, y=1), gas=GasType.test_gas),
]
mp = EvacuationMap(ev_map=test3)

gas_filling = update_gas_filling(
    gases,
    mp,
    10,
    diagonal_spread=False,
    break_if_full=True
)

for s in gas_filling.maps_series:
    for arr in s.to_array():
        print(*arr)
    print()
