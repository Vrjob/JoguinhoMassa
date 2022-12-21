import pygame
from sys import exit
from random import randint, choice
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()

        if type == 'fly':         
            fly_frame1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
            fly_frame2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
            fly_frame3 = pygame.image.load('graphics/fly/fly3.png').convert_alpha()
            fly_frame4 = pygame.image.load('graphics/fly/fly4.png').convert_alpha()
            self.frame = [fly_frame1, fly_frame2, fly_frame3, fly_frame4, fly_frame3, fly_frame2]
            y_pos = randint(70,210)
            self.speed = randint(4,8)
        if type == 'bat':         
            bat_frame1 = pygame.image.load('graphics/fly/bat1.png').convert_alpha()
            bat_frame2 = pygame.image.load('graphics/fly/bat2.png').convert_alpha()
            bat_frame3 = pygame.image.load('graphics/fly/bat3.png').convert_alpha()
            bat_frame4 = pygame.image.load('graphics/fly/bat4.png').convert_alpha()
            self.frame = [bat_frame1, bat_frame2, bat_frame3, bat_frame4, bat_frame3, bat_frame2]
            y_pos = randint(70,210)
            self.speed = randint(2,3)
        if type == 'snail':
            snail_frame1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_frame2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            snail_frame3 = pygame.image.load('graphics/snail/snail3.png').convert_alpha()
            snail_frame4 = pygame.image.load('graphics/snail/snail4.png').convert_alpha()
            self.frame = [snail_frame1, snail_frame2, snail_frame3, snail_frame4, snail_frame3, snail_frame2]
            y_pos = 300
            self.speed = randint(5,7)
        if type == 'buddy':
            buddy_frame1 = pygame.image.load('graphics/snail/buddy1.png').convert_alpha()
            buddy_frame2 = pygame.image.load('graphics/snail/buddy2.png').convert_alpha()
            buddy_frame3 = pygame.image.load('graphics/snail/buddy3.png').convert_alpha()
            buddy_frame4 = pygame.image.load('graphics/snail/buddy4.png').convert_alpha()
            self.frame = [buddy_frame1, buddy_frame2, buddy_frame3, buddy_frame4, buddy_frame3, buddy_frame2]
            y_pos = 300
            self.speed = 3
        if type == 'worm':
            worm_frame1 = pygame.image.load('graphics/snail/worm1.png').convert_alpha()
            worm_frame2 = pygame.image.load('graphics/snail/worm2.png').convert_alpha()
            worm_frame3 = pygame.image.load('graphics/snail/worm3.png').convert_alpha()
            worm_frame4 = pygame.image.load('graphics/snail/worm4.png').convert_alpha()
            self.frame = [worm_frame1, worm_frame2, worm_frame3, worm_frame4, worm_frame3, worm_frame2]
            y_pos = 310
            self.speed = 4

        self.animation_index = 0

        self.image = self.frame[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos) )

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frame):
            self.animation_index = 0
        self.image = self.frame[int(self.animation_index)]
   
    def update(self):
        self.animation_state()
        self.rect.x -= self.speed
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
class Bomb(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()

        if type == 'bomb':
            bomb_frame1 = pygame.image.load('graphics/player/bomb1.png').convert_alpha()
            bomb_frame2 = pygame.image.load('graphics/player/bomb2.png').convert_alpha()
            bomb_frame3 = pygame.image.load('graphics/player/bomb3.png').convert_alpha()
            bomb_frame4 = pygame.image.load('graphics/player/bomb4.png').convert_alpha()
            self.frame = [bomb_frame1, bomb_frame2, bomb_frame3, bomb_frame4]

            y_pos = randint(70,210)
            
            self.speed = randint(6,9)


        self.animation_index = 0

        self.image = self.frame[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos) )

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frame):
            self.animation_index = 0
        self.image = self.frame[int(self.animation_index)]
   
    def update(self):
        self.animation_state()
        self.rect.x -= self.speed
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

