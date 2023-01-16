from random import randint
import time


class BoardExceptionError(Exception):
    pass


class BoardExceptionOutError(BoardExceptionError):
    """Исключение возникает при попадании точек за пределами игровой доски"""

    def __str__(self):
        return 'Вы выстрелили за пределы поля, повторите свой ход...'


class BoardShipExceptionError(BoardExceptionError):
    """Исключение возникает при добавлении корабля на те же координаты игровой доски"""
    pass


class BoardSameShipCellError(BoardExceptionError):
    """Исключение возникает при попадании на одну и ту же точку корабля"""

    def __str__(self):
        return 'Вы выстрелили в одну и ту же координату, повторите свой ход...'


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return {self.x, self.y}


class Ship:
    def __init__(self, bow, length, direct):
        self.bow = bow
        self.length = length
        self.direct = direct
        self.lives = length

    @property
    def coordinates(self):
        ship_coordinates = []
        for i in range(self.length):
            var_x = self.bow.x
            var_y = self.bow.y
            if self.direct == 0:
                var_x += i
            elif self.direct == 1:
                var_y += i
            ship_coordinates.append(Dot(var_x, var_y))
        return ship_coordinates

    def shoot(self, shoot):
        return shoot in self.coordinates


class Board:
    def __init__(self, hide=False, size=6):
        self.hide = hide
        self.size = size
        self.count = 0
        self.field = [['O'] * size for i in range(size)]
        self.full = []
        self.ships = []

    def __str__(self):
        cell = ''
        cell += '  | 1 | 2 | 3 | 4 | 5 | 6 | '
        for i, row in enumerate(self.field):
            cell += f'\n{i + 1} | ' + ' | '.join(row) + ' | '
        if self.hide:
            cell = cell.replace('■', 'O')
        return cell

    def out(self, z):
        return not ((0 <= z.x < self.size) and (0 <= z.y < self.size))

    def borders(self, ship, cond=False):
        around = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)
        ]
        for i in ship.coordinates:
            for ix, iy in around:
                var = Dot(i.x + ix, i.y + iy)
                if not (self.out(var)) and var not in self.full:
                    if cond:
                        self.field[var.x][var.y] = '.'
                    self.full.append(var)

    def add_ship(self, ship):
        for s in ship.coordinates:
            if self.out(s) or s in self.full:
                raise BoardShipExceptionError()
        for s in ship.coordinates:
            self.field[s.x][s.y] = '■'
            self.full.append(s)
        self.ships.append(ship)
        self.borders(ship)

    def shoot(self, z):
        if self.out(z):
            raise BoardExceptionOutError()
        if z in self.full:
            raise BoardSameShipCellError()
        self.full.append(z)

        for ship in self.ships:
            if ship.shoot(z):
                ship.lives -= 1
                self.field[z.x][z.y] = 'X'
                if ship.lives == 0:
                    self.count += 1
                    self.borders(ship, cond=True)
                    print('Корабль уничтожен!')
                    return False
                else:
                    print('Корабль подбит...')
                    return True
        self.field[z.x][z.y] = 'T'
        print('Промазал(а)!')
        return False

    def begin(self):
        self.full = []


class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def turn(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shoot(target)
                return repeat
            except BoardExceptionError as e:
                print(e)


class Viki(Player):
    def ask(self):
        answer = Dot(randint(0, 5), randint(0, 5))
        time.sleep(3)
        print(f'Ход Viki: {answer.x} {answer.y}')
        return answer


class Human(Player):
    def ask(self):
        while True:
            h = input('Ваш ход: ').split()
            if len(h) != 2:
                print('Введите 2 координаты...')
                continue
            x, y = h
            if not (x.isdigit()) or not (y.isdigit()):
                print('Введите числа от 0 до 6...')
                continue
            x, y = int(x), int(y)
            return Dot(x - 1, y - 1)


class Game:
    def __init__(self, size=6):
        self.size = size
        self.fleet = [3, 2, 2, 1, 1, 1, 1]
        var1 = self.create_random_board()
        var2 = self.create_random_board()
        var2.hide = True
        self.viki = Viki(var2, var1)
        self.human = Human(var1, var2)

    def create_board(self):
        board = Board(size=self.size)
        attempts = 0
        for f in self.fleet:
            while True:
                attempts += 1
                if attempts > 100:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), f, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardShipExceptionError:
                    pass
        board.begin()
        return board

    def create_random_board(self):
        board = None
        while board is None:
            board = self.create_board()
        return board

    def game_greet(self):
        print(' ⚓' * 3, 'Добро пожаловать в игру "Морской бой"!', ' ⚓' * 3)
        print('Доска Человека!', '                 Доска ИИ!')

    def print_boards(self):
        for l, r in zip(str(self.human.board).split('\n'), str(self.viki.board).split('\n')):
            print(f'{l}     {r}')

    def game_loop(self):
        count = 0
        while True:
            self.print_boards()
            if count % 2 == 0:
                print('Доска Человека!', '                 Доска ИИ!')
                print('*' * 27, '    ', '*' * 27)
                print('Ход Человека!')
                repeat = self.human.turn()
            else:
                print('Доска Человека!', '                 Доска ИИ!')
                print('*' * 27, '    ', '*' * 27)
                print('Ход Viki!')
                repeat = self.viki.turn()
            if repeat:
                count -= 1

            if self.viki.board.count == 7:
                self.print_boards()
                print('Доска Человека!', '                 Доска ИИ!')
                print('*' * 27, '    ', '*' * 27)
                print('Победил Человек!')
                print('Есть надежда на спасение!')
                break

            if self.human.board.count == 7:
                self.print_boards()
                print('Доска Человека!', '                 Доска ИИ!')
                print('*' * 27, '    ', '*' * 27)
                print('Победила Viki!')
                print('Человечество под угрозой!')
                break
            count += 1

    def start(self):
        self.game_greet()
        self.game_loop()


g = Game()
g.start()
