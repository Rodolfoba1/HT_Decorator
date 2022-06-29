from fighterDecorator import FighterDecorator
from fighter import Fighter
import random


class Shield(FighterDecorator):

    def get_speed(self) -> float:
        return super().get_speed()

    def get_attack(self) -> float:
        return super().get_attack()

    def get_defence(self) -> float:
        return super().get_defence() + 300

    def get_hp(self) -> float:
        return super().get_hp()

    def reduce_hp(self, damage: float):
        super().reduce_hp(damage)

    def compute_damage(self, enemy: Fighter) -> float:
        limit: int = 0
        if enemy.get_attack() < 1000:
            limit = 50
        else:
            limit = 75
        probabilidad: int = random.randint(1, 100)
        if probabilidad > limit:
            #Se ha bloqueado el ataque
            return 0
        else:
            return super().compute_damage(enemy)

