import pygame
pygame.init()  
width=1000
height=900
screen = pygame.display.set_mode([width,height])
font=pygame.font.Font("freesansbold.ttf",20)
big_font = pygame.font.Font("freesansbold.ttf",50)
timer=pygame.time.Clock()
fps=60

whitePieces=["rook","horse","bishop","king","queen","bishop","horse","rook"
            ,"minion","minion","minion","minion","minion","minion","minion","minion"]

whiteLocations=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
                (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]

blackPieces=["rook","horse","bishop","king","queen","bishop","horse","rook"
            ,"minion","minion","minion","minion","minion","minion","minion","minion"]

blackLocations=[(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),
                (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6) ]
capturedPiecesWhite=[]
capturedPiecesBlack=[]

turnStep=0
selection=100
validMoves=[] 

blackQueen = pygame.image.load("images/bQ.png.png")
blackQueen = pygame.transform.scale(blackQueen, (80, 80))
blackQueenSmall = pygame.transform.scale(blackQueen, (45, 45))
blackBishop = pygame.image.load("images/bB.png.png")
blackBishop = pygame.transform.scale(blackBishop, (80, 80))
blackBishopSmall = pygame.transform.scale(blackBishop, (45, 45))
blackKing = pygame.image.load("images/bK.png.png")
blackKing = pygame.transform.scale(blackKing, (80, 80))
blackKingSmall = pygame.transform.scale(blackKing, (45, 45))
blackHorse = pygame.image.load("images/bN.png.png")
blackHorse = pygame.transform.scale(blackHorse, (80, 80))
blackHorseSmall = pygame.transform.scale(blackHorse, (45, 45))
blackMinion = pygame.image.load("images/bp.png.png")
blackMinion = pygame.transform.scale(blackMinion, (80, 80))
blackMinionSmall = pygame.transform.scale(blackMinion, (45, 45))
blackRook = pygame.image.load("images/bR.png.png")
blackRook = pygame.transform.scale(blackRook, (80, 80))
blackRookSmall = pygame.transform.scale(blackRook, (45, 45))

whiteMinion = pygame.image.load("images/wp.png.png")
whiteMinion = pygame.transform.scale(whiteMinion, (80, 80))
whiteMinionSmall = pygame.transform.scale(whiteMinion, (45, 45))
whiteRook = pygame.image.load("images/wR.png.png")
whiteRook = pygame.transform.scale(whiteRook, (80, 80))
whiteRookSmall = pygame.transform.scale(whiteRook, (45, 45))
whiteHorse = pygame.image.load("images/wN.png.png")
whiteHorse = pygame.transform.scale(whiteHorse, (80, 80))
whiteHorseSmall = pygame.transform.scale(whiteHorse, (45, 45))
whiteBishop = pygame.image.load("images/wB.png.png")
whiteBishop = pygame.transform.scale(whiteBishop, (80, 80))
whiteBishopSmall = pygame.transform.scale(whiteBishop, (45, 45))
whiteQueen = pygame.image.load("images/wQ.png.png")
whiteQueen = pygame.transform.scale(whiteQueen, (80, 80))
whiteQueenSmall = pygame.transform.scale(whiteQueen, (45, 45))
whiteKing = pygame.image.load("images/wK.png.png")
whiteKing = pygame.transform.scale(whiteKing, (80, 80))
whiteKingSmall = pygame.transform.scale(whiteKing, (45, 45))

whiteImages = [whiteMinion, whiteRook, whiteHorse, whiteBishop, whiteQueen, whiteKing]
smallWhiteImages = [whiteMinionSmall, whiteRookSmall, whiteHorseSmall, whiteBishopSmall, whiteQueenSmall, whiteKingSmall]

blackImages = [blackMinion, blackRook, blackHorse, blackBishop, blackQueen, blackKing]
smallBlackImages = [blackMinionSmall, blackRookSmall, blackHorseSmall, blackBishopSmall, blackQueenSmall, blackKingSmall]

pieceList = ["minion", "rook", "horse", "bishop", "queen", "king"]

counter = 0 


