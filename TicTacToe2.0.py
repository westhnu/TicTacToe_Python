import random

board = [' ' for _ in range(9)]

def print_board():
    print(f"[{board[0]} | {board[1]} | {board[2]}]")
    print(f"[{board[3]} | {board[4]} | {board[5]}]")
    print(f"[{board[6]} | {board[7]} | {board[8]}]")

# 승리 조건 확인
def check_winner(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                      (0, 4, 8), (2, 4, 6)]         
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

# 가능한 움직임 목록 반환
def get_available_moves():
    return [i for i in range(9) if board[i] == ' ']

# AI가 무작위로 움직임 선택
def ai_move():
    available_moves = get_available_moves()
    return random.choice(available_moves)

# 틱택토 게임
def tic_tac_toe():
    player = 'X'
    for turn in range(9):
        print_board()
        if player == 'X':
            move = int(input(f"플레이어 {player}, 위치 입력 (1~9): ")) - 1
        else:
            move = ai_move()  
            print(f"AI(O)가 위치 {move + 1}에 둡니다.")
        
        if board[move] == ' ':
            board[move] = player
            if check_winner(player):
                print_board()
                print(f"플레이어 {player} 승리!")
                return
            player = 'O' if player == 'X' else 'X'
    print("무승부입니다!")

# 게임 실행
tic_tac_toe()