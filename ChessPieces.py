import pygame

#creating a pawn class so i can make pawns easy
class Pawn():
  
  def __init__(self,x,y,color,first=True,active=False):
    self.pos = (x, y)
    self.identity = 'Pawn'
    self.color = color
    self.imgWhite = pygame.image.load('./chess pieces/pawn_white.png')
    self.imgWhite = pygame.transform.scale(self.imgWhite, (40,40))
    self.imgBlack = pygame.image.load('./chess pieces/pawn_black.png')
    self.imgBlack = pygame.transform.scale(self.imgBlack, (40,40))
    self.active = active
    self.first = first
    self.allAvalibleMoves = []

  def AvalibleMoves(self,pieces):
    avalibleMoves = []
    avalible = True
    if self.color == 'w':

      #cheking if it is inside of the border:
      if self.pos[1]-40 < 40:
        avalible = False
      #cheking if a piece is in front
      for i in pieces[0]:
        if i.pos[0] == self.pos[0] and i.pos[1] == self.pos[1]-40:
          avalible = False
      for i in pieces[1]:
        if i.pos[0] == self.pos[0] and i.pos[1] == self.pos[1]-40:
          avalible = False
      if avalible:
        avalibleMoves.append((self.pos[0],self.pos[1]-40))
        #if its the first move it can move two from
        if self.first:
          avalible = True
          for i in pieces[0]:
            if i.pos[0] == self.pos[0] and i.pos[1] == self.pos[1]-80:
              avalible = False
          for i in pieces[1]:
            if i.pos[0] == self.pos[0] and i.pos[1] == self.pos[1]-80:
              avalible = False
          if avalible:
            avalibleMoves.append((self.pos[0],self.pos[1]-80))
      #cheking if a opponent piece is diagonal
      for i in pieces[0]:
        if i.pos[0] == self.pos[0]-40 and i.pos[1] == self.pos[1]-40:
          avalibleMoves.append((self.pos[0]-40,self.pos[1]-40))
        if i.pos[0] == self.pos[0]+40 and i.pos[1] == self.pos[1]-40:
          avalibleMoves.append((self.pos[0]+40,self.pos[1]-40))
    
    elif self.color == 'b':

      #cheking if it is inside of the border:
      if self.pos[1]+40 > 40*8:
        avalible = False

      #cheking if a piece is in front
      for i in pieces[1]:
        if i.pos[0] == self.pos[0] and i.pos[1] == self.pos[1]+40:
          avalible = False
      for i in pieces[0]:
        if i.pos[0] == self.pos[0] and i.pos[1] == self.pos[1]+40:
          avalible = False
      if avalible:
        avalibleMoves.append((self.pos[0],self.pos[1]+40))
        #if its the first move it can move two from
        if self.first:
          avalible = True
          for i in pieces[1]:
            if i.pos[0] == self.pos[0] and i.pos[1] == self.pos[1]+80:
              avalible = False
          for i in pieces[0]:
            if i.pos[0] == self.pos[0] and i.pos[1] == self.pos[1]+80:
              avalible = False
          if avalible:
            avalibleMoves.append((self.pos[0],self.pos[1]+80))
      #cheking if a opponent piece is diagonal
      for i in pieces[1]:
        if i.pos[0] == self.pos[0]-40 and i.pos[1] == self.pos[1]+40:
          avalibleMoves.append((self.pos[0]-40,self.pos[1]+40))
        if i.pos[0] == self.pos[0]+40 and i.pos[1] == self.pos[1]+40:
          avalibleMoves.append((self.pos[0]+40,self.pos[1]+40))

    self.allAvalibleMoves = avalibleMoves
    return avalibleMoves


        

  def Move(self,newPos):
    self.pos = newPos
    self.first = False
   

  def Draw(self, screen):
    #if its black we draw with black skin
    if self.color == 'b':
      screen.blit(self.imgBlack, self.pos)
    #if white we draw with withe skin
    elif self.color == 'w':
      screen.blit(self.imgWhite, self.pos)

    if self.active:
      pygame.draw.rect(screen, (210,210,210), pygame.Rect(self.pos[0]+2, self.pos[1]+2, 36, 36),  3)

#----------------------------#