def drawBoard():

    for i in range(32):
        collum = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, "light gray", [600 - (collum * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, "light gray", [700 - (collum * 200), row * 100, 100, 100])
    
    pygame.draw.rect(screen, "gray", [0, 800, width, 100])
    pygame.draw.rect(screen, "orange", [0, 800, width, 100], 5)
    pygame.draw.rect(screen, "orange", [800, 0, width, 800], 5)
    statusText = ["White! Select a piece !!!","White pick a destination!!!","Black! Select a piece!!!","Black! pick a destination!!!"]
    screen.blit(big_font.render(statusText[turnStep],True,"black"),(20,820))

def drawPieces():
    for i in range(len(whitePieces)):
        index=pieceList.index(whitePieces[i])
        if whitePieces[i] == "Minion":
            screen.blit(whiteMinion,(whiteLocations[i][0]*  + whiteLocations[i][1]))
        else:
            screen.blit(whiteImages[index],(whiteLocations[i][0] * 100, whiteLocations[i][1] * 100))
        if turnStep < 2:
             if selection == i:
                pygame.draw.rect(screen,"red",[whiteLocations[i][0]* 100 + 1, whiteLocations[i][1]* 100 + 1,
                                               100 , 100],2)

    for i in range(len(blackPieces)):
        index=pieceList.index(blackPieces[i])
        if blackPieces[i] == "Minion":
            screen.blit(blackMinion,(blackLocations[i][0]* blackLocations[i][1]))
        else:
            screen.blit(blackImages[index],(blackLocations[i][0]* 100 ,blackLocations[i][1]*100))

        if turnStep >= 2:            
             if selection == i:
                pygame.draw.rect(screen,"blue",[blackLocations[i][0]* 100 + 1, blackLocations[i][1]* 100 + 1,
                                               100 , 100],2)


def checkOptions(pieces, locations, turn):
    allMovesList = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        movesList = []  
        if piece == "minion":
            movesList = checkMinion(location, turn)
        elif piece == "rook":
            movesList = checkRook(location, turn)
        elif piece == "bishop":
            movesList = checkBishop(location, turn)
        elif piece == "horse":
            movesList = checkHorse(location, turn)
        elif piece == "queen":
            movesList = checkQueen(location, turn)
        elif piece == "king":
            movesList = checkKing(location, turn)
        allMovesList.append(movesList)
    return allMovesList

def checkQueen(position, color):
    moveList = checkBishop(position, color)
    secondList = checkRook(position, color)
    for move in secondList:
        moveList.append(move)
    return moveList

def checkRook(position,color):
    moveList = []
    if color == "white":
        enemiesList = blackLocations
        friendList = whiteLocations
    else: 
        friendList = blackLocations
        enemiesList = whiteLocations
    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friendList and \
                0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moveList.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemiesList:
                    path = False
                chain += 1
            else:
                path = False
    return moveList

def checkKing(position, color):
    movelist = []
    if color == "white":
        enemiesList = blackLocations
        friendList = whiteLocations
    else:
        friendList = blackLocations
        enemiesList = whiteLocations

    targets = [(1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friendList and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            movelist.append(target)
    return movelist

def checkHorse(position, color):
    moveList = []
    if color == "white":
        enemiesList = blackLocations
        friendList = whiteLocations
    else:
        friendList = blackLocations
        enemiesList = whiteLocations
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friendList and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moveList.append(target)
    return moveList

def checkBishop(position, color):
    moveList = []
    if color == "white":
        enemiesList = blackLocations
        friendList = whiteLocations
    else:
        friendList = blackLocations
        enemiesList = whiteLocations

    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friendList and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moveList.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemiesList:
                    path = False
                chain += 1
            else:
                path = False

    return moveList
    
def checkMinion(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in whiteLocations and \
                (position[0], position[1] + 1) not in blackLocations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        
        
        if position[1] == 1:  
            if (position[0], position[1] + 1) not in whiteLocations and \
                (position[0], position[1] + 1) not in blackLocations:
                if (position[0], position[1] + 2) not in whiteLocations and \
                        (position[0], position[1] + 2) not in blackLocations:
                    moves_list.append((position[0], position[1] + 2))

        
        if (position[0] + 1, position[1] + 1) in blackLocations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in blackLocations:
            moves_list.append((position[0] - 1, position[1] + 1))
    
    else:         
        if (position[0], position[1] - 1) not in whiteLocations and \
                (position[0], position[1] - 1) not in blackLocations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        
        
        if position[1] == 6:  
            if (position[0], position[1] - 1) not in whiteLocations and \
                (position[0], position[1] - 1) not in blackLocations:  
                if (position[0], position[1] - 2) not in whiteLocations and \
                        (position[0], position[1] - 2) not in blackLocations:
                    moves_list.append((position[0], position[1] - 2))

       
        if (position[0] + 1, position[1] - 1) in whiteLocations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in whiteLocations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list



whiteOptions = checkOptions(whitePieces, whiteLocations, "white")
blackOptions = checkOptions(blackPieces, blackLocations, "black")


def checkValidMoves():
    if turnStep < 2:
        optionsList = whiteOptions
    else:
        optionsList = blackOptions
    
    if selection != 100 and selection < len(optionsList):
        validOptions = optionsList[selection]
        return validOptions
    if blackPieces[blackPiece]=="king":
        winner = "white"
    elif whitePieces[whitePiece] == "king":
        winner = "black"
    return []  



def draw_valid(moves):
    if turnStep < 2:
        color = "green"
    else:
        color = "blue"
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)

def drawCapturedPieces():
    for i in range(len(capturedPiecesWhite)):
        capturedPiece = capturedPiecesWhite[i]
        Index = pieceList.index(capturedPiece)
        screen.blit(smallBlackImages[Index], (825 , 5 + 60 * i))
    for i in range(len(capturedPiecesBlack)):
        capturedPiece = capturedPiecesBlack[i]
        Index = pieceList.index(capturedPiece)
        screen.blit(smallWhiteImages[Index], (900 , 5 + 60 * (i + len(capturedPiecesBlack))))  



def drawCheck():
    if turnStep < 2:
        kingIndex = whitePieces.index("king")
        kingLocation = whiteLocations[kingIndex]
        for i in range(len(blackOptions)):
            if kingLocation in blackOptions[i]:
                if counter < 15:
                    pygame.draw.rect(screen,"dark red",[whiteLocations[kingIndex][0]*100+1,whiteLocations[kingIndex][1]*100+1,100,100],15)
    else:
        kingIndex = blackPieces.index("king")
        kingLocation = blackLocations[kingIndex]
        for i in range(len(whiteOptions)):
            if kingLocation in whiteOptions[i]:
                if counter < 15:
                    pygame.draw.rect(screen,"dark green",[blackLocations[kingIndex][0]*100+1,blackLocations[kingIndex][1]*100+1,100,100],15)



pass
run = True
while run:
    
    if counter < 30:
        counter+=1
    else:
        counter=0
    timer.tick(fps)
    screen.fill("dark gray")
    drawBoard()
    drawPieces()
    drawCheck()
    drawCapturedPieces()
    if selection !=100:
        validMoves=checkValidMoves()
        draw_valid(validMoves)


    for event in pygame.event.get():
     
     
     if event.type == pygame.QUIT:
        run = False
    
     if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        x_coord = event.pos[0] // 100
        y_coord = event.pos[1] // 100
        clickCoords = (x_coord, y_coord)
    


           
        
        if turnStep > 1:
            if clickCoords in blackLocations:
                selection = blackLocations.index(clickCoords)
                if turnStep == 2:
                    turnStep = 3
            if clickCoords in validMoves and selection != 100:
                blackLocations[selection] = clickCoords
                if clickCoords in whiteLocations:
                    whitePiece = whiteLocations.index(clickCoords)
                    capturedPiecesBlack.append(whitePieces[whitePiece])
                    whitePieces.pop(whitePiece)
                    whiteLocations.pop(whitePiece)
                blackOptions = checkOptions(blackPieces , blackLocations, "black")
                whiteOptions = checkOptions(whitePieces, whiteLocations, "white")
                turnStep = 0
                selection = 100
                validMoves = []
  
        if turnStep <= 1:
            if clickCoords in whiteLocations:
                selection = whiteLocations.index(clickCoords)
                if turnStep == 0:
                    turnStep = 1
        if clickCoords in validMoves and selection != 100:
                whiteLocations[selection] = clickCoords
                if clickCoords in blackLocations:
                    blackPiece = blackLocations.index(clickCoords)
                    capturedPiecesWhite.append(blackPieces[blackPiece])
                    blackPieces.pop(blackPiece)
                    blackLocations.pop(blackPiece)
                blackOptions = checkOptions(blackPieces , blackLocations, "black")
                whiteOptions = checkOptions(whitePieces, whiteLocations, "white")
                turnStep = 2
                selection = 100
                validMoves = []

    pygame.display.flip()
pygame.quit()
