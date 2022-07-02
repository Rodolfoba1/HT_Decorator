from fighterDecorator import FighterDecorator
from fighter import Fighter


class Crown(FighterDecorator):

    def get_speed(self) -> float:
        return super().get_speed()

    def get_attack(self) -> float:
        return super().get_attack()

    def get_defence(self) -> float:
        return super().get_defence()

    def get_hp(self) -> float:
        if super().get_defence() < 500:
            return super().get_hp() + 400
        else:
            return super().get_hp() + 200

    def reduce_hp(self, damage: float):
        super().reduce_hp(damage)

    def compute_damage(self, enemy: Fighter) -> float:
        return super().compute_damage(enemy)
