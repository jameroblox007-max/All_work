board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

current_player = "X"
winner = None  
game_over = False

def setup():
    size(600, 600)  
    textSize(64)    
    textAlign(CENTER, CENTER)

def draw():
    background(255)  
    
    stroke(0)
    strokeWeight(4)
    
    line(200, 0, 200, 600)
    line(400, 0, 400, 600)
    
    line(0, 200, 600, 200)
    line(0, 400, 600, 400)
    
    for i in range(3):
        for j in range(3):
            x = j * 200 + 100  
            y = i * 200 + 100  
            
            if board[i][j] == "X":
                fill(231, 76, 60)   
                text("X", x, y)
            elif board[i][j] == "O":
                fill(52, 152, 219) 
                text("O", x, y)

    check_game_status()
    
    if game_over:
        fill(0, 150) 
        rect(0, 250, 600, 100)
        
        fill(255, 255, 0) 
        textSize(48)
        if winner == "Tie":
            text("DRAW!", 300, 300)
        else:
            text(winner + " WINS!", 300, 300)
            
        textSize(64) 

def mousePressed():
    global current_player, game_over, board

    if not game_over:

        col = mouseX // 200
        row = mouseY // 200

        if 0 <= row < 3 and 0 <= col < 3:
            if board[row][col] == "":
                board[row][col] = current_player
                
                if current_player == "X":
                    current_player = "O"
                else:
                    current_player = "X"

def check_game_status():
    global winner, game_over

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "":
            winner = board[i][0]
            game_over = True
            return
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "":
            winner = board[0][i]
            game_over = True
            return
            
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        winner = board[0][0]
        game_over = True
        return
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        winner = board[0][2]
        game_over = True
        return

    is_full = True
    for row in board:
        for cell in row:
            if cell == "":
                is_full = False
                
    if is_full and not game_over:
        winner = "Tie"
        game_over = True
