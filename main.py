#*************#
#School project made in 10th grade for finishing project
#made 16.05.22
#Made by Aleksander Blom
#*************#




import pygame
import pygame_menu

#setting global variables that I need
global player1name
player1name = "player 1"
global player2name
player2name = "player 2"

global screen

if __name__ == '__main__':
    from ChessPieces import *
else:
    from .ChessPieces import *



pygame.display.set_caption("Chess")

pygame.init()
screen = pygame.display.set_mode((400,400))

#---------------------#

class Board():

  def draw(screen):
    white,black= (138, 87, 0),(248, 212, 150)
    size = 40
    boardLength = 8

    cnt = 0
    for i in range(1,boardLength+1):
      for z in range(1,boardLength+1):
        #check if current loop value is even
        if cnt % 2 == 0:
          pygame.draw.rect(screen, white,[size*z,size*i,size,size])
        else:
          pygame.draw.rect(screen, black, [size*z,size*i,size,size])
        cnt +=1
        #since theres an even number of squares go back one value
      cnt-=1
    #Add a nice boarder
    pygame.draw.rect(screen,black,[size,size,boardLength*size,boardLength*size],1)
    pygame.display.update()


#---------------------#


def Draw(screen, pieces):
  #Drawning all the pieces to the board, first black then white
  for i in pieces:
    for j in i:
      j.Draw(screen)


  #updating the display
  pygame.display.update()

#---------------------#

def CreateAllPieces():
  #Black pieces is [0] white is [1]
  pieces = [[],[]]

  #creating black pawns
  pawnB1 = Pawn(40*1, 80, 'b')
  pieces[0].append(pawnB1)
  pawnB2 = Pawn(40*2, 80, 'b')
  pieces[0].append(pawnB2)
  pawnB3 = Pawn(40*3, 80, 'b')
  pieces[0].append(pawnB3)
  pawnB4 = Pawn(40*4, 80, 'b')
  pieces[0].append(pawnB4)
  pawnB5 = Pawn(40*5, 80, 'b')
  pieces[0].append(pawnB5)
  pawnB6 = Pawn(40*6, 80, 'b')
  pieces[0].append(pawnB6)
  pawnB7 = Pawn(40*7, 80, 'b')
  pieces[0].append(pawnB7)
  pawnB8 = Pawn(40*8, 80, 'b')
  pieces[0].append(pawnB8)

  #creating white pawns
  pawnW1 = Pawn(40*1, 280, 'w')
  pieces[1].append(pawnW1)
  pawnW2 = Pawn(40*2, 280, 'w')
  pieces[1].append(pawnW2)
  pawnW3 = Pawn(40*3, 280, 'w')
  pieces[1].append(pawnW3)
  pawnW4 = Pawn(40*4, 280, 'w')
  pieces[1].append(pawnW4)
  pawnW5 = Pawn(40*5, 280, 'w')
  pieces[1].append(pawnW5)
  pawnW6 = Pawn(40*6, 280, 'w')
  pieces[1].append(pawnW6)
  pawnW7 = Pawn(40*7, 280, 'w')
  pieces[1].append(pawnW7)
  pawnW8 = Pawn(40*8, 280, 'w')
  pieces[1].append(pawnW8)

  #creating black rooks
  rookB1 = Rook(40,40,'b')
  pieces[0].append(rookB1)
  rookB2 = Rook(40*8,40,'b')
  pieces[0].append(rookB2)

  #creating white rooks
  rookW1 = Rook(40,40*8,'w')
  pieces[1].append(rookW1)
  rookW2 = Rook(40*8,40*8,'w')
  pieces[1].append(rookW2)

  #creating black horse
  horseB1 = Horse(40*2,40,'b')
  pieces[0].append(horseB1)
  horseB2 = Horse(40*7,40,'b')
  pieces[0].append(horseB2)

  #creating white horse
  horseW1 = Horse(40*2,40*8,'w')
  pieces[1].append(horseW1)
  horseW2 = Horse(40*7,40*8,'w')
  pieces[1].append(horseW2)

  #creating black bishop
  bishopB1 = Bishop(40*3,40,'b')
  pieces[0].append(bishopB1)
  bishopB2 = Bishop(40*6,40,'b')
  pieces[0].append(bishopB2)

  #creating white bishop
  bishopW1 = Bishop(40*3,40*8,'w')
  pieces[1].append(bishopW1)
  bishopW2 = Bishop(40*6,40*8,'w')
  pieces[1].append(bishopW2)

  #creating black queen
  queenB1 = Queen(40*4,40,'b')
  pieces[0].append(queenB1)

  #creating white queen
  queenW1 = Queen(40*4,40*8,'w')
  pieces[1].append(queenW1)

  #creating black King
  kingB1 = King(40*5,40,'b')
  pieces[0].append(kingB1)

  #creating white king
  kingW1 = King(40*5,40*8,'w')
  pieces[1].append(kingW1)

  for i in pieces[0]:
    i.AvalibleMoves(pieces)
  for i in pieces[1]:
    i.AvalibleMoves(pieces)

  return pieces

