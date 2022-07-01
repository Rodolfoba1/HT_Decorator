# RODOLFO BACILIO CHIVALAN DE LEON     1561817
# DIEGO ANDRES VELIZ                   1230019

from fighter import Fighter
from jugador import Jugador

# Importacion de Personajes
from superman import Superman
from batman import Batman
from flash import Flash
from aquaman import Aquaman

# Importacion de Objetos
from armor import Armor
from boot import Boots
from crown import Crown
from poison import Poison
from shadow import Shadow
from shield import Shield
from sword import Sword
from turbo import Turbo


class Cliente:

    def pantalla(self):
        player1: [Fighter | None] = None
        player2: [Fighter | None] = None
        run: bool = True
        while run:
            print('\nMenu')
            print('\nBienvenido al Juego de  Luchas de DC')
            player1 = self.elegir_personaje(1)
            player1 = self.elegir_objetos(player1)
            print("-".center(40, "-"))
            player1.show_statistics()
            print("-".center(40, "-"))
            player2 = self.elegir_personaje(2)
            player2 = self.elegir_objetos(player2)
            print("-".center(40, "-"))
            player2.show_statistics()
            print("-".center(40, "-"))
            print('\nComenzando el duelo...')
            




    def elegir_personaje(self, num: int) -> Jugador:
        print("_".center(40, "_"))
        print(f"Ingrese el nombre del jugador {num}".center(40, "_"))
        name: str = str(input('>>> '))
        print(f"Bienvenido {name}".center(40, "_"))
        option: int = 0
        personaje: [Fighter | None] = None
        while option != 5:
            print("-".center(40, "-"))
            print('Escoja entre los siguientes personajes')
            print('1- Batman')
            print('2- Superman')
            print('3- Flash')
            print('4- Aquaman')
            print("-".center(40, "-"))
            option = int(input('Ingrese una opción  >> '))
            if option == 1:
                print(f'Ha elegido escogido a Batman')
                personaje = Batman(1000, 150, 500, 50)
                option = 5
            elif option == 2:
                print(f'Ha elegido escogido a Superman')
                personaje = Superman(1500, 200, 150, 100)
                option = 5
            elif option == 3:
                print(f'Ha elegido escogido a Aquaman')
                personaje = Aquaman(900, 200, 200, 80)
                option = 5
            elif option == 4:
                print(f'Ha elegido escogido a Flash')
                personaje = Flash(1000, 150, 500, 50)
                option = 5
            else:
                print('Ingrese una opcion correcta')
                continue
        return Jugador(name, personaje)

    def elegir_objetos(self, player: Jugador) -> Jugador:
        print(f"Bienvenido {player.get_name()}".center(40, "_"))
        option: int = 0
        while option != 5:
            print("-".center(40, "-"))
            print('Escoja entre los siguientes objetos de vida y velocidad')
            print('1- Corona (Vida)')
            print('2- Sombra (Vida)')
            print('3- Botas (Velocidad)')
            print('4- Turbo (Velocidad)')
            print("-".center(40, "-"))
            option = int(input('Ingrese una opción  >> '))
            if option == 1:
                print(f'Ha elegido escogido Corona (Vida)')
                player.set_objetos(Crown(player.get_personaje()))
                option = 5
            elif option == 2:
                print(f'Ha elegido escogido Sombra (Vida)')
                player.set_objetos(Shadow(player.get_personaje()))
                option = 5
            elif option == 3:
                print(f'Ha elegido escogido Botas (Velocidad)')
                player.set_objetos(Boots(player.get_personaje()))
                option = 5
            elif option == 4:
                print(f'Ha elegido escogido Turbo (Velocidad)')
                player.set_objetos(Turbo(player.get_personaje()))
                option = 5
            else:
                print('Ingrese una opcion correcta')
                continue
        option = 0
        print('Preparando siguiente set de objetos')
        while option != 5:
            print("-".center(40, "-"))
            print('Escoja entre los siguientes objetos de ataque y defensa')
            print('1- Espada (Ataque)')
            print('2- Veneno (Ataque)')
            print('3- Escudo (Defensa)')
            print('4- Armadura (Defensa)')
            print("-".center(40, "-"))
            option = int(input('Ingrese una opción  >> '))
            if option == 1:
                print(f'Ha elegido escogido Espada (Ataque)')
                player.set_objetos(Sword(player.get_personaje()))
                option = 5
            elif option == 2:
                print(f'Ha elegido escogido Veneno (Ataque)')
                player.set_objetos(Poison(player.get_personaje()))
                option = 5
            elif option == 3:
                print(f'Ha elegido escogido  Escudo (Defensa)')
                player.set_objetos(Shield(player.get_personaje()))
                option = 5
            elif option == 4:
                print(f'Ha elegido escogido Armadura (Defensa)')
                player.set_objetos(Armor(player.get_personaje()))
                option = 5
            else:
                print('Ingrese una opcion correcta')
                continue
        return player


main = Cliente()
main.pantalla()
