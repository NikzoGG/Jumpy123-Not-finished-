import pygame
from showthings import showlevel1,showplayer,hidemenuitems,stopgame,hideverything,showkeys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Jump')
clock = pygame.time.Clock()


#loadvane na font za pisane
text_font1 = pygame.font.Font('assets/fonts/score.ttf',60)
text_font2 = pygame.font.Font('assets/fonts/score.ttf',20)

#suzdavane na funkciq za pishene na tekst
def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))


#loading buttons
sure = pygame.image.load('assets/graphics/sure.png')
sure_rect = sure.get_rect(midbottom=(3000,3000))

returnbutton = pygame.image.load('assets/graphics/return.png')
returnbutton_rect = returnbutton.get_rect(midbottom=(3000,3000))

yes1 = pygame.image.load('assets/graphics/yes1.png')
yes1_rect = yes1.get_rect(midbottom=(3000,3000))

yes2 = pygame.image.load('assets/graphics/yes2.png')
yes2_rect = yes2.get_rect(midbottom=(3000,3000))

#keys
key1 = pygame.image.load('assets/graphics/levels/level1/specialitems/key1.png')
key1_rect = key1.get_rect(midbottom=(3000,3000))

#loading icons
potionicon1 = pygame.image.load('assets/graphics/npc_interactives/speedpotionshopicon.png')
potionicon1_rect = potionicon1.get_rect(midbottom=(3000,3000))

potionicon2 = pygame.image.load('assets/graphics/npc_interactives/jumppotionshopicon.png')
potionicon2_rect = potionicon2.get_rect(midbottom=(3000,3000))

speedpotioninventory = pygame.image.load('assets/graphics/npc_interactives/speedpotioninventory.png')
speedpotioninventory_rect = speedpotioninventory.get_rect(midbottom=(3000,3000))

jumppotioninventory = pygame.image.load('assets/graphics/npc_interactives/jumppotioninventory.png')
jumppotioninventory_rect = jumppotioninventory.get_rect(midbottom=(3000,3000))


#loading safe room
saferoom = pygame.image.load('assets/graphics/levels/saferoom/saferoom.png')
saferoom_rect = saferoom.get_rect(midbottom=(3000,3000))


#loading menubackground
menubg = pygame.image.load('assets/graphics/bg.jpg')
menubg_rect = menubg.get_rect(midbottom=(600,800))

#loading potion menu shop
potionmenu = pygame.image.load('assets/graphics/npc_interactives/menushop.png')
potionmenu_rect = potionmenu.get_rect(midbottom=(3000,3000))

#loading startbg
startbg = pygame.image.load('assets/graphics/startbg.png')
startbg_rect = startbg.get_rect(midbottom=(3000,3000))


#loading enemies
ghost1 = pygame.image.load('assets/graphics/ghost1.png')
ghost1_rect = ghost1.get_rect(midbottom=(3000,3000))


#loading ground
ground = pygame.image.load('assets/graphics/ground.png')
ground_rect = ground.get_rect(midbottom=(3000,3000))


#loading wizards
wizard = pygame.image.load('assets/graphics/levels/level2/wizard.png')
wizard_rect = wizard.get_rect(midbottom=(3000,3000))

#loading menu buttons
start = pygame.image.load('assets/graphics/start.png')
start_rect = start.get_rect(midbottom=(600,300))
quit = pygame.image.load('assets/graphics/quit.png')
quit_rect = quit.get_rect(midbottom=(600,380))


#loading gems
gem1 = pygame.image.load('assets/graphics/levels/level1/gems/gem1.png')
gem1_rect = gem1.get_rect(midbottom=(10000,10000))


#loading platforms
platform1 = pygame.image.load('assets/graphics/levels/level1/platforms/platform1.png')
platform1_rect = platform1.get_rect(midbottom=(3000,3000))
platform2 = pygame.image.load('assets/graphics/levels/level1/platforms/platform2.png')
platform2_rect = platform2.get_rect(midbottom=(3000,3000))
platform3 = pygame.image.load('assets/graphics/levels/level1/platforms/platform3.png')
platform3_rect = platform3.get_rect(midbottom=(3000,3000))
platform4 = pygame.image.load('assets/graphics/levels/level1/platforms/platform4.png')
platform4_rect = platform4.get_rect(midbottom=(3000,3000))
platform5 = pygame.image.load('assets/graphics/levels/level1/platforms/platform5.png')
platform5_rect = platform5.get_rect(midbottom=(3000,3000))