#---------------------#

def updateMoves(pieces):
  for i in pieces[0]:
    i.AvalibleMoves(pieces)
  for i in pieces[1]:
    i.AvalibleMoves(pieces)

#---------------------#
    

def drawAvalible(screen, pieces, currentActive, color):
  avalibleMoves = pieces[color][currentActive].AvalibleMoves(pieces)

  for i in avalibleMoves:
    pygame.draw.circle(screen, (230,230,230), (i[0]+20,i[1]+20), 10)
  
  return avalibleMoves

#---------------------#

def Winner(w):
  menu = pygame_menu.Menu('Game Over', 400, 400,theme=pygame_menu.themes.THEME_SOLARIZED)

  if w == 'w':
    menu.add.label(f"{player2name} (white) won the game")
  if w == 'b':
    menu.add.label(f"{player1name} (black) won the game")

  menu.add.button('Play again', Game, menu)
  menu.add.button('Quit', pygame_menu.events.EXIT)

  surface = pygame.display.set_mode((400,400))
  menu.mainloop(surface)

#---------------------#

def SwitchQueen(color, pos, pieces, menu):
  if color == 0:
    queen = Queen(pos[0],pos[1],'b')
    pieces[0].append(queen)
    menu.disable()
  if color == 1:
    queen = Queen(pos[0],pos[1],'w')
    pieces[1].append(queen)
    menu.disable()

def SwitchBishop(color, pos, pieces, menu):
  if color == 0:
    bishop = Bishop(pos[0],pos[1],'b')
    pieces[0].append(bishop)
    menu.disable()
  if color == 1:
    bishop = Bishop(pos[0],pos[1],'w')
    pieces[1].append(bishop)
    menu.disable()

def SwitchRook(color, pos, pieces, menu):
  if color == 0:
    rook = Rook(pos[0],pos[1],'b')
    pieces[0].append(rook)
    menu.disable()
  if color == 1:
    rook = Rook(pos[0],pos[1],'w')
    pieces[1].append(rook)
    menu.disable()

def SwitchHorse(color, pos, pieces, menu):
  if color == 0:
    horse = Horse(pos[0],pos[1],'b')
    pieces[0].append(bishop)
    menu.disable()
  if color == 1:
    horse = Horse(pos[0],pos[1],'w')
    pieces[1].append(horse)
    menu.disable()
  

def ChangePawn(color, pos, pieces):
  menu = pygame_menu.Menu('Switch your pawn', 400, 400,theme=pygame_menu.themes.THEME_SOLARIZED)
  
  menu.add.button('Queen', SwitchQueen,color, pos, pieces, menu)
  
  menu.add.button('Bishop', SwitchBishop,color, pos, pieces, menu)

  menu.add.button('Rook', SwitchRook,color, pos, pieces, menu)

  menu.add.button('Knight', SwitchHorse,color, pos, pieces, menu)

  surface = pygame.display.set_mode((400,400))

  menu.mainloop(surface)

  #reseting screen after the menu dissepar
  screen.fill((71,71,71))
  font = pygame.font.Font('freesansbold.ttf', 20)
  text1 = font.render(player1name, True, (255,255,255), (71,71,71))
  text2 = font.render(player2name, True, (255,255,255), (71,71,71))
  
  screen.blit(text1,(10,10))
  screen.blit(text2,(10,370))

  return ""
  
    

#-------------------------#

