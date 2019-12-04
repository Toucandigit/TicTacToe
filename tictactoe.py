import random

class TBoard(object):
    def __init__(self, pl = "X"):
        self.board = [" "] * 9
        if len(pl) > 1:
            pl = pl[0]
        if pl == " " or pl == "":
            self.pl = "X"
        else:
            self.pl = str(pl)
        if str(pl) != "O":
            self.ai = "O"
        else:
            self.ai = "X"

    def pl_move(self, space):
        self.board[space] = self.pl

    def is_win(self):
        for ind in range(0, 3):
            if self.board[ind] == self.board[ind + 3] == self.board[ind + 6] != " ":
                return self.board[ind]
        for ind in range(0, 7, 3):
            if self.board[ind] == self.board[ind + 1] == self.board[ind + 2] != " ":
                return self.board[ind]
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return self.board[0]
        elif self.board[2] == self.board[4] == self.board[6] != " ":
            return self.board[2]
        else:
            return None

    def ai_move(self):
        test_board = list(self.board)
        for ind in range(len(test_board)):
            if test_board[ind] != " ":
                continue
            test_board[ind] = self.ai
            if TBoard.test_win(test_board) == self.ai:
                self.board[ind] = self.ai
                break
            test_board = list(self.board)
        else:
            for ind2 in range(len(test_board)):
                if test_board[ind2] != " ":
                    continue
                test_board[ind2] = self.pl
                if TBoard.test_win(test_board) == self.pl:
                    self.board[ind2] = self.ai
                    break
                test_board = list(self.board)
            else:
                scores = self.test_board(test_board)
                max_score = max(scores)
                at_max = []
                for ind in range(len(scores)):
                    if scores[ind] == max_score:
                        at_max.append(ind)
                move = random.choice(at_max)
                while self.board[move] != " ":
                    move = random.choice(at_max)
                self.board[move] = self.ai

    def print_board(self):
        for ind in range(0, 7, 3):
            print(" " + str(self.board[ind]) + " | " + str(self.board[ind + 1]) + " | " + str(self.board[ind + 2]) + " ")
            if ind != 6:
                print("---|---|---")

    @staticmethod
    def test_win(board):
        assert len(board) == 9
        for tile in board:
            if tile == " ":
                break
        else:
            return "No one"
        for ind in range(0, 3):
            if board[ind] == board[ind + 3] == board[ind + 6] != " ":
                return board[ind]
        for ind in range(0, 7, 3):
            if board[ind] == board[ind + 1] == board[ind + 2] != " ":
                return board[ind]
        if board[0] == board[4] == board[8] != " ":
            return board[0]
        elif board[2] == board[4] == board[6] != " ":
            return board[2]
        else:
            return None

    def test_board(self, board):
        tb = list(board)
        scores = []
        for ind in range(len(board)):
            if board[ind] != " ":
                scores.append(0)
                continue
            tb[ind] = self.ai
            score = 0
            for ind2 in range(len(board)):
                if tb[ind2] != " ":
                    continue
                else:
                    tb[ind2] = self.pl
                    if TBoard.test_win(tb) is None:
                        score2 = sum(self.test_board(tb))
                        score += score2
                    else:
                        if TBoard.test_win(tb) == self.pl:
                            score += 0
                        else:
                            score += 1
            scores.append(score)
            tb = list(board)
        return scores

    def reset(self):
        self.board = [" "] * 9

    def play(self):
        start = raw_input("Would you like to go first? [y/n]")
        while start != "y" and start != "n":
            start = raw_input("I didn't quite catch that")
        answer = None
        if start == "n":
            self.ai_move()
            self.print_board()
        while TBoard.test_win(self.board) is None:
            self.print_board()
            def seek_answer():
                ans = input("Where would you like to go? [1 to 9]") - 1
                if not 0 <= ans < 9:
                    print("That's not a valid tile! Try again!")
                    ans = seek_answer()
                elif self.board[ans] != " ":
                    print("Oops! Looks like that tile is already taken! Try again!")
                    ans = seek_answer()
                return ans
            answer = seek_answer()
            self.pl_move(answer)
            self.print_board()
            if TBoard.test_win(self.board) is not None:
                break
            self.ai_move()
            self.print_board()
        print(TBoard.test_win(self.board) + " wins!")
        again = raw_input("Would you like to play again? [y/n]")
        while again != "y" and again != "n":
            again = raw_input("Sorry, I didn't quite get that.")
        if again == "y":
            self.reset()
            self.play()
        else:
            print("Thanks for playing!")

brd = TBoard()
brd.play()
