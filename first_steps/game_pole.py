from random import randint


class Cell:
    def __init__(self, mine=0, around_mines=0) -> None:
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

class GamePole:
    def __init__(self, N, M) -> None:
        self.pole = self.init(N)
        self.put_mines(N, M)
        self.count_around(N)
    
    def init(self, N):
        return [[Cell() for _ in range(N)] for _ in range(N)]
    
    def put_mines(self, N, M):
        while M > 0:
            i, j = randint(1, N-2), randint(1, N-2)
            self.pole[i][j].mine = 1
            M -= 1                

    def count_around(self, N):
        for i in range(1, N-1):
            for j in range(1, N-1):
                if self.pole[i][j].mine:
                    self.pole[i-1][j-1].around_mines += 1
                    self.pole[i-1][j].around_mines += 1
                    self.pole[i-1][j+1].around_mines += 1
                    self.pole[i+1][j-1].around_mines += 1
                    self.pole[i+1][j].around_mines += 1
                    self.pole[i+1][j+1].around_mines += 1
                    self.pole[i][j-1].around_mines += 1
                    self.pole[i][j+1].around_mines += 1

    def show(self):
        for row in self.pole:
            print([cell.mine if cell.mine else cell.around_mines for cell in row])            
            pass


pole_game = GamePole(10, 12)
pole_game.show()