class Item(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()

        if type == 'coin':
            coin_frame1 = pygame.image.load('graphics/player/coin1.png').convert_alpha()
            coin_frame2 = pygame.image.load('graphics/player/coin2.png').convert_alpha()
            coin_frame3 = pygame.image.load('graphics/player/coin3.png').convert_alpha()
            coin_frame4 = pygame.image.load('graphics/player/coin4.png').convert_alpha()
            self.frame = [coin_frame1, coin_frame2, coin_frame3, coin_frame4]
            y_pos = randint(70,210)

            
            self.speed = randint(7,12)
       

        self.animation_index = 0

        self.image = self.frame[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos) )

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frame):
            self.animation_index = 0
        self.image = self.frame[int(self.animation_index)]
   
    def update(self):
        self.animation_state()
        self.rect.x -= self.speed
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

def display_score():
    
    current_time = int((pygame.time.get_ticks() - start_time)/1000)
    score_surf = test_font.render(f"Score: {current_time}", False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 6

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf,obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)


        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return []
def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacle_group:
            if player.colliderect(obstacle_rect): 
                return True
    return False
def collisionsItem(player, itens):
    if itens:
        for itens_rect in item_group:
            if player.colliderect(itens_rect): 
                return True
    return False
def collisionsBomb(player, bombs):
    if bombs:
        for bombs_rect in bomb_group:
            if player.colliderect(bombs_rect): 
                return True
    return False

def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 300:

        player_surf = player_jump3
        if cair:
            player_surf = player_fall
        if jump == 1:
            player_surf = player_jump1
        if jump == 2:
            player_surf = player_jump2    
        
    else:
        player_index += 0.1
        if player_index >= len(player_walk): 
            player_index = 0

        player_surf = player_walk[int(player_index)]
def frame_animation():
    global frame_index, snail_surf, fly_surf, worm_surf, snaka_surf, snakab_surf, buddy_surf, bat_surf
    frame_index += 0.1
    if frame_index >= len(snail_frame): 
        frame_index = 0
    snail_surf = snail_frame[int(frame_index)]
    fly_surf = fly_frame[int(frame_index)]
    worm_surf = worm_frame[int(frame_index)]
    snaka_surf = snaka_frame[int(frame_index)]
    snakab_surf = snakab_frame[int(frame_index)]
    bat_surf = bat_frame[int(frame_index)]
    buddy_surf = buddy_frame[int(frame_index)]
def frameA_animation():
    global framea_index, ground_surface, mud_surface
    framea_index += 0.1
    if framea_index >= len(ground_frame): 
        framea_index = 0
    ground_surface = ground_frame[int(framea_index)]
    mud_surface = mud_frame[int(framea_index)]

gravidade = 1
player_life = 130
imortal = False
blink = False
tipo = 0
item = Item
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Joguinho')
ico = pygame.image.load('graphics/player/player_ico.png').convert_alpha()

pygame.display.set_icon(ico)
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0
#groups
#player =  pygame.sprite.GroupSingle()
#player.add(Player())

obstacle_group = pygame.sprite.Group()
item_group = pygame.sprite.Group()
bomb_group = pygame.sprite.Group()


sky_surface = pygame.image.load('graphics/Sky.png').convert()
sky_rect1 = sky_surface.get_rect(topleft = (0,0))
sky_rect2 = sky_surface.get_rect(topleft = (800,0))

framea_index = 0

ground_frame1 = pygame.image.load('graphics/ground1.png').convert()
ground_frame2 = pygame.image.load('graphics/ground2.png').convert()
ground_frame3 = pygame.image.load('graphics/ground3.png').convert()
ground_frame4 = pygame.image.load('graphics/ground4.png').convert()
ground_frame = [ground_frame1, ground_frame2, ground_frame3, ground_frame4, ground_frame3, ground_frame2]
ground_surface = ground_frame[framea_index]
ground_rect1 = ground_surface.get_rect(topleft = (0,300))
ground_rect2 = ground_surface.get_rect(topleft = (800,300))
blur_surf= pygame.image.load('graphics/blur.png').convert_alpha()
blur_rect= blur_surf.get_rect(topleft = (0,300))
mud_frame1 = pygame.image.load('graphics/mud1.png').convert_alpha()
mud_frame2 = pygame.image.load('graphics/mud2.png').convert_alpha()
mud_frame3 = pygame.image.load('graphics/mud3.png').convert_alpha()
mud_frame4 = pygame.image.load('graphics/mud4.png').convert_alpha()
mud_frame = [mud_frame1, mud_frame2, mud_frame3, mud_frame4, mud_frame1, mud_frame2]
mud_surface = mud_frame[framea_index]
mud_rect = mud_surface.get_rect(topleft = (60,330))