class Rook():
  
  def __init__(self,x,y,color,active=False):
    self.pos = (x, y)
    self.color = color
    self.identity = 'rook'
    self.imgWhite = pygame.image.load('./chess pieces/rook_white.png')
    self.imgWhite = pygame.transform.scale(self.imgWhite, (40,40))
    self.imgBlack = pygame.image.load('./chess pieces/rook_black.png')
    self.imgBlack = pygame.transform.scale(self.imgBlack, (40,40))
    self.active = active
    self.allAvalibleMoves = []

  def AvalibleMoves(self,pieces):
    avalibleMoves = []
    if self.color == 'w' or self.color == 'b':
      #cheking forward
      run = True
      i = 0

      while run:
        i +=1
        avalible = True

        #cheking if the piece is inside the boarder
        if self.pos[1]+(i*-40) >= 40:

          #cheking if a black piece is in front
          for black in pieces[0]:
            if self.pos[0] == black.pos[0] and self.pos[1]+(i*-40) == black.pos[1]:
              if self.color == 'w':
                avalibleMoves.append((self.pos[0], self.pos[1]+(i*-40)))
              avalible = False
              run = False

          #cheking if a white piece is in front
          for white in pieces[1]:
            if self.pos[0] == white.pos[0] and self.pos[1]+(i*-40) == white.pos[1]:
              if self.color == 'b':
                avalibleMoves.append((self.pos[0], self.pos[1]+(i*-40)))
              run = False
              avalible = False

          if avalible:
            avalibleMoves.append((self.pos[0], self.pos[1]+(i*-40)))
        else:
          run = False
      
      #cheking backwards
      run = True
      i = 0

      while run:
        i +=1
        avalible = True

        #cheking if the piece is inside the boarder
        if self.pos[1]+(i*40) <= 40*8:

          #cheking if a black piece is in front
          for black in pieces[0]:
            if self.pos[0] == black.pos[0] and self.pos[1]+(i*40) == black.pos[1]:
              if self.color == 'w':
                avalibleMoves.append((self.pos[0], self.pos[1]+(i*40)))
              avalible = False
              run = False

          #cheking if a white piece is in front
          for white in pieces[1]:
            if self.pos[0] == white.pos[0] and self.pos[1]+(i*40) == white.pos[1]:
              if self.color == 'b':
                avalibleMoves.append((self.pos[0], self.pos[1]+(i*40)))
              run = False
              avalible = False

          if avalible:
            avalibleMoves.append((self.pos[0], self.pos[1]+(i*40)))
        else:
          run = False

      #cheking to the left
      run = True
      i = 0

      while run:
        i +=1
        avalible = True

        #cheking if the piece is inside the boarder
        if self.pos[0]+(i*-40) >= 40:

          #cheking if a black piece is in front
          for black in pieces[0]:
            if self.pos[0]+(i*-40) == black.pos[0] and self.pos[1] == black.pos[1]:
              if self.color == 'w':
                avalibleMoves.append((self.pos[0]+(i*-40), self.pos[1]))
              avalible = False
              run = False

          #cheking if a white piece is in front
          for white in pieces[1]:
            if self.pos[0]+(i*-40) == white.pos[0] and self.pos[1] == white.pos[1]:
              if self.color == 'b':
                avalibleMoves.append((self.pos[0]+(i*-40), self.pos[1]))
              run = False
              avalible = False

          if avalible:
            avalibleMoves.append((self.pos[0]+(i*-40), self.pos[1]))
        else:
          run = False

      
      #cheking to the right
      run = True
      i = 0

      while run:
        i +=1
        avalible = True

        #cheking if the piece is inside the boarder
        if self.pos[0]+(i*40) <= 40*8:

          #cheking if a black piece is in front
          for black in pieces[0]:
            if self.pos[0]+(i*40) == black.pos[0] and self.pos[1] == black.pos[1]:
              if self.color == 'w':
                avalibleMoves.append((self.pos[0]+(i*40), self.pos[1]))
              avalible = False
              run = False

          #cheking if a white piece is in front
          for white in pieces[1]:
            if self.pos[0]+(i*40) == white.pos[0] and self.pos[1] == white.pos[1]:
              if self.color == 'b':
                avalibleMoves.append((self.pos[0]+(i*40), self.pos[1]))
              run = False
              avalible = False

          if avalible:
            avalibleMoves.append((self.pos[0]+(i*40), self.pos[1]))
        else:
          run = False

    self.allAvalibleMoves = avalibleMoves
    return(avalibleMoves)

  def Move(self,newPos):
    self.pos = newPos


  def Draw(self, screen):
    #if its black we draw with black skin
    if self.color == 'b':
      screen.blit(self.imgBlack, self.pos)
    #if white we draw with withe skin
    elif self.color == 'w':
      screen.blit(self.imgWhite, self.pos)

    if self.active:
      pygame.draw.rect(screen, (210,210,210), pygame.Rect(self.pos[0]+2, self.pos[1]+2, 36, 36),  3)

