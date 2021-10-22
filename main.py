import pygame, sys, random

def ball_animation():

    #include variabels via global (good only in this kind of small programs). In other cases, use return statements or classes.
    global ball_speed_x, ball_speed_y, player_score, opponent_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0:
        player_score += 1
        ball_restart()
    
    
    if ball.right >= screen_width:
        opponent_score += 1
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():

    player.y += player_speed

    if player.top <= 0:
        player.top =0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_ai():

    if opponent.top < ball.y:
            opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))

pygame.init()
clock = pygame.time.Clock()

# Screen size
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Position and size of the ball, player and opponent
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 50, 100, 100)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

# Colors
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)
red = pygame.Color('red')
green = pygame.Color('green')
white = pygame.Color('white')


ball_speed_x = 7 * random.choice((1,-1))

ball_speed_y = 7 * random.choice((1,-1))

player_speed = 0

opponent_speed = 16


# Put some text on the screen
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)




while True:
    for event in pygame.event.get():        

# KEYDOWN = When any key is pressed
# KEYUP = When any key is released
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed +=16
            if event.key == pygame.K_UP:
                player_speed -=16            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -=16
            if event.key == pygame.K_UP:
                player_speed +=16

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        
       
              

    ball_animation()

    player_animation()

    opponent_ai()

    

    screen.fill(bg_color)
    pygame.draw.rect(screen, green, player)
    pygame.draw.rect(screen, red, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, white, (screen_width/2,0), (screen_width/2, screen_height))

    player_text = game_font.render(f"{player_score}",False, white)
    screen.blit(player_text,(660,30))

    opponent_text = game_font.render(f"{opponent_score}",False, white)
    screen.blit(opponent_text,(600,30))

    pygame.display.flip()
    clock.tick(60)