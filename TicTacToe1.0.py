board = [' ' for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(board[i:i+3])

def check_winner(player):
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in wins)

def tic_tac_toe():
    player = 'X'
    for turn in range(9):
        print_board()
        move = int(input(f"플레이어 {player}, 위치 입력 (1-9): ")) - 1
        if board[move] == ' ':
            board[move] = player
            if check_winner(player):
                print_board()
                print(f"플레이어 {player} 승리!")
                return
            player = 'O' if player == 'X' else 'X'
    print("무승부입니다!")

tic_tac_toe()