#loading dead screen
deadscreen = pygame.image.load('assets/graphics/dead.png')
deadscreen_rect = deadscreen.get_rect(midbottom=(3000,3000))

#loading inventory image
inventory_1 = pygame.image.load('assets/graphics/inventory_1.png')
inventory_1_rect = inventory_1.get_rect(midbottom=(3000,3000))

#loading safe room things
seller = pygame.image.load('assets/graphics/sell_guy.png')
seller_rect = seller.get_rect(midbottom=(3000,3000))

#loading doors
door1 = pygame.image.load('assets/graphics/levels/level1/specialitems/door1.png')
door1_rect = door1.get_rect(midbottom=(3000,3000))


#loading bricks
brick1 = pygame.image.load('assets/graphics/levels/level1/bricks/brick1.png')
brick1_rect = brick1.get_rect(midbottom=(3000,3000))

#loading clouds
cloud1 = pygame.image.load('assets/graphics/cloud1.png')
cloud1_rect = cloud1.get_rect(midbottom=(3000,3000))

#loading player
player = pygame.image.load('assets/graphics/player.png')
player_rect = player.get_rect(midbottom=(3000,3000))


#game variables
gamestarted = False
cloud_speed = 3
score = 0
gem1collected = False
level = 0
tabpress = 0
speedpotion = False
speedpotionnumber = 0
jumppotion = False
jumppotionnumber = 0
showseller = False
playercollidedwithseller = False
timer1 = 0
playerclicked1 = False
deadghost = False
timer2 = 0
playerclicked2 = False
timer3 = 0
timer4 = 0
playerclicked3 = False
timer5 = 0
playerclicked4 = False
timer6 = 0
showkey1 = True
doorkey = 0
collidedwithwizard = False
shootingability = False

#player variables
player_speed = 7
player_gravity = 0
deadplayer = False
movingleft = False
movingright = False
player_health = 100
vel2 = 19

