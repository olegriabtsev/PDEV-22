cells = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
game = True
over = False
turn = 0
prev_turn = -1
print('---', 'Добро пожаловать в игру "Крестики-нолики"!', '---')


def game_board(cells):
    board = (f'|{cells[1]}|{cells[2]}|{cells[3]}|\n'
             f'|{cells[4]}|{cells[5]}|{cells[6]}|\n'
             f'|{cells[7]}|{cells[8]}|{cells[9]}|')
    print(board)


def check_turn(turn):
    if turn % 2 == 0:
        return 'O'
    else:
        return 'X'


def check_win(board):
    if (cells[1] == cells[2] == cells[3]) \
            or (cells[4] == cells[5] == cells[6]) \
            or (cells[7] == cells[8] == cells[9]):
        return True
    elif (cells[1] == cells[4] == cells[7]) \
            or (cells[2] == cells[5] == cells[8]) \
            or (cells[3] == cells[6] == cells[9]):
        return True
    elif (cells[1] == cells[5] == cells[9]) \
            or (cells[3] == cells[5] == cells[7]):
        return True
    else:
        return False


while game:
    game_board(cells)
    if prev_turn == turn:
        print('Это поле уже занято, выберите другое свободное поле.')
    prev_turn = turn
    print('Ход ' + str((turn % 2) + 1) + '-го игрока. Ваш ход или введите символ q для выхода из игры: ')

    choice = input()
    if choice == 'q':
        game = False
        print('Выход из игры!')
    elif str.isdigit(choice) and int(choice) in cells:
        if not cells[int(choice)] in {'X', 'O'}:
            turn += 1
            cells[int(choice)] = check_turn(turn)
    if check_win(cells):
        game, over = False, True
    if turn > 8:
        game = False

game_board(cells)
if over:
    if check_turn(turn) == 'X':
        print('1-ый Игрок победил!')
    else:
        print('2-ой Игрок победил!')
else:
    print('Нет победителя!')

print('Спасибо за игру!')
