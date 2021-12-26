
class Cell:
    def __init__(self, val):
        self.marked = False
        self.value = val
    def __repr__(self):
        if not self.marked: return " " + self.value + " "
        else: return "-" + self.value + "-"

def make_row(text_row):
    """text_row is of the form 4  2 12 23  6"""
    clean = ' '.join(text_row.split())
    items = clean.split(" ")
    return [Cell(x) for x in items]

def winningMatch(fiveItems):
    for x in fiveItems:
        if not x.marked:
            return False
    return True

def lastBoardToWin(boards):
    boardWinCount = 0
    for b in boards:
        if b.won:
            boardWinCount += 1
    return boardWinCount == len(boards) - 1

class Board:

    def __init__(self, text):
        """text is 5 lines of plaintext defining the 5x5 bingo board"""
        self.arr = []
        self.won = False
        for text_row in text.split("\n"):
            self.arr.append(make_row(text_row))
    def __repr__(self):
        return str(self.arr)

    def didWin(self):
        for row in self.arr:
            if winningMatch(row): 
                return True
        for col in range(5):
            if winningMatch(x[col] for x in self.arr):
                return True
        return False

    def mark(self, num):
        for row in self.arr:
            for cell in row:
                if cell.value == num:
                    cell.marked = True

    def allUnmarkedSum(self):
        total = 0
        for row in self.arr:
            for cell in row:
                if not cell.marked:
                    total += int(cell.value)
        return total


with open("4.txt", "r") as f:
    fileContents = f.read()
    
    numbers = fileContents.split("\n")[0].split(",")

    boards = [Board(x) for x in fileContents.split("\n\n")[1:]]

    # print(boards)

    close = False
    close2 = False

    for num in numbers:
        if close: break

        for board in boards:
            board.mark(num)
            if(board.didWin()):
                close = True
                print("Part 1:", int(num)*board.allUnmarkedSum())
                break


    for num in numbers:
        if close2: break
        for board in boards:
            board.mark(num)
            if(board.didWin()):
                if board.won == False and lastBoardToWin(boards):
                    print("Part 2:", int(num)*board.allUnmarkedSum())
                    close2 = True
                    break
                board.won = True
