from dataclasses import dataclass, field

@dataclass
class Pessoa:
    name: str
    lastname: str
    active: bool = False
    adress: list = field(default_factory=list, repr=False)
    full_name: str = field(default='Missing', init=False, repr=False)

    def __post_init__(self):
        self.full_name = f'{self.name} {self.lastname}'

if __name__ == '__main__':
    p1 = Pessoa('Fellipe', 'Patrick', True, ['São Pedro'])
    print(p1)
