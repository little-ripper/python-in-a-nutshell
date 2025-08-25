import dataclasses
import time

@dataclasses.dataclass
class Point:
    x: float
    y: float
    create_time: float = 0.0

    def __post_init__(self):
        self.create_time = time.time()

p = Point(x=0.5, y=0.5)
print(p)
