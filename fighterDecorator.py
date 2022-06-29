from fighter import Fighter


class FighterDecorator(Fighter):

    def __init__(self, nuevo: Fighter):
        self._jugador: Fighter = nuevo

    def get_speed(self) -> float:
        return self._jugador.get_speed()

    def get_attack(self) -> float:
        return self._jugador.get_attack()

    def get_defence(self) -> float:
        return self._jugador.get_defence()

    def get_hp(self) -> float:
        return self._jugador.get_hp()

    def reduce_hp(self, damage: float):
        self._jugador.reduce_hp(damage)

    def compute_damage(self, enemy: Fighter) -> float:
        return self._jugador.compute_damage(enemy)