#----------------------------#

class Bishop():
  
  def __init__(self,x,y,color,active=False):
    self.pos = (x, y)
    self.color = color
    self.identity = 'bishop'
    self.imgWhite = pygame.image.load('./chess pieces/bishop_white.png')
    self.imgWhite = pygame.transform.scale(self.imgWhite, (40,40))
    self.imgBlack = pygame.image.load('./chess pieces/bishop_black.png')
    self.imgBlack = pygame.transform.scale(self.imgBlack, (40,40))
    self.active = active
    self.allAvalibleMoves = []

  def AvalibleMoves(self,pieces):
    avalibleMoves = []
    if self.color == 'w' or self.color == 'b':
      #cheking upwards to the left
      run = True
      i = 0

      while run:
        #cheking upwards to the left
        i +=1
        avalible = True

        #cheking if the piece is inside the boarder
        if self.pos[0]+(i*-40) >= 40 and self.pos[1]+(i*-40) >= 40:

          #Going diagonaly and cheking if a black piece is in front
          for black in pieces[0]:
            if self.pos[0]+(i*-40) == black.pos[0] and self.pos[1]+(i*-40) == black.pos[1]:
              if self.color == 'w':
                avalibleMoves.append((self.pos[0]+(i*-40), self.pos[1]+(i*-40)))
              avalible = False
              run = False

          #Going diagonaly and cheking if a white piece is in front
          for white in pieces[1]:
            if self.pos[0]+(i*-40) == white.pos[0] and self.pos[1]+(i*-40) == white.pos[1]:
              if self.color == 'b':
                avalibleMoves.append((self.pos[0]+(i*-40), self.pos[1]+(i*-40)))
              run = False
              avalible = False

          if avalible:
            avalibleMoves.append((self.pos[0]+(i*-40), self.pos[1]+(i*-40)))
        else:
          run = False
      

      #cheking upwards to the right
      run = True
      i = 0

      while run:
        #cheking upwards to the right
        i +=1
        avalible = True

        #cheking if the piece is inside the boarder
        if self.pos[0]+(i*40) <= 40*8 and self.pos[1]+(i*-40) >= 40:

          #Going diagonaly and cheking if a black piece is in front
          for black in pieces[0]:
            if self.pos[0]+(i*40) == black.pos[0] and self.pos[1]+(i*-40) == black.pos[1]:
              if self.color == 'w':
                avalibleMoves.append((self.pos[0]+(i*40), self.pos[1]+(i*-40)))
              avalible = False
              run = False

          #Going diagonaly and cheking if a white piece is in front
          for white in pieces[1]:
            if self.pos[0]+(i*40) == white.pos[0] and self.pos[1]+(i*-40) == white.pos[1]:
              if self.color == 'b':
                avalibleMoves.append((self.pos[0]+(i*40), self.pos[1]+(i*-40)))
              run = False
              avalible = False

          if avalible:
            avalibleMoves.append((self.pos[0]+(i*40), self.pos[1]+(i*-40)))
        else:
          run = False

      
      #cheking downwards to the right
      run = True
      i = 0

      while run:
        #cheking downwards to the right
        i +=1
        avalible = True

        #cheking if the piece is inside the boarder
        if self.pos[0]+(i*40) <= 40*8 and self.pos[1]+(i*40) <= 40*8:

          #Going diagonaly and cheking if a black piece is in front
          for black in pieces[0]:
            if self.pos[0]+(i*40) == black.pos[0] and self.pos[1]+(i*40) == black.pos[1]:
              if self.color == 'w':
                avalibleMoves.append((self.pos[0]+(i*40), self.pos[1]+(i*40)))
              avalible = False
              run = False

          #Going diagonaly and cheking if a white piece is in front
          for white in pieces[1]:
            if self.pos[0]+(i*40) == white.pos[0] and self.pos[1]+(i*40) == white.pos[1]:
              if self.color == 'b':
                avalibleMoves.append((self.pos[0]+(i*40), self.pos[1]+(i*40)))
              run = False
              avalible = False

          if avalible:
            avalibleMoves.append((self.pos[0]+(i*40), self.pos[1]+(i*40)))
        else:
          run = False

      
      #cheking downwards to the left
      run = True
      i = 0

      while run:
        #cheking downards to the left
        i +=1
        avalible = True

        #cheking if the piece is inside the boarder
        if self.pos[0]+(i*-40) >= 40 and self.pos[1]+(i*40) <= 40*8:

          #Going diagonaly and cheking if a black piece is in front
          for black in pieces[0]:
            if self.pos[0]+(i*-40) == black.pos[0] and self.pos[1]+(i*40) == black.pos[1]:
              if self.color == 'w':
                avalibleMoves.append((self.pos[0]+(i*-40), self.pos[1]+(i*40)))
              avalible = False
              run = False

          #Going diagonaly and cheking if a white piece is in front
          for white in pieces[1]:
            if self.pos[0]+(i*-40) == white.pos[0] and self.pos[1]+(i*40) == white.pos[1]:
              if self.color == 'b':
                avalibleMoves.append((self.pos[0]+(i*-40), self.pos[1]+(i*40)))
              run = False
              avalible = False

          if avalible:
            avalibleMoves.append((self.pos[0]+(i*-40), self.pos[1]+(i*40)))
        else:
          run = False

      self.allAvalibleMoves = avalibleMoves
      return avalibleMoves

  def Move(self,newPos):
    self.pos = newPos

  def Draw(self, screen):
    #if its black we draw with black skin
    if self.color == 'b':
      screen.blit(self.imgBlack, self.pos)
    #if white we draw with withe skin
    elif self.color == 'w':
      screen.blit(self.imgWhite, self.pos)
    
    if self.active:
      pygame.draw.rect(screen, (210,210,210), pygame.Rect(self.pos[0]+2, self.pos[1]+2, 36, 36),  3)