running = True
while running:
    #activates user input
    keys = pygame.key.get_pressed()

    #getting mouse pos
    mousepos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #for loop key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.colliderect(ground_rect):
                player_gravity -= vel2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.colliderect(platform1_rect) and player_rect.y == 435:
                player_gravity -= vel2    

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.colliderect(platform3_rect) and player_rect.y == 290:
                player_gravity -= vel2 
            
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.colliderect(platform4_rect) and player_rect.y == 290:
                player_gravity -= vel2 
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.colliderect(platform5_rect) and player_rect.y == 290:
                player_gravity -= vel2 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.colliderect(platform2_rect) and player_rect.y == 435:
                player_gravity -= vel2

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.colliderect(cloud1_rect) and player_rect.y == 158:
                player_gravity -= vel2

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.colliderect(saferoom_rect) and player_rect.y == 611:
                player_gravity = -19

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB and (level == 1 or level == -2 or level == 2):
                tabpress += 1
        

    #managing buttons
    if quit_rect.collidepoint(mousepos):
        if pygame.mouse.get_pressed()[0] == 1:
            running = False
    if start_rect.collidepoint(mousepos):
        if pygame.mouse.get_pressed()[0] == 1:
            gamestarted = True
            showlevel1(gem1_rect,ground_rect,platform1_rect,cloud1_rect,startbg_rect,brick1_rect,platform2_rect,ghost1_rect,platform3_rect,platform4_rect,platform5_rect)
            level = 1
            showplayer(player_rect)
            hidemenuitems(quit_rect,menubg_rect,start_rect)
    #gravity
    if gamestarted == True:       
        player_gravity += 1
        player_rect.y += player_gravity
    if player_rect.colliderect(ground_rect):
        player_rect.y = 611
        player_gravity = -1
    if player_rect.colliderect(platform1_rect):
        if player_rect.y == 435:
            player_gravity = -1
        else:
            player_gravity = 0
    if player_rect.colliderect(platform2_rect):
        if player_rect.y == 435:
            player_gravity = -1
        else:
            player_gravity = 0
    
    if player_rect.colliderect(platform3_rect):
        if player_rect.y == 290:
            player_gravity = -1
        else:
            player_gravity = 0
    
    if player_rect.colliderect(platform4_rect):
        if player_rect.y == 290:
            player_gravity = -1
        else:
            player_gravity = 0

    if player_rect.colliderect(platform5_rect):
        if player_rect.y == 290:
            player_gravity = -1
        else:
            player_gravity = 0

    if player_rect.colliderect(platform5_rect) and jumppotion == True:
        if player_rect.y == 290:
            pass                                                          #- tova e za da moje kogato playerut skacha na visoko s jump potion da ne pada nadolu a da stoi vurhu platformite na platform2
        else:
            player_gravity = -1

    if player_rect.colliderect(platform3_rect) and jumppotion == True:
        player_rect.y = 290
                                                                            #- tova e za da moje playerut kato skochi ot zemqta i padne vurhy platformite na platform2 da ne pada nadolu
    if player_rect.colliderect(platform4_rect) and jumppotion == True:
        player_rect.y = 290

    if player_rect.colliderect(platform5_rect) and jumppotion == True:
        player_rect.y = 290
    

    if player_rect.colliderect(ghost1_rect) and player_rect.colliderect(ground_rect) == False:
        touching_ghost = True
        player_gravity = -1
        deadghost = True
        score += 300
    elif player_rect.colliderect(ghost1_rect) and player_rect.colliderect(ground_rect):
        stopgame(gem1_rect,ground_rect,platform1_rect,cloud1_rect,startbg_rect,brick1_rect,platform2_rect,ghost1_rect,player_rect)
        deadplayer = True
    else:
        touching_ghost = False
    
    #letqshti objecti
    if player_rect.colliderect(cloud1_rect) and movingleft == False and movingright == False and player_rect.y == 158:
        player_gravity = -1 
        player_rect.x = cloud1_rect.x + 20
    elif movingleft == True and movingright == True and player_rect.colliderect(cloud1_rect) and player_rect.y == 158:
        pass

    #inventory closing
    if tabpress == 1:
        inventory_1_rect.x = 100
        inventory_1_rect.y = 100

    if tabpress == 2:
        inventory_1_rect.x = 3000
        inventory_1_rect.y = 3000
        tabpress = 0

    if tabpress == 1 and speedpotionnumber > 0:
        speedpotioninventory_rect.x = 100
        speedpotioninventory_rect.y = 100
    else:
        speedpotioninventory_rect.x = 3000
        speedpotioninventory_rect.y = 3000

    if tabpress == 1 and jumppotionnumber > 0:
        jumppotioninventory_rect.x = 100
        jumppotioninventory_rect.y = 140
    else:
        jumppotioninventory_rect.x = 3000
        jumppotioninventory_rect.y = 3000
    
    #saferoom gravity
    if player_rect.colliderect(saferoom_rect):
        if player_rect.y == 611:
            player_gravity = -1


    #kogato playera skoche ot visoko da ne zastava vutre doly v zemqta a da stoi vurhy neq!
    if player_rect.y == 611 and player_rect.colliderect(ground_rect):
        player_rect.y = 611

    #kogato playera skoche ot visoko da ne zastava vutre v ghosta a da e nad nego
    if player_rect.y == 557 and touching_ghost == True:
        player_rect.y = 557

    #movement
    if keys[pygame.K_a]:
        movingleft = True
        player_rect.x -= player_speed
    else:
        movingleft = False
    if keys[pygame.K_d]:
        movingright = True
        player_rect.x += player_speed  
    else:
        movingright = False       
    if player_rect.x < -4:
        player_rect.x = -4
    if player_rect.x > 1246:
        player_rect.x = 1246  

    #clouds movement
    if gamestarted == True:
        cloud1_rect.x += cloud_speed
    if cloud1_rect.x == 1224:
        cloud1_rect.x = -30


    #key logic    
    if showkey1 == True:
        showkeys(key1_rect)
        key1_rect.y = 280
        key1_rect.x = 700
    else:
        key1_rect.y = 3000
        key1_rect.x = 3000

    if player_rect.colliderect(key1_rect):
        showkey1 = False
        doorkey += 1
    

    #handling buttons
    if keys[pygame.K_l] and (level == 1 or level == 2):
        sure_rect.x = 340
        sure_rect.y = 10
        yes1_rect.x = 550
        yes1_rect.y = 250
    else:
        sure_rect.x = 3000
        sure_rect.y = 3000
        yes1_rect.x = 3000
        yes1_rect.y = 3000

    if keys[pygame.K_p] and level == -2:
        returnbutton_rect.x = 340
        returnbutton_rect.y = 10
        yes2_rect.x = 550
        yes2_rect.y = 250
    else:
        returnbutton_rect.x = 3000
        returnbutton_rect.y = 3000
        yes2_rect.x = 3000
        yes2_rect.y = 3000

    if yes1_rect.collidepoint(mousepos):
        if pygame.mouse.get_pressed()[0] == 1:
            level = -2
            player_rect.x = 35
            player_rect.y = 611
            hideverything(ground_rect,ghost1_rect,startbg_rect,cloud1_rect,brick1_rect,platform1_rect,platform2_rect,platform3_rect,platform4_rect,platform5_rect)

    if yes2_rect.collidepoint(mousepos):
        if pygame.mouse.get_pressed()[0] == 1:
            level = 1
            ground_rect.x = 0
            ground_rect.y = 650
            platform1_rect.x = 350
            platform1_rect.y = 473
            platform2_rect.x = 445
            platform2_rect.y = 473
            cloud1_rect.x = -30
            cloud1_rect.y = 200
            startbg_rect.x = 0
            startbg_rect.y = 0
            brick1_rect.x = 393
            brick1_rect.y = 475
            platform3_rect.x = 670
            platform3_rect.y = 330
            platform4_rect.x = 720
            platform4_rect.y = 330
            platform5_rect.x = 770
            platform5_rect.y = 330
            showplayer(player_rect)
            if deadghost == False:
                ghost1_rect.x = 700
                ghost1_rect.y = 600

    if deadghost == True:
        ghost1_rect.x = 3000
        ghost1_rect.y = 3000


    if level == 1:
        saferoom_rect.x = 3000
        saferoom_rect.y = 3000
        showseller = False
    if level == -2:
        saferoom_rect.x = 0
        saferoom_rect.y = 0
        showseller = True
        

    if showseller == True:
        seller_rect.x = 1000
        seller_rect.y = 540
    else:
        seller_rect.x = 3000
        seller_rect.y = 3000
    

    #showing gems
    if player_rect.colliderect(brick1_rect) and gem1collected == False and player_rect.y == 513:
        gem1_rect.x = 390
        gem1_rect.y = 370

    #managing gems
    if player_rect.colliderect(gem1_rect):
        gem1collected = True
        gem1_rect.x = 3000
        gem1_rect.y = 3000
        score += 100

    #death
    if deadplayer == True:
        deadscreen_rect.x = 0
        deadscreen_rect.y = 0
        level = -1
        showseller = False

    #player buying from seller
    if player_rect.colliderect(seller_rect):
        playercollidedwithseller = True
    else:
        playercollidedwithseller = False

    if playercollidedwithseller == True:
        potionmenu_rect.x = 300
        potionmenu_rect.y = 100
        potionicon1_rect.x = 320
        potionicon1_rect.y = 120
        potionicon2_rect.x = 380
        potionicon2_rect.y = 120
    else:
        potionmenu_rect.x = 3000
        potionmenu_rect.y = 3000
        potionicon1_rect.x = 3000
        potionicon1_rect.y = 3000
        potionicon2_rect.x = 3000
        potionicon2_rect.y = 3000


    if potionicon1_rect.collidepoint(mousepos):
        if pygame.mouse.get_pressed()[0] == 1:
            if score >= 150 and timer1 == 0:
                speedpotionnumber += 1
                score -= 150
                playerclicked1 = True                  
            else:
                print('not enough coins or you have to wait until the buying cooldown expires!')

    if potionicon2_rect.collidepoint(mousepos):
        if pygame.mouse.get_pressed()[0] == 1:
            if score >= 100 and timer4 == 0:
                jumppotionnumber += 1
                score -= 100
                playerclicked3 = True
            else:
                print('not enough coins or you have to wait until the buying cooldown expires')
            
    if playerclicked1 == True:
        timer1 += 1

    if timer1 > 200:
        timer1 = 0
        playerclicked1 = False
        

    if speedpotioninventory_rect.collidepoint(mousepos):
        if pygame.mouse.get_pressed()[0] == 1 and timer2 == 0 and speedpotion == False:
            print('speedpotionacticated')
            speedpotionnumber -= 1
            speedpotion = True
            playerclicked2 = True

    if jumppotioninventory_rect.collidepoint(mousepos):
        if pygame.mouse.get_pressed()[0] == 1 and jumppotion == False and timer5 == 0:
            print('jump potion activated')
            jumppotionnumber -= 1
            jumppotion = True
            playerclicked4 = True
        
    if playerclicked2 == True:
        timer2 += 1

    if timer2 > 300:
        timer2 = 0
        playerclicked2 = False 

    if speedpotion == True:
        player_speed = 20
    else:
        player_speed = 7

    if speedpotion == True:    
        timer3 += 1

    if timer3 == 320:
        timer3 = 0
        speedpotion = False

    if jumppotion == True:
        vel2 = 38
    else:
        vel2 = 19

    #player health limit
    if player_health < 0:
        player_health = 0


    #timer for buying jump potion
    if playerclicked3 == True:
        timer4 += 1

    if timer4 > 200:
        timer4 = 0
        playerclicked3 = False

    #timer for activating jump potion
    if playerclicked4 == True:
        timer5 += 1

    if timer5 > 300:
        timer5 = 0
        playerclicked4 = False

    if jumppotion == True:
        timer6 += 1

    if timer6 == 320:
        timer6 = 0
        jumppotion = False


    #door logic
    if level == 1:
        door1_rect.x = 1200
        door1_rect.y = 560
    else:
        door1_rect.x = 3000
        door1_rect.y = 3000

    if player_rect.colliderect(door1_rect) and doorkey > 0 and deadghost == True and gem1collected == True:
        if keys[pygame.K_q]:
            platform3_rect.x = 3000
            platform4_rect.x = 3000
            platform5_rect.x = 3000
            platform1_rect.x = 3000
            platform2_rect.x = 3000
            brick1_rect.x = 3000
            level = 2
            player_rect.x = 35

    if player_rect.colliderect(door1_rect) and doorkey == 0:
        if keys[pygame.K_q]:
            print('you need key to open the door or you have not completed level 1')
    
    if deadplayer == True:
        key1_rect.x = 3000

    #wizard logic
    if level == 2:
        wizard_rect.x = 800
        wizard_rect.y = 500

    if player_rect.colliderect(wizard_rect) and collidedwithwizard == False:
        shootingability = True
        collidedwithwizard = True
        print('Hi! You are now at level 2! I will give you this free shooting ability so you dont die! LOL. Press e to use it')

    #shooting

    if keys[pygame.K_e] and shootingability == True:
        pass


    #drawing
    screen.fill((0,0,0))      
    screen.blit(startbg,startbg_rect)
    screen.blit(door1,door1_rect)
    screen.blit(platform5,platform5_rect)
    screen.blit(platform4,platform4_rect)
    screen.blit(platform3,platform3_rect)
    screen.blit(deadscreen,deadscreen_rect)
    screen.blit(ghost1,ghost1_rect)
    screen.blit(platform2,platform2_rect)
    screen.blit(brick1,brick1_rect)
    screen.blit(platform1,platform1_rect)
    screen.blit(gem1,gem1_rect)
    screen.blit(cloud1,cloud1_rect)
    screen.blit(ground,ground_rect)
    screen.blit(sure,sure_rect)
    screen.blit(wizard,wizard_rect)
    screen.blit(key1,key1_rect)
    screen.blit(yes1,yes1_rect)
    screen.blit(saferoom,saferoom_rect)
    if level == 1 or level == -2 or level == 2:
        draw_text('Score: ' + str(score),text_font1,(0,0,0),510,100)
    
    screen.blit(seller,seller_rect)
    screen.blit(potionmenu,potionmenu_rect)
    screen.blit(potionicon1,potionicon1_rect)
    screen.blit(potionicon2,potionicon2_rect)
    screen.blit(inventory_1,inventory_1_rect)
    screen.blit(jumppotioninventory,jumppotioninventory_rect)
    screen.blit(speedpotioninventory,speedpotioninventory_rect)
    if speedpotionnumber > 0 and tabpress == 1:
        draw_text(str(speedpotionnumber) + 'x',text_font2,(0,0,0),127,120)
    if jumppotionnumber > 0 and tabpress == 1:
        draw_text(str(jumppotionnumber) + 'x',text_font2,(0,0,0),127,160)
    screen.blit(returnbutton,returnbutton_rect)
    screen.blit(yes2,yes2_rect)
    screen.blit(player,player_rect)
    screen.blit(menubg,menubg_rect)
    screen.blit(start,start_rect)
    screen.blit(quit,quit_rect)
    #fps stuff
    pygame.display.flip()
    clock.tick(60)
    fps = clock.get_fps()
    #print('FPS: ' + str(fps))
