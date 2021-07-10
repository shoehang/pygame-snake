#BASIC SNAKE GAME w PYGAME
#referencing rajatdiptabiswas/Snake Game.py

import pygame, time, random, sys

def main():   
    #INITIALIZE SCREEN
    pygame.init()
    width = 500
    height = 500
    surface = pygame.display.set_mode((width, height))
    pygame.display.set_caption('snaPy')
    clock = pygame.time.Clock()
    
    #SNAKE VALUES
    collision = False
    position = [width/2, height/2]
    direction = 'RIGHT'
    snakebody = [[width/2, height/2], [(width/2)-10, height/2], [(width/2)-20, height/2]]
    
    #FOOD VALUES
    foodpos = [random.randrange(0,width,10), random.randrange(0,height,10)]
    foodspawn = True
    
    #SCORE VALUE
    score = 0
    
    while True:
        #FETCH EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            #SNAKE MOVEMENTS KEYPRESS
            elif event.type == pygame.KEYDOWN:
                #DIRECTIONAL KEYS
                if event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                if event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                if event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'
        if direction == 'UP': position[1] -= 10
        if direction == 'DOWN': position[1] += 10
        if direction == 'LEFT': position[0] -= 10
        if direction == 'RIGHT': position[0] += 10
        
        #SNAKE MOVEMENTS
        snakebody.insert(0, [position[0],position[1]])
        if position[0] == foodpos[0] and position[1] == foodpos[1]:
            snakebody.insert(0,[position[0], position[1]])
            foodspawn = False
            score += 1
        else:
            snakebody.pop()
        
        #DRAW TO SURFACE
        surface.fill((255, 255, 255))
        #SNAKE
        for segment in snakebody:
            pygame.draw.rect(surface, (200, 200, 200), pygame.Rect(segment[0]+3, segment[1]+3, 10, 10))
            pygame.draw.rect(surface, (173, 201, 194), pygame.Rect(segment[0], segment[1], 10, 10))
        #FOOD
        if not foodspawn:
            foodpos = [random.randrange(0,width,10), random.randrange(0,height,10)]
        foodspawn = True
        pygame.draw.rect(surface, (200, 200, 200), pygame.Rect(foodpos[0]+3, foodpos[1]+3, 10, 10))
        pygame.draw.rect(surface, (255, 200, 100), pygame.Rect(foodpos[0], foodpos[1], 10, 10))
        
        #COLLISION(WALL/BODY)
        if position[0] < 0 or position[0] > 500 or position[1] < 0 or position[1] > 500:
            collision = True
            time.sleep(1)
        for segment in snakebody[2:]:
            if position[0] == segment[0] and position[1] == segment[1]:
                collision = True
                time.sleep(1)
        if collision:
            gameoverfont = pygame.font.SysFont('courier', 60)
            gameovertext = gameoverfont.render('Game Over', True, (0, 0, 0))
            gameoverrect = gameovertext.get_rect()
            gameoverrect.midtop = (width/2, height/2)
            surface.fill((200, 150, 150))
            surface.blit(gameovertext, gameoverrect)
        
        #SCORE
        font = pygame.font.SysFont('courier', 25)
        textsurface = font.render('score: ' + str(score), True, (20,20,20))
        font2 = pygame.font.SysFont('courier', 25)
        textsurface2 = font2.render('score: ' + str(score), True, (200,200, 200))
        surface.blit(textsurface2, (33, 23))
        surface.blit(textsurface, (30, 20))

        #REFRESH SCREEN
        pygame.display.update()
        clock.tick(18)

if __name__ == '__main__':
    main()