from pydantic import BaseModel
from typing import List, Optional, Tuple
from enum import Enum

class Pos(BaseModel):
    x: int
    y: int
    
    def to_tuple(self) -> Tuple[int, int]:
        return (self.x, self.y)
    
    def to_tuple_yx(self) -> Tuple[int, int]:
        return (self.y, self.x)
    
    class Config:
        from_attributes = True

class GasType(Enum):
    test_gas = 0

class Gas(BaseModel):
    pos: Pos
    gas: GasType

    def velocity(self) -> float:
        pass

    class Config:
        from_attributes = True

class Person(BaseModel):
    pos: Pos
    velocity: float = 1.0
    class Config:
        from_attributes = True

class Destination(BaseModel):
    position: Pos
    class Config:
        from_attributes = True

class BaseElement(Enum):
    free = 0
    wall = 1
    person = 2
    gas = 3

class Route(BaseModel):
    points: List[Pos]
    
class EvacuationMap(BaseModel):
    ev_map: List[List[BaseElement]] 
    
    def to_array(self) -> List[List[int]]:
        return [[v.value for v in _map] for _map in self.ev_map]
    
    class Config:
        from_attributes = True

class EvacuationMapTimeSeries(BaseModel):
    maps_series: List[EvacuationMap]
    
    class Config:
        from_attributes = True

class GasSpreadLayers(BaseModel):
    layers: List[List[Pos]]

class BaseSettings(BaseModel):
    person: Person
    gases: List[Gas]
    
    class Config:
        from_attributes = True