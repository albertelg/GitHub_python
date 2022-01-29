# Import a library of functions called 'pygame'
import pygame
import os

def drawSquare(screen,color):
    # Draw a 3x3 table on the screen
    i=80
    j=262
    wide=5
    inc=60
    for k in range(0,4):
        pygame.draw.line(screen, color, [i, i+inc*k], [j,i+inc*k], wide)
        
    for k in range(0,4):
        pygame.draw.line(screen, color, [i+inc*k,i], [i+inc*k,j], wide)

def drawValues(t,screen,color):
    fontV = pygame.font.Font('freesansbold.ttf', 22) 
    i=100
    inc=60
    for r in range(0,3):
        j=102
        for c in range(0,3):
            text=fontV.render(t[r][c],True,color)
            screen.blit(text, (j,i))
            j=j+inc
        i=i+inc
        
def draw(tauler):
    # set the pygame window position
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (1100,120)
    # Initialize the game engine
    pygame.init()
     
    # Define the colors we will use in RGB format
    BLACK = (  0,   0,   0)
    WHITE = (255, 255, 255)
    BLUE =  (  0,   0, 255)
    GREEN = (  0, 255,   0)
    RED =   (255,   0,   0)
     
    # Set the height and width of the screen
    size = [350, 350]
    screen = pygame.display.set_mode(size,pygame.NOFRAME)
    
    pygame.display.set_caption("3 en ratlla")
    
    # Clear the screen and set the screen background
    screen.fill(WHITE)

    # create a font object. 
    font = pygame.font.Font('freesansbold.ttf', 18) 
      
    # create a text and draw. 
    text = font.render('   1          2          3 ', True, BLACK, WHITE)   
    screen.blit(text, (88,50))
    lind=list('ABC')
    inc=60
    for i in range(0,len(lind)):
        text = font.render(lind[i],True,BLACK,WHITE)
        screen.blit(text,(55,100+i*inc))
    
    drawSquare(screen,GREEN)

    screen.unlock()
    drawValues(tauler,screen,BLACK)
            
    pygame.display.flip()
    #pygame.quit()
    

if __name__=="__main__":
    t=[['X']*3 for i in range(0,3)]
    draw(t)