def Move(screen,currentActive, newPos, color, pieces, turn):
  pieces[color][currentActive].Move(newPos)
  
  #removing a piece if its taken
  if color == 1:
    j=-1
    for i in pieces[0]:
      j+=1
      if newPos == i.pos:

        #cheking if king is taken
        if i.identity == 'king':
          Winner('w')

        del pieces[0][j]
        
  #removing a piece if its taken
  if color == 0:
    j=-1
    for i in pieces[1]:
      j+=1
      if newPos == i.pos:
        
        #cheking if king is taken
        if i.identity == 'king':
          Winner('b')
          
        #deleting the piece
        del pieces[1][j]
        
      
  #cheking if a pawn has gone over and deleting the piece and calling the change function
  if pieces[color][currentActive].pos[1] == 40 and pieces[color][currentActive].color == 'w' and pieces[color][currentActive].identity == 'Pawn':
    del pieces[color][currentActive]
    temp = ChangePawn(color, newPos, pieces)
    
  if pieces[color][currentActive].pos[1] == 320 and pieces[color][currentActive].color == 'b' and pieces[color][currentActive].identity == 'Pawn':
    del pieces[color][currentActive]
    temp = ChangePawn(color, newPos, pieces)

  
  #changing whos turn it is
  if turn == 'white':
    turn = 'black'
  elif turn == 'black':
    turn = 'white'

  #drawing everything again
  Board.draw(screen)

  #setting the piece to non active
  pieces[color][currentActive].active = False

  updateMoves(pieces)
  
  return pieces, turn

#---------------------#

def Game(menu):
  menu.disable()
  run = True
  screen.fill((71,71,71))

  #Drawing the board
  Board.draw(screen)

  #getting every piece on the board
  pieces = CreateAllPieces()

  #keeping track of whos turn it is
  turn = 'white'

  #keeping track of wich piece is active
  global currentActive
  currentActive = None

  avalibleMoves = None

  global player1name
  global player2name

  if player1name == "":
    player1name = "player 1"
  if player2name == "":
    player2name = "player 2"

  
  font = pygame.font.Font('freesansbold.ttf', 20)
  
  text1 = font.render(player1name, True, (255,255,255), (71,71,71))
  text2 = font.render(player2name, True, (255,255,255), (71,71,71))
  
  screen.blit(text1,(10,10))
  screen.blit(text2,(10,370))
  

  while run:
    #checking for events
    for event in pygame.event.get():
      #checking if we quit
      if event.type == pygame.QUIT:
        run = False

      #cheking if mouse is pressed
      if event.type == pygame.MOUSEBUTTONDOWN:

        mouse = pygame.mouse.get_pos()
        
      

        if turn == 'white':

          #keeping track of how many times it has looped
          index = 0

          #looping thru all the white pieces
          for i in pieces[1]:
            #cheking whick button mouse is clicking
            if i.pos[0] <= mouse[0] <= i.pos[0]+40 and  i.pos[1] <= mouse[1] <= i.pos[1]+40:
              #making the current active not active anymore
              try:
                pieces[1][currentActive].active = False
              except:
                pass
              
              #setting the new current active
              Board.draw(screen)
              currentActive = index
              i.active = True

              avalibleMoves = drawAvalible(screen, pieces, currentActive, 1)


            index +=1


        elif turn == 'black':
          #keeping track of how many times it has looped
          index = 0

          #looping thru all the black pieces
          for i in pieces[0]:
            #cheking whick button mouse is clicking
            if i.pos[0] <= mouse[0] <= i.pos[0]+40 and  i.pos[1] <= mouse[1] <= i.pos[1]+40:
              #making the current active not active anymore
              try:
                pieces[0][currentActive].active = False
              except:
                pass
              
              #setting the new current active
              Board.draw(screen)
              currentActive = index
              i.active = True

              avalibleMoves = drawAvalible(screen, pieces, currentActive, 0)


            index +=1

        #cheking if you clicked one of the valid moves
        try:
          for i in avalibleMoves:
            if i[0] <= mouse[0] <= i[0]+40 and  i[1] <= mouse[1] <= i[1]+40:
              #cheking if turn is white
              if turn == 'white':
                pieces,turn = Move(screen, currentActive, i, 1, pieces,turn)
              elif turn == 'black':
                pieces,turn = Move(screen, currentActive, i, 0, pieces,turn)
              #reseting current active
              currentActive = None
        except:
          pass
  
    #calling a function that draws the pieces
    Draw(screen, pieces)

#---------------------#

def Menu():
  menu = pygame_menu.Menu('Chess', 400, 400,theme=pygame_menu.themes.THEME_SOLARIZED)

  menu.add.text_input('Player 1: ', default='', onchange= Player1, maxchar=8)
  menu.add.text_input('Player 2: ', default='', onchange=Player2, maxchar=8)
  menu.add.button('Play', Game, menu)
  menu.add.button('Quit', pygame_menu.events.EXIT)

  surface = pygame.display.set_mode((400,400))
  menu.mainloop(surface)

def Player1(name):
  global player1name
  player1name = name
def Player2(name):
  global player2name
  player2name = name

Menu()