#----------------------------#

class Horse():
  
  def __init__(self,x,y,color, active=False):
    self.pos = (x, y)
    self.color = color
    self.identity = 'horse'
    self.imgWhite = pygame.image.load('./chess pieces/horse_white.png')
    self.imgWhite = pygame.transform.scale(self.imgWhite, (40,40))
    self.imgBlack = pygame.image.load('./chess pieces/horse_black.png')
    self.imgBlack = pygame.transform.scale(self.imgBlack, (40,40))
    self.active = active
    self.allAvalibleMoves = []

  
  def AvalibleMoves(self,pieces):
    avalibleMoves = []

    #doing this if the color is white
    if self.color == 'w' or self.color == 'b':
      
      #all the possible moves for a horse
      HorseMoves = [
        #up
        (self.pos[0]-40, self.pos[1]-80),
        (self.pos[0]+40, self.pos[1]-80),

        #down
        (self.pos[0]-40, self.pos[1]+80),
        (self.pos[0]+40, self.pos[1]+80),

        #right
        (self.pos[0]+80, self.pos[1]-40),
        (self.pos[0]+80, self.pos[1]+40),

        #left
        (self.pos[0]-80, self.pos[1]-40),
        (self.pos[0]-80, self.pos[1]+40)
      ]

      #cheking if the moves are valid
      for i in HorseMoves:
        avalible = True

        #cheking if its inside of the boarder
        if i[0] >= 40 and i[0] <= 40*8 and i[1] >= 40 and i[1] <= 40*8:
          pass
        else:
          avalible = False
        
        #cheking if a white piece is on the spot
        if self.color == 'w':
          for white in pieces[1]:
            if i[0] == white.pos[0] and i[1] == white.pos[1]:
              avalible = False

        #cheking if a black piece is on the spot
        if self.color == 'b':
          for white in pieces[0]:
            if i[0] == white.pos[0] and i[1] == white.pos[1]:
              avalible = False
        
        if avalible:
          avalibleMoves.append(i)

      self.allAvalibleMoves = avalibleMoves
      return avalibleMoves
  
  def Move(self,newPos):
    self.pos = newPos

  def Draw(self, screen):
    #if its black we draw with black skin
    if self.color == 'b':
      screen.blit(self.imgBlack, self.pos)
    #if white we draw with withe skin
    elif self.color == 'w':
      screen.blit(self.imgWhite, self.pos)

  

    if self.active:
      pygame.draw.rect(screen, (210,210,210), pygame.Rect(self.pos[0]+2, self.pos[1]+2, 36, 36),  3)


