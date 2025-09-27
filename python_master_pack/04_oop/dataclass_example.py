"""Dataclass with validation and post-init"""
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    age: int = 0
    tags: list = field(default_factory=list)

    def __post_init__(self):
        if self.age < 0:
            raise ValueError('age must be >=0')

if __name__ == '__main__':
    u = User('Karthi', 40, ['dev'])
    print(u)