#mosters / obstacles - - - - - - - - - -
frame_index = 0
#Snail  V:4
snail_frame1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_frame2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_frame3 = pygame.image.load('graphics/snail/snail3.png').convert_alpha()
snail_frame4 = pygame.image.load('graphics/snail/snail4.png').convert_alpha()
snail_frame = [snail_frame1, snail_frame2, snail_frame3, snail_frame4, snail_frame3, snail_frame2]
snail_surf = snail_frame[frame_index]
#Fly    V:5
fly_frame1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
fly_frame2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
fly_frame3 = pygame.image.load('graphics/fly/fly3.png').convert_alpha()
fly_frame4 = pygame.image.load('graphics/fly/fly4.png').convert_alpha()
fly_frame = [fly_frame1, fly_frame2, fly_frame3, fly_frame4, fly_frame3, fly_frame2]
fly_surf = fly_frame[frame_index]
#Worm   V:3
worm_frame1 = pygame.image.load('graphics/snail/worm1.png').convert_alpha()
worm_frame2 = pygame.image.load('graphics/snail/worm2.png').convert_alpha()
worm_frame3 = pygame.image.load('graphics/snail/worm3.png').convert_alpha()
worm_frame4 = pygame.image.load('graphics/snail/worm4.png').convert_alpha()
worm_frame = [worm_frame1, worm_frame2, worm_frame3, worm_frame4, worm_frame3, worm_frame2]
worm_surf = worm_frame[frame_index]
#Buddy  V:2
buddy_frame1 = pygame.image.load('graphics/snail/buddy1.png').convert_alpha()
buddy_frame2 = pygame.image.load('graphics/snail/buddy2.png').convert_alpha()
buddy_frame3 = pygame.image.load('graphics/snail/buddy3.png').convert_alpha()
buddy_frame4 = pygame.image.load('graphics/snail/buddy4.png').convert_alpha()
buddy_frame = [buddy_frame1, buddy_frame2, buddy_frame3, buddy_frame4, buddy_frame3, buddy_frame2]
buddy_surf = buddy_frame[frame_index]
#Bat    V:1
bat_frame1 = pygame.image.load('graphics/fly/bat1.png').convert_alpha()
bat_frame2 = pygame.image.load('graphics/fly/bat2.png').convert_alpha()
bat_frame3 = pygame.image.load('graphics/fly/bat3.png').convert_alpha()
bat_frame4 = pygame.image.load('graphics/fly/bat4.png').convert_alpha()
bat_frame = [bat_frame1, bat_frame2, bat_frame3, bat_frame4, bat_frame3, bat_frame2]
bat_surf = bat_frame[frame_index]



obstacle_rect_list = []



snaka_frame1 = pygame.image.load('graphics/snail/snaka1.png').convert_alpha()
snaka_frame2 = pygame.image.load('graphics/snail/snaka2.png').convert_alpha()
snaka_frame = [snaka_frame1, snaka_frame2, snaka_frame1, snaka_frame2, snaka_frame1, snaka_frame2,]
frame_index = 0
snaka_surf = snaka_frame[frame_index]
snaka_rect= snaka_surf.get_rect(topleft = (0,0))

snakab_frame1 = pygame.image.load('graphics/snail/snaka11.png').convert_alpha()
snakab_frame2 = pygame.image.load('graphics/snail/snaka12.png').convert_alpha()
snakab_frame = [snakab_frame1, snakab_frame2, snakab_frame1, snakab_frame2, snakab_frame1, snakab_frame2]
snakab_surf = snakab_frame[frame_index]
snakab_rect= snaka_surf.get_rect(topleft = (0,0))