#----------------------------#


class Queen():
  
  def __init__(self,x,y,color, active=False):
    self.pos = (x, y)
    self.color = color
    self.identity = 'queen'
    self.imgWhite = pygame.image.load('./chess pieces/queen_white.png')
    self.imgWhite = pygame.transform.scale(self.imgWhite, (40,40))
    self.imgBlack = pygame.image.load('./chess pieces/queen_black.png')
    self.imgBlack = pygame.transform.scale(self.imgBlack, (40,40))
    self.active = active
    self.allAvalibleMoves = []

  def AvalibleMoves(self,pieces):
    avalibleMoves = []
    #works with white or black
    if self.color == 'w' or self.color == 'b':
      #cheking upwards to the left
      run = True
      i = 0

      while run:
        #cheking upwards to the left
        i +=1
        avalible = True

        #cheking if the piece is inside the boarder
        if self.pos[0]+(i*-40) >= 40 and self.pos[1]+(i*-40) >= 40:

          #Going diagonaly and cheking if a black piece is in front
          for black in pieces[0]:
            if self.pos[0]+(i*-40) == black.pos[0] and self.pos[1]+(i*-40) == black.pos[1]:
              if self.color == 'w':
                avalibleMoves.append((self.pos[0]+(i*-40), self.pos[1]+(i*-40)))
              avalible = False
              run = False

          #Going diagonaly and cheking if a white piece is in front
          for white in pieces[1]:
            if self.pos[0]+(i*-40) == white.pos[0] and self.pos[1]+(i*-40) == white.pos[1]:
              if self.color == 'b':
                avalibleMoves.append((self.pos[0]+(i*-40), self.pos[1]+(i*-40)))
              run = False
              avalible = False

          if avalible:
            avalibleMoves.append((self.pos[0]+(i*-40), self.pos[1]+(i*-40)))
        else:
          run = False
      

      #cheking upwards to the right
      run = True
      i = 0

      while run:
        #cheking upwards to the right
        i +=1
        avalible = True

        #cheking if the piece is inside the boarder
        if self.pos[0]+(i*40) <= 40*8 and self.pos[1]+(i*-40) >= 40:

          #Going diagonaly and cheking if a black piece is in front
          for black in pieces[0]:
            if self.pos[0]+(i*40) == black.pos[0] and self.pos[1]+(i*-40) == black.pos[1]:
              if self.color == 'w':
                avalibleMoves.append((self.pos[0]+(i*40), self.pos[1]+(i*-40)))
              avalible = False
              run = False

          #Going diagonaly and cheking if a white piece is in front
          for white in pieces[1]:
            if self.pos[0]+(i*40) == white.pos[0] and self.pos[1]+(i*-40) == white.pos[1]:
              if self.color == 'b':
                avalibleMoves.append((self.pos[0]+(i*40), self.pos[1]+(i*-40)))
              run = False
              avalible = False

          if avalible:
            avalibleMoves.append((self.pos[0]+(i*40), self.pos[1]+(i*-40)))
        else:
          run = False

      
      #cheking downwards to the right
      run = True
      i = 0

      while run:
        #cheking downwards to the right
        i +=1
        avalible = True

        #cheking if the piece is inside the boarder
        if self.pos[0]+(i*40) <= 40*8 and self.pos[1]+(i*40) <= 40*8:

          #Going diagonaly and cheking if a black piece is in front
          for black in pieces[0]:
            if self.pos[0]+(i*40) == black.pos[0] and self.pos[1]+(i*40) == black.pos[1]:
              if self.color == 'w':
                avalibleMoves.append((self.pos[0]+(i*40), self.pos[1]+(i*40)))
              avalible = False
              run = False

          #Going diagonaly and cheking if a white piece is in front
          for white in pieces[1]:
            if self.pos[0]+(i*40) == white.pos[0] and self.pos[1]+(i*40) == white.pos[1]:
              if self.color == 'b':
                avalibleMoves.append((self.pos[0]+(i*40), self.pos[1]+(i*40)))
              run = False
              avalible = False

          if avalible:
            avalibleMoves.append((self.pos[0]+(i*40), self.pos[1]+(i*40)))
        else:
          run = False

      
      #cheking downwards to the left
      run = True
      i = 0

      while run:
        #cheking downards to the left
        i +=1
        avalible = True

        #cheking if the piece is inside the boarder
        if self.pos[0]+(i*-40) >= 40 and self.pos[1]+(i*40) <= 40*8:

          #Going diagonaly and cheking if a black piece is in front
          for black in pieces[0]:
            if self.pos[0]+(i*-40) == black.pos[0] and self.pos[1]+(i*40) == black.pos[1]:
              if self.color == 'w':
                avalibleMoves.append((self.pos[0]+(i*-40), self.pos[1]+(i*40)))
              avalible = False
              run = False

          #Going diagonaly and cheking if a white piece is in front
          for white in pieces[1]:
            if self.pos[0]+(i*-40) == white.pos[0] and self.pos[1]+(i*40) == white.pos[1]:
              if self.color == 'b':
                avalibleMoves.append((self.pos[0]+(i*-40), self.pos[1]+(i*40)))
              run = False
              avalible = False

          if avalible:
            avalibleMoves.append((self.pos[0]+(i*-40), self.pos[1]+(i*40)))
        else:
          run = False
      
      #cheking forward
      run = True
      i = 0

      while run:
        i +=1
        avalible = True

        #cheking if the piece is inside the boarder
        if self.pos[1]+(i*-40) >= 40:

          #cheking if a black piece is in front
          for black in pieces[0]:
            if self.pos[0] == black.pos[0] and self.pos[1]+(i*-40) == black.pos[1]:
              if self.color == 'w':
                avalibleMoves.append((self.pos[0], self.pos[1]+(i*-40)))
              avalible = False
              run = False

          #cheking if a white piece is in front
          for white in pieces[1]:
            if self.pos[0] == white.pos[0] and self.pos[1]+(i*-40) == white.pos[1]:
              if self.color == 'b':
                avalibleMoves.append((self.pos[0], self.pos[1]+(i*-40)))
              run = False
              avalible = False

          if avalible:
            avalibleMoves.append((self.pos[0], self.pos[1]+(i*-40)))
        else:
          run = False
      
      #cheking backwards
      run = True
      i = 0

      while run:
        i +=1
        avalible = True

        #cheking if the piece is inside the boarder
        if self.pos[1]+(i*40) <= 40*8:

          #cheking if a black piece is in front
          for black in pieces[0]:
            if self.pos[0] == black.pos[0] and self.pos[1]+(i*40) == black.pos[1]:
              if self.color == 'w':
                avalibleMoves.append((self.pos[0], self.pos[1]+(i*40)))
              avalible = False
              run = False

          #cheking if a white piece is in front
          for white in pieces[1]:
            if self.pos[0] == white.pos[0] and self.pos[1]+(i*40) == white.pos[1]:
              if self.color == 'b':
                avalibleMoves.append((self.pos[0], self.pos[1]+(i*40)))
              run = False
              avalible = False

          if avalible:
            avalibleMoves.append((self.pos[0], self.pos[1]+(i*40)))
        else:
          run = False

      #cheking to the left
      run = True
      i = 0

      while run:
        i +=1
        avalible = True

        #cheking if the piece is inside the boarder
        if self.pos[0]+(i*-40) >= 40:

          #cheking if a black piece is in front
          for black in pieces[0]:
            if self.pos[0]+(i*-40) == black.pos[0] and self.pos[1] == black.pos[1]:
              if self.color == 'w':
                avalibleMoves.append((self.pos[0]+(i*-40), self.pos[1]))
              avalible = False
              run = False

          #cheking if a white piece is in front
          for white in pieces[1]:
            if self.pos[0]+(i*-40) == white.pos[0] and self.pos[1] == white.pos[1]:
              if self.color == 'b':
                avalibleMoves.append((self.pos[0]+(i*-40), self.pos[1]))
              run = False
              avalible = False

          if avalible:
            avalibleMoves.append((self.pos[0]+(i*-40), self.pos[1]))
        else:
          run = False

      
      #cheking to the right
      run = True
      i = 0

      while run:
        i +=1
        avalible = True

        #cheking if the piece is inside the boarder
        if self.pos[0]+(i*40) <= 40*8:

          #cheking if a black piece is in front
          for black in pieces[0]:
            if self.pos[0]+(i*40) == black.pos[0] and self.pos[1] == black.pos[1]:
              if self.color == 'w':
                avalibleMoves.append((self.pos[0]+(i*40), self.pos[1]))
              avalible = False
              run = False

          #cheking if a white piece is in front
          for white in pieces[1]:
            if self.pos[0]+(i*40) == white.pos[0] and self.pos[1] == white.pos[1]:
              if self.color == 'b':
                avalibleMoves.append((self.pos[0]+(i*40), self.pos[1]))
              run = False
              avalible = False

          if avalible:
            avalibleMoves.append((self.pos[0]+(i*40), self.pos[1]))
        else:
          run = False

      self.allAvalibleMoves = avalibleMoves
      return avalibleMoves
    
  def Move(self,newPos):
    self.pos = newPos

  def Draw(self, screen):
    #if its black we draw with black skin
    if self.color == 'b':
      screen.blit(self.imgBlack, self.pos)
    #if white we draw with withe skin
    elif self.color == 'w':
      screen.blit(self.imgWhite, self.pos)

    if self.active:
      pygame.draw.rect(screen, (210,210,210), pygame.Rect(self.pos[0]+2, self.pos[1]+2, 36, 36),  3)

