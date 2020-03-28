import random
import math

class TicTacToeGame:

    def __init__(self, player1, player2):

        self.field = ["O", "1", "X", "X", "4", "X", "6", "O", "O"]  # Игровое поле
        self.current_player = "X"  # Следующий игрок
        self.winner = ""  # Победитель
        self.state = "run"  # Статус игры (run, draw, win)
        self.counter = {"X": 0, "O": 0, "empty": 3}
        self.players = {"X": player1, "O": player2}
        self.victory_options = []

        # по горизонтали
        self.victory_options.append([self.field[0], self.field[1], self.field[2]])
        self.victory_options.append([self.field[3], self.field[4], self.field[5]])
        self.victory_options.append([self.field[6], self.field[7], self.field[8]])

        # по вертикали
        self.victory_options.append([self.field[0], self.field[3], self.field[6]])
        self.victory_options.append([self.field[1], self.field[4], self.field[7]])
        self.victory_options.append([self.field[2], self.field[5], self.field[8]])

        # по диагонали
        self.victory_options.append([self.field[0], self.field[4], self.field[8]])
        self.victory_options.append([self.field[6], self.field[4], self.field[2]])

    def print_field(self):  # Выводит поле на экран

        print("---------")

        for i in range(0, 9):

            if i == 0 or i == 3 or i == 6:
                result = "| "

            value = self.field[i]

            if value != "X" and value != "O":
                value = " "

            result += f"{value} "

            if i == 2 or i == 5 or i == 8:
                result += "|"
                print(result)
                result = ""

        print("---------")

    def find_current_player(self):  # Определяет текущего игрока

        if self.counter["O"] < self.counter["X"]:
            self.current_player = "O"
        else:
            self.current_player = "X"

    def cell_is_free(self, cell):

        value = self.field[cell]
        return value != "X" and value != "O"

    def random_move(self):

        result = []
        for i in range(0, 9):

            if self.field[i] != "X" and self.field[i] != "O":
                result.append(i)

        return random.choice(result)

    def human_move(self):

        cells = {"1 1": 6, "1 2": 3, "1 3": 0, "2 1": 7, "2 2": 4, "2 3": 1, "3 1": 8, "3 2": 5, "3 3": 2}

        while self.state == "run":

            # field    # user input
            # 0 1 2    # (1 3) (2 3) (3 3)
            # 3 4 5    # (1 2) (2 2) (3 2)
            # 6 7 8    # (1 1) (2 1) (3 1)

            user_input = input("Enter the coordinates: ").split()

            if len(user_input) != 2 or not user_input[0].isdigit() or not user_input[1].isdigit():
                print("You should enter numbers!")
                continue

            if int(user_input[0]) > 3 or int(user_input[1]) > 3:
                print("Coordinates should be from 1 to 3!")
                continue

            new_coordinates = cells[f"{user_input[0]} {user_input[1]}"]

            if not self.cell_is_free(new_coordinates):
                print("This cell is occupied! Choose another one!")
                continue

            break

        return new_coordinates

    def computer_move(self, type_player):

        print(f'Making move level "{type_player}"')

        if type_player == "easy":
            return self.random_move()
        elif type_player == "medium":

            target_cell = ""
            for line in self.victory_options:

                if (line.count("X") == 2 and line.count("O") == 0) or (line.count("O") == 2 and line.count("X") == 0):
                    target_cell = next(x for x in line if x != "X" and x != "O")
                    break

            if target_cell == "":
                return self.random_move()
            else:
                return int(target_cell)

    def check_after_move(self):

        player = self.current_player

        # Проверяем выигрыш: по-горизонтали, по-вертикали, по-диагонали сверху вниз и снизу вверх
        if (self.field[0] == player and self.field[1] == player and self.field[2] == player) or \
                (self.field[3] == player and self.field[4] == player and self.field[5] == player) or \
                (self.field[6] == player and self.field[7] == player and self.field[8] == player) or \
                (self.field[0] == player and self.field[3] == player and self.field[6] == player) or \
                (self.field[1] == player and self.field[4] == player and self.field[7] == player) or \
                (self.field[2] == player and self.field[5] == player and self.field[8] == player) or \
                (self.field[0] == player and self.field[4] == player and self.field[8] == player) or \
                (self.field[2] == player and self.field[4] == player and self.field[6] == player):
            self.winner = self.current_player

        # Обновляем счетчики и параметры
        self.counter[self.current_player] += 1
        self.counter["empty"] -= 1
        self.find_current_player()

        # Анализируем результат игры
        if self.winner != "":
            self.state = "win"
            print(f"{self.winner} wins")
        elif self.counter["empty"] == 0:
            self.state = "draw"
            print("Draw")

    def action(self):

        while self.state == "run":

            type_player = self.players[self.current_player]

            if type_player == "human":
                new_coordinates = self.human_move()
            else:
                new_coordinates = self.computer_move(type_player)

            self.field[new_coordinates] = self.current_player
            self.print_field()

            self.check_after_move()


new_game = TicTacToeGame("medium", "easy")
new_game.print_field()
new_game.action()