player_walk1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_walk2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
player_walk3 = pygame.image.load('graphics/player/player_walk_3.png').convert_alpha()
player_walk4 = pygame.image.load('graphics/player/player_walk_4.png').convert_alpha()
player_walk5 = pygame.image.load('graphics/player/player_walk_5.png').convert_alpha()
player_walk = [player_walk1, player_walk2, player_walk3, player_walk4, player_walk5, player_walk4, player_walk3,player_walk2]
player_index = 0

player_jump1 = pygame.image.load('graphics/player/jump1.png').convert_alpha()
player_jump2 = pygame.image.load('graphics/player/jump2.png').convert_alpha()
player_jump3 = pygame.image.load('graphics/player/jump3.png').convert_alpha()
player_fall = pygame.image.load('graphics/player/jump4.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect= player_surf.get_rect(bottomleft = (player_life,300))


imortal_img = pygame.image.load('graphics/player/safe4.png').convert_alpha()
imortal_rect = imortal_img.get_rect(topleft = (0,0))

player_gravity = 0

#intro
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render('Joguinho', False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,70))

game_message = test_font.render('Press Space to run!', False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,340))

#timer
obstacle_timer = pygame.USEREVENT +1
dificuldade = 1000
pygame.time.set_timer(obstacle_timer, dificuldade)

frame_timer = pygame.USEREVENT +2
pygame.time.set_timer(frame_timer, 400)

item_timer = pygame.USEREVENT +3
dificuldadeA = 10000
pygame.time.set_timer(item_timer, dificuldadeA)
dificuldadeB = 15000
bomb_timer = pygame.USEREVENT +4
pygame.time.set_timer(bomb_timer, dificuldadeB)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity = -20     

