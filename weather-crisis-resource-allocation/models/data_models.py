from dataclasses import dataclass

@dataclass
class Region:
    name: str
    need: int
    urgency: int

@dataclass
class Depot:
    name: str
    supply: int
