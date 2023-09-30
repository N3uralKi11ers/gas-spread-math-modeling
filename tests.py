from models import Gas, Pos, EvacuationMap, GasType
from gas_spread import update_gas_filling
from distance import calculate_distance

test1 = [
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

# start = (0, 0)
# end = (6, 0)


gas = Gas(pos=Pos(x=4, y=4), gas=GasType.test_gas)
mp = EvacuationMap(ev_map=test1)

update_gas_filling(
    gas,
    mp,
    30
)