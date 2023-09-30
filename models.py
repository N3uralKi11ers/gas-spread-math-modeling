from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class Pos(BaseModel):
    x: int
    y: int
    
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

class EvacuationMap(BaseModel):
    ev_map: List[List[int]] 
    class Config:
        from_attributes = True

class EvacuationMapTimeSeries(BaseModel):
    maps_series: List[EvacuationMap]
    class Config:
        from_attributes = True

class BaseSettings(BaseModel):
    person: Person
    gases: List[Gas]
    
    class Config:
        from_attributes = True