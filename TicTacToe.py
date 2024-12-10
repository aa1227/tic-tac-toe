class TicTacToe:
    def __init__(self): #Initialization
        self.board = [[" " for _ in range(3)] for _ in range(3)] #Nested for loops to help with creating the board.
        self.players = {"X": "", "O": ""} #String dictionary for the players and the values of their symbols, which should be which player it is.
        self.current_player = "X"
    def boardPrint(self):
        for r in self.board:   #This method prints out the game board.
            print("|".join(r)) #appends the separators to the rows lists
            print("-" * 5) #adds five lines at the bottom of each row list
    def playerMove(self, r, c):
        if self.board[r][c] == " ": #Assigns the empty section to the current player's symbol.
            self.board[r][c] = self.current_player
            return True
        else: #Checks if the cell is already occupied, and returns false if it is.
            print("Cell is occupied. Please pick another spot on the board.")
            return False
    def playerSwitch(self): #A method that switches between the two players.
        if self.current_player == "O":
            self.current_player = "X"
        else:
            self.current_player = "O"
    def check_winner(self):
        #Checks the rows for three "X" or "O" consecutively.
        for r in self.board:
            if r[0] == r[1] == r[2] and r[0] in ["X", "O"]:
                return row[0]
        #Checks the columns for three "X" or "O" consecutively.
        for c in range(3):
            if self.board[0][c] == self.board[1][c] == self.board[2][c] and self.board[0][c] in ["X", "O"]:
                return self.board[0][c]
        
        #The following checks for diagonals for any of the valid symbols.
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] in ["X", "O"]:
            return self.board[0][0] #Returns the winner symbol
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] in ["X", "O"]:
            return self.board[0][2] #Returns the winner symbol
        
        return None #On the case that there is no winner, yet.
    def isDraw(self):
        #Checks if all rows are filled and there is no winner.
        for r in self.board:
            if " " in r:
                return False #Not all the cells are filled, so it returns false.
        if self.check_winner is None: #Runs only if all cells are filled.
            return True               #All cells are filled and there is a winner.
        return False                  #All cells are filled and there isn't a winner.
    def setup_players(self):
        # Allows the players to choose their symbol
        print("Welcome to Tic-Tac-Toe!")
        while True:
            player1 = input("Player 1, would you like to be 'X' or 'O'? ").upper()
            if player1 in ["X", "O"]:
                self.players[player1] = input(f"Enter name for Player 1 (playing as {player1}): ") #Assigns a name for each player.
                player2 = "O" if player1 == "X" else "X"
                self.players[player2] = input(f"Enter name for Player 2 (playing as {player2}): ")
                break
            else:
                print("Invalid input. Please choose 'X' or 'O'.")

        print(f"\n{self.players['X']} will play as 'X'.")
        print(f"{self.players['O']} will play as 'O'.\n")
    
    def playGame(self):
        self.setup_players()
        self.boardPrint()

        while True:
            # Prompt the current player for their move
            print(f"{self.players[self.current_player]}'s turn (playing as {self.current_player}).")
            try:
                r = int(input("Enter row (0-2): ")) #Assigns the input value to r,c.
                c = int(input("Enter column (0-2): "))
                if r < 0 or r > 2 or c < 0 or c > 2: #Checks for invalid values such as negative numbers or a number higher than 2.
                    print("Invalid input! Please enter a row and column between 0 and 2.")
                    continue
            except ValueError: #Checks if the input value isn't a number.
                print("Invalid input! Please enter numeric values.")
                continue

            if self.playerMove(r, c): #Uses the input values of r and c 
                self.boardPrint()

                winner = self.check_winner() #Assigns the value from the method to winner.
                if winner:
                    print(f"Congratulations {self.players[winner]}! You win!")
                    break

                if self.isDraw():
                    print("It's a draw! Well played!")
                    break

                self.playerSwitch()
if __name__ == "__main__":
    game = TicTacToe()
    game.playGame()   