#movimentos
            if event.type == pygame.KEYDOWN:
                #pulo
                if event.key == pygame.K_UP and vivo and player_rect.bottom == 300:
                    gravidade = 1
                    jump = 1
                    player_gravity = -20
                #agachar
                elif event.key == pygame.K_DOWN and player_rect.bottom < 300:
                    player_gravity = 20
                    cair = True

                #pulo duplo
                elif event.key == pygame.K_UP and player_rect.bottom < 300 and jump == 1:
                    player_gravity = -10
                    jump += 1

                #planar
                elif event.key == pygame.K_UP and player_rect.bottom < 300 and jump == 2:
                    gravidade = 0.1
                    jump += 1

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_rect.midbottom = (player_life,300)
                    countdown = 0
                    game_active = True
                    vivo = True
                    start_time = pygame.time.get_ticks()
        if game_active:
            if event.type == obstacle_timer and game_active and vivo:
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'worm', 'fly', 'snail', 'worm','snail', 'worm', 'bat', 'buddy', 'snail'])))
            if event.type == item_timer and game_active and vivo:
                item_group.add(Item(choice(['coin'])))
            if event.type == bomb_timer and game_active and vivo:
                bomb_group.add(Bomb(choice(['bomb'])))


        player_surf = player_walk[int(player_index)]

    if game_active:
        screen.blit(sky_surface,sky_rect1)
        screen.blit(sky_surface,sky_rect2)
        screen.blit(snakab_surf,snakab_rect)
        screen.blit(ground_surface,ground_rect1)
        screen.blit(ground_surface,ground_rect2)
        score = display_score()
        if vivo:
            ABC = 0


        sky_rect1.left -= 1
        sky_rect2.left -= 1
        if sky_rect1.right <= 0:
            sky_rect1.left = 0 
            sky_rect2.left = 800   
        ground_rect1.left -= 4
        ground_rect2.left -= 4
        if ground_rect1.right <= 0:
            ground_rect1.left = 0 
            ground_rect2.left = 800   
  
        #player
        player_gravity += gravidade
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
            cair = False
        player_animation()
        frameA_animation()
        if vivo:
            frame_animation()
        if player_rect.top <= 20:
            player_rect.top = 20
        screen.blit(player_surf,player_rect)
        #player.draw(screen)
        #player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        item_group.draw(screen)
        item_group.update()
        bomb_group.draw(screen)
        bomb_group.update()
        #collision
        
        if (collisions(player_rect, obstacle_group))and imortal == False:

            player_rect.left -= 20
            countdown = int((pygame.time.get_ticks() - start_time)/1000)
            imortal = True

        if (collisionsItem(player_rect, item_group))and imortal == False:
            if player_rect.left <= 700:
                player_rect.left += 10
            countdown = int((pygame.time.get_ticks() - start_time)/1000)
            imortal = True

        if (collisionsBomb(player_rect, bomb_group))and imortal == False:
            obstacle_rect_list.clear()
            obstacle_group.empty()
            item_group.empty()
            bomb_group.empty()
            countdown = int((pygame.time.get_ticks() - start_time)/1000)
            blink = True
            imortal = True 
            
        if blink:
            screen.fill((255,255,255))
            if (((pygame.time.get_ticks() - start_time)/1000) - countdown) >= 1.0:
                blink = False


        #imortal
        if imortal == True:
            imortal_rect.left = player_rect.left
            imortal_rect.left -= 8
            imortal_rect.top = player_rect.top
            imortal_rect.top -= 2
            screen.blit(imortal_img,imortal_rect)

            imortal_img = pygame.image.load('graphics/player/safe1.png').convert_alpha()
                
            if (((pygame.time.get_ticks() - start_time)/1000) - countdown) >= 1:
                imortal_img = pygame.image.load('graphics/player/safe2.png').convert_alpha()
            if (((pygame.time.get_ticks() - start_time)/1000) - countdown) >= 1.2:
                imortal_img = pygame.image.load('graphics/player/safe3.png').convert_alpha()
            if (((pygame.time.get_ticks() - start_time)/1000) - countdown) >= 1.4:
                imortal_img = pygame.image.load('graphics/player/safe4.png').convert_alpha()
            if (((pygame.time.get_ticks() - start_time)/1000) - countdown) >= 1.6:
                imortal_img = pygame.image.load('graphics/player/safe5.png').convert_alpha()
            if (((pygame.time.get_ticks() - start_time)/1000) - countdown) >= 1.8:
                imortal_img = pygame.image.load('graphics/player/safe6.png').convert_alpha()
            if (((pygame.time.get_ticks() - start_time)/1000) - countdown) >= 2:
                imortal_img = pygame.image.load('graphics/player/safe7.png').convert_alpha()
                imortal = False 

        screen.blit(snaka_surf,snaka_rect)
        screen.blit(mud_surface,mud_rect)
        screen.blit(blur_surf,blur_rect)
        

        #game over
        if player_rect.left < 50:
            imortal = False 
            vivo = False
            ABC += 0.1
            if ABC > 0.3:
                player_rect.bottom = 300
                snaka_surf = pygame.image.load('graphics/snail/snakaa.png').convert_alpha()
                snakab_rect.bottom = 370
                mud_rect.bottom = 337
            if ABC > 0.6:
                snaka_surf = pygame.image.load('graphics/snail/snakab.png').convert_alpha()
                snakab_rect.bottom = 440
                mud_rect.bottom = 332

            if ABC > 0.9:
                snaka_surf = pygame.image.load('graphics/snail/snakac.png').convert_alpha()
                snakab_rect.bottom = 490
                mud_rect.bottom = 327
            if ABC > 1.2:
                snaka_surf = pygame.image.load('graphics/snail/snakad.png').convert_alpha()
                snakab_rect.bottom = 520
                mud_rect.bottom = 322
            if ABC > 1.5:
                snaka_surf = pygame.image.load('graphics/snail/snakae.png').convert_alpha()
                snakab_rect.bottom = 600
                mud_rect.bottom = 317
            if ABC > 8.5:
                game_active = False
                snakab_rect.bottom = 340
                mud_rect.top = 330

    else:
        screen.fill((84,129,162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        obstacle_group.empty()

        score_message = test_font.render(f'Your Score: {score}', False, (111,196,169))
        score_message_rect = score_message.get_rect(center = (400,330))
        screen.blit(game_name,game_name_rect)

        if score == 0:
            screen.blit(game_message,game_message_rect)
        else:
            screen.blit(score_message,score_message_rect)


    pygame.display.update()
    clock.tick(60)


