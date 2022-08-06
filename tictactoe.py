from menacebrains.menace import menace


def rotate(list):
    P = len(list)
    Q = len(list[0])
    list_rotated = [[None] * P for _ in range(Q)]
    for q in range(Q):
        for p in range(P-1, -1, -1):
            list_rotated[Q-q-1][p] = list[p][q]
    return list_rotated


game = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]
moves = range(1, 10)
score = [0, 0]
try:
    players = int(input("Number of players: 1 or 2 >>> "))
    if players != 1 or players != 2:
        players == 1
except ValueError:
    players = 1
games = 1
if players == 2:
    player1name = input("Player 1's name >>> ")
    if player1name == "":
        player1name = "Player 1"
    player2name = input("Player 2's name >>> ")
    if player2name == "":
        player2name = "Player 2"

Player1_Has_Won = False
Player2_Has_Won = False
There_Is_Hope = True
Will_To_Live = True
Has_Made_Legal_Move = False
print("""
    1 | 2 | 3
    --+---+--
    4 | 5 | 6
    --+---+--
    7 | 8 | 9""")

while Will_To_Live == True:
    xmoves = []
    omoves = []
    print(f"""
Game {games}:""")
    spaces_used = 0
    while Player1_Has_Won == False and Player2_Has_Won == False and There_Is_Hope == True:
        while Has_Made_Legal_Move == False:
            try:
                if players == 1:
                    move = input("""
>>> """)
                elif players == 2:
                    move = input(f"""
{player1name} >>> """)

                move = int(move)

                if move not in moves:
                    raise ValueError
                if game[int(move - 1) // 3][int(move - 1) % 3] != " ":
                    raise ValueError

                move -= 1
                xmoves.append(move)
                spaces_used += 1
                game[int(move) // 3][int(move) % 3] = "X"

                print(f"""
    {game[0][0]} | {game[0][1]} | {game[0][2]}
    --+---+--
    {game[1][0]} | {game[1][1]} | {game[1][2]}
    --+---+--
    {game[2][0]} | {game[2][1]} | {game[2][2]}""")

                for x in game:
                    if x == ["X", "X", "X"]:
                        Player1_Has_Won = True
                for x in rotate(game):
                    if x == ["X", "X", "X"]:
                        Player1_Has_Won = True
                if game[0][0] == "X" and game[1][1] == "X" and game[2][2] == "X":
                    Player1_Has_Won = True
                elif game[0][2] == "X" and game[1][1] == "X" and game[2][0] == "X":
                    Player1_Has_Won = True
                if spaces_used == 9:
                    There_Is_Hope = False
                if Player1_Has_Won == True or There_Is_Hope == False:
                    break
                break
            except ValueError:
                print(f"""
    {game[0][0]} | {game[0][1]} | {game[0][2]}
    --+---+--
    {game[1][0]} | {game[1][1]} | {game[1][2]}
    --+---+--
    {game[2][0]} | {game[2][1]} | {game[2][2]}

    Try again.""")

        while Has_Made_Legal_Move == False:
            if Player1_Has_Won == True:
                break
            try:
                if players == 1 and Player2_Has_Won == False and There_Is_Hope == True:
                    move = menace(xmoves)
                    omoves.append(move)
                    spaces_used += 1
                    game[move // 3][move % 3] = "O"

                    print(f"""
    {game[0][0]} | {game[0][1]} | {game[0][2]}
    --+---+--
    {game[1][0]} | {game[1][1]} | {game[1][2]}
    --+---+--
    {game[2][0]} | {game[2][1]} | {game[2][2]}""")

                    for x in game:
                        if x == ["O", "O", "O"]:
                            Player2_Has_Won = True
                            break
                    for x in rotate(game):
                        if x == ["O", "O", "O"]:
                            Player2_Has_Won = True
                            break
                    if game[0][0] == "O" and game[1][1] == "O" and game[2][2] == "O":
                        Player2_Has_Won = True
                        break
                    elif game[0][2] == "O" and game[1][1] == "O" and game[2][0] == "O":
                        Player2_Has_Won = True
                        break

                elif players == 2 and Player2_Has_Won == False and There_Is_Hope == True:
                    move = input(f"""
{player2name} >>> """)

                    move = int(move)

                    if move not in moves:
                        raise ValueError
                    if game[int(move - 1) // 3][int(move - 1) % 3] != " ":
                        raise ValueError

                    move -= 1
                    omoves.append(move)
                    spaces_used += 1
                    game[int(move) // 3][int(move) % 3] = "O"

                    print(f"""
    {game[0][0]} | {game[0][1]} | {game[0][2]}
    --+---+--
    {game[1][0]} | {game[1][1]} | {game[1][2]}
    --+---+--
    {game[2][0]} | {game[2][1]} | {game[2][2]}""")

                    for x in game:
                        if x == ["O", "O", "O"]:
                            Player2_Has_Won = True
                            break
                    for x in rotate(game):
                        if x == ["O", "O", "O"]:
                            Player2_Has_Won = True
                            break
                    if game[0][0] == "O" and game[1][1] == "O" and game[2][2] == "O":
                        Player2_Has_Won = True
                        break
                    elif game[0][2] == "O" and game[1][1] == "O" and game[2][0] == "O":
                        Player2_Has_Won = True
                        break
                break
            except ValueError:
                print(f"""
    {game[0][0]} | {game[0][1]} | {game[0][2]}
    --+---+--
    {game[1][0]} | {game[1][1]} | {game[1][2]}
    --+---+--
    {game[2][0]} | {game[2][1]} | {game[2][2]}

    Try again.""")

    if Player1_Has_Won == True and players == 1:
        score[0] += 1
        print("""
You win!""")
    elif Player2_Has_Won == True and players == 1:
        score[1] += 1
        print("""
I win!""")
    elif Player1_Has_Won == True and players == 2:
        score[0] += 1
        print(f"""
{player1name} wins!""")
    elif Player2_Has_Won == True and players == 2:
        score[1] += 1
        print(f"""
{player2name} wins!""")
    elif There_Is_Hope == False:
        print("""
It's a tie!""")
    if players == 1:
        print(f"""
    ---SCORE---
    You: {score[0]}
    Me : {score[1]}""")
    elif players == 2:
        print(f"""
    ---SCORE---
    {player1name}: {score[0]}
    {player2name}: {score[1]}""")
    game = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]
    Player1_Has_Won = False
    Player2_Has_Won = False
    There_Is_Hope = True
    games += 1