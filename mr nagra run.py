import pygame
from pygame.locals import *
import time
import random

pygame.init()

width = 1000
height = 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mr Nagra Run")

blue = (0, 0, 225)
red = (255, 0, 0)
purple = (99, 30, 98)
white = (255, 255, 255)
black = (0, 0, 0)

pygame.mixer.music.load("C:/Users/Felix/Downloads/mr nagra run/game theme.mp3")
pygame.mixer.music.play()

font = pygame.font.SysFont("Arial", 30)

clock = pygame.time.Clock()

final_jump_count = 0

# Character Variables
character_x, character_y = 0, 0
ground_y = 0
velocity_y = 0

# Character action variables
gravity = 1.5
jump_height = -24
is_jumping = False

# Boss block variables
block_x, block_y, block_velocity_x, block_velocity_y = 0, 0, 0, 0
active_block = None

##############################################################################################################################################################################

def startscreen():
    
    global begin, selectingcharacters, mouse_released

    startscreen_img = pygame.image.load("C:/Users/Felix/Downloads/mr nagra run/startscreen.jpeg")
    startscreenrect = startscreen_img.get_rect()
    startscreenrect.center = (width // 2, height // 2)
    screen.blit(startscreen_img, startscreenrect)

    startbutton = pygame.image.load('C:/Users/Felix/Downloads/mr nagra run/startbutton.png')
    startbuttonrect = startbutton.get_rect()
    startbuttonrect.topleft = (390, 585)
    
    mouse_pos = pygame.mouse.get_pos()
    if startbuttonrect.collidepoint(mouse_pos):
        buttonselect = pygame.image.load('C:/Users/Felix/Downloads/mr nagra run/startbuttonhover.png')
        screen.blit(buttonselect, startbuttonrect)
    else:
        screen.blit(startbutton, startbuttonrect)
    
    startclick = pygame.mixer.Sound("C:/Users/Felix/Downloads/mr nagra run/gamenoise.mp3")

    if pygame.mouse.get_pressed()[0] and mouse_released:  
        if startbuttonrect.collidepoint(mouse_pos):
            begin = False
            startclick.play()
            selectingcharacters = True
            mouse_released = False

##############################################################################################################################################################################

def character_background():

    character_select = pygame.image.load("C:/Users/Felix/Downloads/mr nagra run/select.jpeg")
    character_selectrect = character_select.get_rect()
    character_selectrect.center = (width // 2, height // 2)
    screen.blit(character_select, character_selectrect)

def choose_characters():

    global selectingcharacters, playinggame, loadgame, characterselection, mouse_released
    global character_x, character_y, ground_y

    clicksound = pygame.mixer.Sound("C:/Users/Felix/Downloads/mr nagra run/click.mp3")
    mouse_pos = pygame.mouse.get_pos()

    omer = pygame.transform.scale(pygame.image.load('C:/Users/Felix/Downloads/mr nagra run/omer.png'), (300, 200))
    screen.blit(omer, (60, 550))
    omerbox = pygame.Rect(210, 580, 120, 100)
    if omerbox.collidepoint(mouse_pos):
        omerselect = pygame.image.load('C:/Users/Felix/Downloads/mr nagra run/omerselect.png')
        smallomerselect = pygame.transform.scale(omerselect, (300, 200))
        screen.blit(smallomerselect, (60, 550))

    if pygame.mouse.get_pressed()[0] and mouse_released:  
        if omerbox.collidepoint(mouse_pos):
            print("omer has been selected")
            selectingcharacters = False
            clicksound.play()
            loadgame = True
            characterselection = "omer"
            mouse_released = False
    
    roger = pygame.transform.scale(pygame.image.load('C:/Users/Felix/Downloads/mr nagra run/roger.png'), (350, 250))
    screen.blit(roger, (195, 510))
    rogerbox = pygame.Rect(350, 580, 120, 100)
    if rogerbox.collidepoint(mouse_pos):
        rogerselect = pygame.image.load('C:/Users/Felix/Downloads/mr nagra run/rogerselect.png')
        smallrogerselect = pygame.transform.scale(rogerselect, (350, 250))
        screen.blit(smallrogerselect, (195, 510))
    
    if pygame.mouse.get_pressed()[0] and mouse_released:  
        if rogerbox.collidepoint(mouse_pos):
            print("roger has been selected")
            selectingcharacters = False
            clicksound.play()
            loadgame = True
            characterselection = "roger"
            mouse_released = False

    billy = pygame.transform.scale(pygame.image.load("C:/Users/Felix/Downloads/mr nagra run/billy.png"), (300, 200))
    screen.blit(billy, (405, 562))
    billybox = pygame.Rect(490, 580, 120, 100)
    if billybox.collidepoint(mouse_pos):
        billyselect = pygame.image.load('C:/Users/Felix/Downloads/mr nagra run/billyselect.png')
        smallbillyselect = pygame.transform.scale(billyselect, (300, 200))
        screen.blit(smallbillyselect, (405, 562))

    if pygame.mouse.get_pressed()[0] and mouse_released:  
        if billybox.collidepoint(mouse_pos):
            print("billy has been selected")
            selectingcharacters = False
            clicksound.play()
            loadgame = True
            characterselection = "billy"
            mouse_released = False

    rushaan = pygame.transform.scale(pygame.image.load('C:/Users/Felix/Downloads/mr nagra run/rushaan.png'), (300, 200))
    screen.blit(rushaan, (520, 532))
    rushaanbox = pygame.Rect(630, 580, 120, 100)
    if rushaanbox.collidepoint(mouse_pos):
        rushaanselect = pygame.image.load('C:/Users/Felix/Downloads/mr nagra run/rushaanselect.png')
        smallrushaanselect = pygame.transform.scale(rushaanselect, (300, 200))
        screen.blit(smallrushaanselect, (520, 532))
    
    if pygame.mouse.get_pressed()[0] and mouse_released:  
        if rushaanbox.collidepoint(mouse_pos):
            print("rushaan has been selected")
            selectingcharacters = False
            clicksound.play()
            loadgame = True
            characterselection = "rushaan"
            mouse_released = False

    saif = pygame.transform.scale(pygame.image.load('C:/Users/Felix/Downloads/mr nagra run/saif.png'), (540, 340))
    screen.blit(saif, (585, 490))
    saifbox = pygame.Rect(770, 580, 120, 100)
    if saifbox.collidepoint(mouse_pos):
        saifselect = pygame.image.load('C:/Users/Felix/Downloads/mr nagra run/saifselect.png')
        smallsaifselect = pygame.transform.scale(saifselect, (540, 340))
        screen.blit(smallsaifselect, (585, 490))
    
    if pygame.mouse.get_pressed()[0] and mouse_released:  
        if saifbox.collidepoint(mouse_pos):
            print("saif has been selected")
            selectingcharacters = False
            clicksound.play()
            loadgame = True
            characterselection = "saif"
            mouse_released = False

##############################################################################################################################################################################

def gamebackground():
    background = pygame.image.load('C:/Users/Felix/Downloads/mr nagra run/background.jpg')
    backgroundrect = background.get_rect()
    backgroundrect.center = (width // 2, height // 2)
    screen.blit(background, backgroundrect)

##############################################################################################################################################################################

# Powerup variables
active_powerup = None 
powerup_timer = 0

plusfive_pic = pygame.transform.scale(pygame.image.load("C:/Users/Felix/Downloads/mr nagra run/coin.png"), (250,250) )
highjump_pic = pygame.transform.scale(pygame.image.load("C:/Users/Felix/Downloads/mr nagra run/highjump.png"), (250,250) )

powerups = ["plusfive", "highjump"]

def activate_powerup(powerup):

    global final_jump_count, jump_height, powerup_timer, active_powerup

    if powerup == "plusfive":
        final_jump_count += 5
        powerup_timer = pygame.time.get_ticks()
        active_powerup = "plusfive"
    elif powerup == "highjump":
        jump_height = -30
        powerup_timer = pygame.time.get_ticks()
        active_powerup = "highjump"

def check_powerup():

    global active_powerup, jump_height, elapsed_time

    if active_powerup == "plusfive":
        elapsed_time = pygame.time.get_ticks() - powerup_timer
        print(elapsed_time)
        if elapsed_time > 2000:
            active_powerup = None
    elif active_powerup == "highjump":
        elapsed_time = pygame.time.get_ticks() - powerup_timer
        if elapsed_time > 4000:
            jump_height = -24
            active_powerup = None

def display_powerup():

    global activate_powerup

    if active_powerup == "plusfive":
        screen.blit(plusfive_pic, (400, 100))
    elif active_powerup == "highjump":
        screen.blit(highjump_pic, (400, 200))

##############################################################################################################################################################################

def set_character_pos():

    global playinggame, loadgame
    global character_positions, character_x, character_y, ground_y, velocity_y, gravity, jump_height, is_jumping, block_x, block_y,  block_velocity_x, block_velocity_y, active_block, character, player_rect

    character_x, character_y = 0, 0
    ground_y = 0
    velocity_y = 0

    # Character action variables
    gravity = 1.5
    jump_height = -24
    is_jumping = False

    # Boss block variables
    block_x, block_y, block_velocity_x, block_velocity_y = 0, 0, 0, 0
    active_block = None

    character_positions = {
        "omer": [98, 492, 492],
        "roger": [98, 455, 455],
        "billy": [165, 505, 505],
        "rushaan": [142, 480, 480],
        "saif": [60, 435, 435],
        }
    
    if characterselection == "omer":
        character = pygame.transform.scale(pygame.image.load('C:/Users/Felix/Downloads/mr nagra run/omer.png'), (300, 200))
        character_x, character_y, ground_y = character_positions["omer"]
        loadgame = False
        playinggame = True
    elif characterselection == "roger":
        character = pygame.transform.scale(pygame.image.load('C:/Users/Felix/Downloads/mr nagra run/roger.png'), (350, 250))
        character_x, character_y, ground_y = character_positions["roger"]
        loadgame = False
        playinggame = True
    elif characterselection == "billy":
        character = pygame.transform.scale(pygame.image.load('C:/Users/Felix/Downloads/mr nagra run/billy.png'), (300, 200))
        character_x, character_y, ground_y = character_positions["billy"]
        loadgame = False
        playinggame = True
    elif characterselection == "rushaan":
        character = pygame.transform.scale(pygame.image.load('C:/Users/Felix/Downloads/mr nagra run/rushaan.png'), (300, 200))
        character_x, character_y, ground_y = character_positions["rushaan"]
        loadgame = False
        playinggame = True
    elif characterselection == "saif":
        character = pygame.transform.scale(pygame.image.load('C:/Users/Felix/Downloads/mr nagra run/saif.png'), (540, 340))
        character_x, character_y, ground_y = character_positions["saif"]
        loadgame = False
        playinggame = True

def startgame():

    global character_x, character_y, velocity_y, jump_height, is_jumping, character, player_rect, final_jump_count, active_powerup
    
    if characterselection == "omer":
        player_rect = pygame.Rect(character_x + 176, character_y + 5, 64, 114)
    elif characterselection == "roger":
        player_rect = pygame.Rect(character_x + 176.5, character_y + 50, 58, 110)
    elif characterselection == "billy":
        player_rect = pygame.Rect(character_x + 112, character_y + 5, 60, 105)
    elif characterselection == "rushaan":
        player_rect = pygame.Rect(character_x + 130, character_y + 30, 68, 106)
    elif characterselection == "saif":
        player_rect = pygame.Rect(character_x + 210, character_y + 76, 68, 106)
    
    screen.blit(character, (character_x, character_y))

    jumpnoise = pygame.mixer.Sound("C:/Users/Felix/Downloads/mr nagra run/jump.mp3")

    keys = pygame.key.get_pressed()

    if not is_jumping and (keys[pygame.K_UP] or keys[pygame.K_SPACE]):
        velocity_y = jump_height
        final_jump_count += 1
        jumpnoise.play()
        is_jumping = True

    if is_jumping:
        velocity_y += gravity
        character_y += velocity_y
    if character_y >= ground_y:
        character_y = ground_y
        is_jumping = False
    
    powerup_intervals = [10, 20, 40, 60, 80, 100, 140, 180, 250]
    powerup_intervals += [i for i in range(300, final_jump_count + 1, 50)]

    if final_jump_count in powerup_intervals and active_powerup is None:
        activate_powerup(random.choice(powerups))

    display_powerup()
    check_powerup()
    
    jump_text = font.render(f"Jumps: {final_jump_count}", True, black)
    screen.blit(jump_text, (10, 40))

def boss():

    global playinggame, deathscreen
    global active_block, block_x, block_y, block_velocity_x, block_velocity_y, block_speed_multiplier, player_rect, active_powerup 

    nagra = pygame.transform.scale(pygame.image.load("C:/Users/Felix/Downloads/mr nagra run/nagra.png"), (300, 500))
    screen.blit(nagra, (785, 200))

    block_images = [
        pygame.transform.rotate(pygame.transform.scale(pygame.image.load("C:/Users/Felix/Downloads/mr nagra run/block1.png"), (100, 70)), 25),
        pygame.transform.rotate(pygame.transform.scale(pygame.image.load("C:/Users/Felix/Downloads/mr nagra run/block2.png"), (100, 70)), 25),
        pygame.transform.rotate(pygame.transform.scale(pygame.image.load("C:/Users/Felix/Downloads/mr nagra run/block3.png"), (100, 70)), 25)
    ]

    shotsound = pygame.mixer.Sound("C:/Users/Felix/Downloads/mr nagra run/shot.mp3")
    
    if active_block is None:
        active_block = random.choice(block_images)
        shotsound.play()
        block_x = 800
        block_y = 520
        block_velocity_x = -10
        block_speed_multiplier = 1

    if final_jump_count >= 100:
        num = (final_jump_count - 100) // 50 + 1
        if num > 6:
            num = 6
        else:
            speed = 0.01 * num
            block_speed_multiplier += 0.10 + speed
    elif final_jump_count >= 60:
        block_speed_multiplier += 0.08
    elif final_jump_count >= 30:
        block_speed_multiplier += 0.07
    elif final_jump_count >= 10:
        block_speed_multiplier += 0.05
    else:
        block_speed_multiplier += 0.04

    block_velocity_x = -10 * block_speed_multiplier
    block_x += block_velocity_x

    screen.blit(active_block, (block_x, block_y))

    if block_x + 100 < 0:
        active_block = None

    block_rect = pygame.Rect(block_x, block_y, 100, 70)

    death = pygame.mixer.Sound("C:/Users/Felix/Downloads/mr nagra run/death.mp3")
    
    if player_rect.colliderect(block_rect):
        death.play()
        active_block = None
        active_powerup = None
        playinggame = False
        deathscreen = True
        block_speed_multiplier = 1

##############################################################################################################################################################################

def playagain():

    global deathscreen, playinggame, selectingcharacters, running, loadgame, final_jump_count, characterselection

    screen.fill(white)
    gameoverscreen = pygame.image.load("C:/Users/Felix/Downloads/mr nagra run/gameoverscreen.png")
    gameoverscreenrect = gameoverscreen.get_rect()
    gameoverscreenrect.center = (width // 2, height // 2)
    screen.blit(gameoverscreen, gameoverscreenrect)

   
    final_jump_text = font.render(f"Final Jumps: {final_jump_count}", True, black)
    screen.blit(final_jump_text, ((width - final_jump_text.get_width()) // 2 + 30, height // 2 + 40))

    keys = pygame.key.get_pressed()

    if keys[K_r]:
        deathscreen = False
        loadgame = True
        final_jump_count = 0  
    if keys[K_c]:
        deathscreen = False
        playinggame = False
        characterselection = None
        selectingcharacters = True
        final_jump_count = 0 
    if keys[K_q]:
        running = False 

##############################################################################################################################################################################

begin, mouse_released = True, True

characterselection, selectingcharacters, loadgame, playinggame, deathscreen = False, False, False, False, False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:  
            mouse_released = True

    if begin:
        startscreen()

    if selectingcharacters:
        character_background()
        choose_characters()
    
    if loadgame:
        set_character_pos()

    if playinggame:
        gamebackground()
        startgame()
        boss()

    if deathscreen:
        playagain()

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
