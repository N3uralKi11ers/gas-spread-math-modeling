from models import Gas, Pos, EvacuationMap, GasType
from gas_spread import update_gas_filling_layers

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
    Gas(pos=Pos(x=6, y=5), gas=GasType.test_gas),
    Gas(pos=Pos(x=1, y=1), gas=GasType.test_gas),
]
mp = EvacuationMap(ev_map=test1)

gas_filling = update_gas_filling_layers(
    gases,
    mp,
    10,
    diagonal_spread=False,
)

for s in gas_filling.layers:
    for arr in s:
        print(arr)
    print()