#----------------------------#

class King():
  
  def __init__(self,x,y,color, active=False, check=False):
    self.pos = (x, y)
    self.identity = 'king'
    self.color = color
    self.imgWhite = pygame.image.load('./chess pieces/king_white.png')
    self.imgWhite = pygame.transform.scale(self.imgWhite, (40,40))
    self.imgBlack = pygame.image.load('./chess pieces/king_black.png')
    self.imgBlack = pygame.transform.scale(self.imgBlack, (40,40))
    self.active = active
    self.check = False
    self.checkMate = False
    self.allAvalibleMoves = []

  def AvalibleMoves(self,pieces):
    avalibleMoves = []

    #doing this if the color is white or black
    if self.color == 'w' or self.color == 'b':
      if not self.checkMate:
        #all the possible moves for a king
        KingMoves = [
          #up
          (self.pos[0]-40, self.pos[1]-40),
          (self.pos[0]+40, self.pos[1]-40),
          (self.pos[0], self.pos[1]-40),

          #left right
          (self.pos[0]-40, self.pos[1]),
          (self.pos[0]+40, self.pos[1]),

          #down
          (self.pos[0]-40, self.pos[1]+40),
          (self.pos[0]+40, self.pos[1]+40),
          (self.pos[0], self.pos[1]+40)
        ]

        #cheking if the moves are valid
        for i in KingMoves:
          avalible = True

          #cheking if its inside of the boarder
          if i[0] >= 40 and i[0] <= 40*8 and i[1] >= 40 and i[1] <= 40*8:
            pass
          else:
            avalible = False
          
          #cheking if a white piece is on the spot and if a black can take
          if self.color == 'w':
            for white in pieces[1]:
              if i[0] == white.pos[0] and i[1] == white.pos[1]:
                avalible = False
            for black in pieces[0]:
              for j in black.allAvalibleMoves:
                
                if i[0] == j[0] and i[1] == j[1]:
                  avalible = False

          #cheking if a black piece is on the spot and if a white can take
          if self.color == 'b':
            for white in pieces[0]:
              if i[0] == white.pos[0] and i[1] == white.pos[1]:
                avalible = False
            for white in pieces[1]:
              for j in white.allAvalibleMoves:
                if i[0] == j[0] and i[1] == j[1]:
                  avalible = False
          
          if avalible:
            avalibleMoves.append(i)

      self.allAvalibleMoves = avalibleMoves
      return avalibleMoves

  
  def Move(self,newPos):
    self.pos = newPos
  


  def Draw(self, screen):
    #if its black we draw with black skin
    if self.color == 'b':
      screen.blit(self.imgBlack, self.pos)
    #if white we draw with withe skin
    elif self.color == 'w':
      screen.blit(self.imgWhite, self.pos)

    if self.active:
      pygame.draw.rect(screen, (210,210,210), pygame.Rect(self.pos[0]+2, self.pos[1]+2, 36, 36),  3)