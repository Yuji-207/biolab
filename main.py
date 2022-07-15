from typing import List, Union
from pydantic import BaseModel


class Image(BaseModel):
    path: str = None
    type: str = None
    magnification: int = None
    datetime: str = None


class Component(BaseModel):
    name: str = None
    amount: float = None
    unit: str = None


class Cycle(BaseModel):
    repeat: int = None
    temperature: float = None
    timedelta: int = None
    images: List[Image] = None


class DNA(BaseModel):
    name: str = None
    components: List[Component] = None
    cycles: List[Cycle] = None
    start_date: str = None
    end_date: str = None


class RNA(BaseModel):
    yields: float = None
    start_date: str = None
    end_date: str = None


class State(BaseModel):
    type: str = None
    coating: str = None
    init_cell_number: int = None
    components: List[Component] = None
    images: List[Image] = None
    start_date: str = None
    end_date: str = None


class Condition(BaseModel):
    dna: List[DNA] = None
    rna: List[RNA] = None
    states: List[State] = None
    start_date: str = None
    end_date: str = None
    

class Experiment(BaseModel):
    conditions: List[Condition] = None
    start_date: str = None
    end_date: str = None
