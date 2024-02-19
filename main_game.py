import pygame
from sys import exit

width = 1000
height = 600

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('STEM Game')
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

stage = 0
stage_list = ["background.jpg", "lab_background.png", "lab_outside.png", "plains.png", "","","","betsyfields.png","plainstomarshes.png","","","","","swamp.png","","","","","townhall.png"]
left = [8]
right = [7]
up = [2, 8, 13, 18]
down = [2, 3, 8, 13]
bg_surface = pygame.transform.scale(pygame.image.load("background.jpg").convert_alpha(), (width, height))
lab_bg_surface = pygame.transform.scale(pygame.image.load("lab_background.png").convert_alpha(), (width, height))
lab_outside_surface = pygame.transform.scale(pygame.image.load("lab_outside.png").convert_alpha(), (width, height))

game_state = "Start Menu"

start_button_surface = pygame.transform.scale(pygame.image.load("start_button.png").convert_alpha(), (400, 100))
start_button_y = 420
start_button_hitbox = start_button_surface.get_rect(topleft = (290, start_button_y))

start_button_boy_surface = pygame.transform.scale(pygame.image.load("start_button.png").convert_alpha(), (320, 80))
start_button_boy_hitbox = start_button_surface.get_rect(topleft = (150, 450))

start_button_girl_surface = pygame.transform.scale(pygame.image.load("start_button.png").convert_alpha(), (320, 80))
start_button_girl_hitbox = start_button_surface.get_rect(topleft = (500, 450))

player_movement_enabled = False
player_visible = False
player_x = 900
player_y = 430
player_speed = 5
player_gender = 'Male'
player_surface = None
player_hitbox = None

mentor_x = -100
mentor_y = 200
mentor_speed = 5
mentor_surface = pygame.transform.scale(pygame.image.load("mentor.png").convert_alpha(), (125, 125))
mentor_hitbox = mentor_surface.get_rect(topleft = (mentor_x, mentor_y))

addition_goblin1_x = 150
addition_goblin1_y = 150
addition_goblin1_surface = pygame.transform.scale(pygame.image.load("addition_goblin.png").convert_alpha(), (125, 125))
addition_goblin1_hitbox = addition_goblin1_surface.get_rect(topleft = (addition_goblin1_x, addition_goblin1_y))

addition_goblin2_x = 435
addition_goblin2_y = 150
addition_goblin2_surface = pygame.transform.scale(pygame.image.load("addition_goblin.png").convert_alpha(), (125, 125))
addition_goblin2_hitbox = addition_goblin2_surface.get_rect(topleft = (addition_goblin2_x, addition_goblin2_y))

addition_goblin3_x = 750
addition_goblin3_y = 150
addition_goblin3_surface = pygame.transform.scale(pygame.image.load("addition_goblin.png").convert_alpha(), (125, 125))
addition_goblin3_hitbox = addition_goblin3_surface.get_rect(topleft = (addition_goblin3_x, addition_goblin3_y))

addition1 = pygame.transform.scale(pygame.image.load("addition1.png").convert_alpha(), (125, 125))

addanswer1 = pygame.transform.scale(pygame.image.load("addanswer1.png").convert_alpha(), (125, 125))
addanswer2 = pygame.transform.scale(pygame.image.load("addanswer2.png").convert_alpha(), (125, 125))
addanswer3 = pygame.transform.scale(pygame.image.load("addanswer3.png").convert_alpha(), (125, 125))
addanswer1_hitbox = addanswer1.get_rect(topleft = (600, 100))
addanswer2_hitbox = addanswer2.get_rect(topleft = (600, 250))
addanswer3_hitbox = addanswer3.get_rect(topleft = (600, 400))

textbox_x = 200
textbox_y = 50
textbox_width = 600
textbox_height = 100
textbox_surface = pygame.Surface((textbox_width, textbox_height))
textbox_hitbox = textbox_surface.get_rect(topleft = (textbox_x, textbox_y))
textbox_hitnew = textbox_surface.get_rect(topleft = (textbox_x, textbox_y+400))
textbox_text = "Objective: Use the arrow keys"

timer = 0
debounce = True
next = 0
addanswer = 0

def textBox(text):
    textbox_text_object = font.render(text, True, (0, 0, 0))
    text_rect = textbox_text_object.get_rect(center=(textbox_surface.get_width() // 2, textbox_surface.get_height() // 2))
    textbox_surface.fill('White')
    textbox_surface.blit(textbox_text_object, text_rect)
    screen.blit(textbox_surface, textbox_hitbox)

def textBoxDown(text):
    textbox_text_object = font.render(text, True, (0, 0, 0))
    text_rect = textbox_text_object.get_rect(center=(textbox_surface.get_width() // 2, textbox_surface.get_height() // 2))
    textbox_surface.fill('White')
    textbox_surface.blit(textbox_text_object, text_rect)
    textbox_hitnew = textbox_surface.get_rect(topleft = (textbox_x, textbox_y+400))
    screen.blit(textbox_surface, textbox_hitnew)

def setGender():
    global player_surface, player_hitbox
    if(player_gender=='Male'):
        player_surface = pygame.transform.scale(pygame.image.load("player_boy.png").convert_alpha(), (125, 125))
        player_hitbox = player_surface.get_rect(topleft = (player_x, player_y))
    else:
        player_surface = pygame.transform.scale(pygame.image.load("player_girl.png").convert_alpha(), (125, 125))
        player_hitbox = player_surface.get_rect(topleft = (player_x, player_y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if(game_state == "Start Menu"):
                if event.button == 1:  
                    if start_button_hitbox.collidepoint(event.pos):
                        game_state = "Player Select"
            elif(game_state == "Player Select"):
                if event.button == 1:
                    if start_button_boy_hitbox.collidepoint(event.pos):
                        game_state = "Lab Start"
                        player_visible = True
                        player_gender = "Male"
                        stage += 1
                    elif start_button_girl_hitbox.collidepoint(event.pos):
                        game_state = "Lab Start"
                        player_visible = True
                        player_gender = "Female"
                        stage += 1
            elif(game_state == "Go to addition"):
                if event.button == 1:
                    if addanswer1_hitbox.collidepoint(event.pos):
                        addanswer += 1
            else:
                if event.button == 1:
                    if textbox_hitbox.collidepoint(event.pos) or textbox_hitnew.collidepoint(event.pos):
                        if debounce==False:
                            next = next + 1
                            debounce = True

    if(player_movement_enabled == True):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_hitbox.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_hitbox.x += player_speed
        if keys[pygame.K_UP]:
            player_hitbox.y -= player_speed
        if keys[pygame.K_DOWN]:
            player_hitbox.y += player_speed
        player_x = player_hitbox.x
        player_y = player_hitbox.y
    
    screen.blit(pygame.transform.scale(pygame.image.load(stage_list[stage]).convert_alpha(), (width, height)), (0,0))

    if(game_state == "Start Menu"):
        #screen.blit(bg_surface,(0,0))
        screen.blit(start_button_surface, start_button_hitbox)
        screen.blit(pygame.transform.scale(pygame.image.load("logo.png").convert_alpha(), (400, 200)), (300,100))
    elif(game_state == "Player Select"):
        screen.blit(bg_surface,(0,0))
        screen.blit(pygame.transform.scale(pygame.image.load("player_boy.png").convert_alpha(), (400, 400)), (125,75))
        screen.blit(pygame.transform.scale(pygame.image.load("player_girl.png").convert_alpha(), (400, 400)), (475,75))
        screen.blit(start_button_boy_surface, start_button_boy_hitbox)
        screen.blit(start_button_girl_surface, start_button_girl_hitbox)
    elif(game_state == "Lab Start"):
        screen.blit(lab_bg_surface,(0,0))
        setGender()
        screen.blit(mentor_surface, mentor_hitbox)
        if(mentor_hitbox.x < 200):
            mentor_hitbox.x += mentor_speed
        if(textbox_text == "Objective: Use the arrow keys"):
            player_movement_enabled =  True
            textBox(textbox_text)
            timer = timer + 1
            if(timer == 100):
                textbox_text = "Objective: Go to the scientist"
                timer = 0
        elif(textbox_text == "Objective: Go to the scientist"):
            textBox(textbox_text)
            if(mentor_hitbox.colliderect(player_hitbox)):
                textbox_text = "Hey! You must be the new student! (Click)"
        elif(textbox_text == "Hey! You must be the new student! (Click)"):
            player_movement_enabled = False
            textBox(textbox_text)
            debounce = False
            if(next == 1):
                textbox_text = "Your professor has told me great things about you."
        elif(textbox_text == "Your professor has told me great things about you."):
            textBox(textbox_text)
            debounce = False
            if(next == 2):
                textbox_text = "In the Kingdom of Pi, there has been havoc!"
        elif(textbox_text == "In the Kingdom of Pi, there has been havoc!"):
            textBox(textbox_text)
            debounce = False
            if(next == 3):
                textbox_text = "Are you ready to save it? Or not?"
        elif(textbox_text == "Are you ready to save it? Or not?"):
            textBox(textbox_text)
            debounce = False
            if(next == 4):
                textbox_text = "Great, scientist! To the right then!"
        elif(textbox_text == "Great, scientist! To the right then!"):
            textBox(textbox_text)
            debounce = False
            if(next == 5):
                textbox_text = "Exit the lab and go south and see your first task."
        elif(textbox_text == "Exit the lab and go south and see your first task."):
            textBox(textbox_text)
            debounce = False
            if(next == 6):
                textbox_text = "Good luck, this kingdom depends on you!"
        elif(textbox_text == "Good luck, this kingdom depends on you!"):
            player_movement_enabled = True
            textBox(textbox_text)
            if(player_x>width-30):
                textbox_text = "Wow, they'll need it. Such a brave hero!"
                timer = 0
                player_movement_enabled = False
        elif(textbox_text == "Wow, they'll need it. Such a brave hero!"):
            if(player_x>width+50):
                player_hitbox.x += player_speed
            textBox(textbox_text)
            timer += 1
            if(timer == 100):
                textbox_text = "Objective: Follow the path outside and find Betsy"
                game_state = "Talk to cow"
                stage += 1
                player_hitbox.x, player_hitbox.y = 750, 270
    elif(game_state=="Talk to cow"):
        player_visible = True
        player_movement_enabled = True
        if(textbox_text=="Objective: Follow the path outside and find Betsy"):
            if(stage==7):
                textbox_text = "Objective: Go talk to the white cow, Betsy!"
            else:
                textBox(textbox_text)
        elif(textbox_text=="Objective: Go talk to the white cow, Betsy!"):
            textBoxDown(textbox_text)
            if(player_hitbox.collidepoint((300,50))):
                textbox_text = "Mooo! My name is Betsy (Click)"
        elif(textbox_text=="Mooo! My name is Betsy (Click)"):
            textBoxDown(textbox_text)        
            debounce = False    
            if(next == 8):
                textbox_text = "Howdy moo on this fine day!"
        elif(textbox_text=="Howdy moo on this fine day!"):
            textBoxDown(textbox_text)        
            debounce = False    
            if(next == 9):
                textbox_text = "Oh...the scientist sent you?"
        elif(textbox_text=="Oh...the scientist sent you?"):
            textBoxDown(textbox_text)        
            debounce = False    
            if(next == 10):
                textbox_text = "To restore the Kingdom of Pi, you must learn..."
        elif(textbox_text=="To restore the Kingdom of Pi, you must learn..."):
            textBoxDown(textbox_text)        
            debounce = False    
            if(next == 11):
                textbox_text = "Moothematics! Addition, substraction,"
        elif(textbox_text=="Moothematics! Addition, substraction,"):
            textBoxDown(textbox_text)        
            debounce = False    
            if(next == 12):
                textbox_text = "...division, multiplication, *moo* *mooo*..."
        elif(textbox_text=="...division, multiplication, *moo* *mooo*..."):
            textBoxDown(textbox_text)        
            debounce = False    
            if(next == 13):
                textbox_text = "(1 hour later)"
        elif(textbox_text=="(1 hour later)"):
            textBoxDown(textbox_text)        
            debounce = False    
            if(next == 14):
                textbox_text = "Anyways, you must defeat two warlords of math!"
        elif(textbox_text=="Anyways, you must defeat two warlords of math!"):
            textBoxDown(textbox_text)        
            debounce = False    
            if(next == 15):
                textbox_text = "First, you must go to the well of wisdom."
        elif(textbox_text=="First, you must go to the well of wisdom."):
            textBoxDown(textbox_text)        
            debounce = False    
            if(next == 16):
                textbox_text = "It will tell you what to study and where!"
        elif(textbox_text=="It will tell you what to study and where!"):
            textBoxDown(textbox_text)        
            debounce = False    
            if(next == 17):
                textbox_text = "Cross the bridge and go south."
        elif(textbox_text=="Cross the bridge and go south."):
            textBoxDown(textbox_text)        
            debounce = False    
            if(next == 18):
                textbox_text = "You see, the well was a town center before."
        elif(textbox_text=="You see, the well was a town center before."):
            textBoxDown(textbox_text)        
            debounce = False    
            if(next == 19):
                textbox_text = "But, the villains scared everyone. Oh well."
        elif(textbox_text=="But, the villains scared everyone. Oh well."):
            textBoxDown(textbox_text)        
            debounce = False    
            if(next == 20):
                textbox_text = "Anyways, good luck! Mooooo!! Mooooo!!"
                timer = 0
        elif(textbox_text=="Anyways, good luck! Mooooo!! Mooooo!!"):
            textBoxDown(textbox_text)        
            debounce = True
            if(timer == 100):
                textbox_text = "Objective: Go to the swamp well."
                game_state = "Walk to well"
            timer += 1
    elif(game_state == "Walk to well"):
        if(textbox_text == "Objective: Go to the swamp well."):
            textBoxDown(textbox_text)
            well_hitbox = pygame.Rect(250,150,400,400)
            if(well_hitbox.colliderect(player_hitbox) and stage==18):
                textbox_text = "Hello. I am the soul of the well."
        elif(textbox_text == "Hello. I am the soul of the well."):
            textBox(textbox_text)
            debounce = False
            if(next == 21):
                textbox_text = "I can tell that you are a pure soul."
        elif(textbox_text == "I can tell that you are a pure soul."):
            textBox(textbox_text)
            debounce = False
            if(next == 22):
                textbox_text = "To defeat the villaness of fractions-"
        elif(textbox_text == "To defeat the villaness of fractions-"):
            textBox(textbox_text)
            debounce = False
            if(next == 23):
                textbox_text = "-you must train up north, and east."
        elif(textbox_text == "-you must train up north, and east."):
            textBox(textbox_text)
            debounce = False
            if(next == 24):
                textbox_text = "Up north, you will see addition goblins."
        elif(textbox_text == "Up north, you will see addition goblins."):
            textBox(textbox_text)
            debounce = False
            if(next == 25):
                textbox_text = "At east, you will see subtraction goblins."
        elif(textbox_text == "At east, you will see subtraction goblins."):
            textBox(textbox_text)
            debounce = False
            if(next == 26):
                textbox_text = "Once you are done, meet my dear, betsy."
        elif(textbox_text == "Once you are done, meet my dear, betsy."):
            textBox(textbox_text)
            debounce = False
            if(next == 27):
                textbox_text = "Betsy will be in the Taiga, west of here."
        elif(textbox_text == "Betsy will be in the Taiga, west of here."):
            textBox(textbox_text)
            debounce = False
            if(next == 28):
                textbox_text = "All the best. Pi Kingdom counts on you."
                timer = 0
        elif(textbox_text=="All the best. Pi Kingdom counts on you."):
            textBox(textbox_text)        
            debounce = True
            if(timer == 100):
                textbox_text = "Go up north and defeat the addition goblins"
                game_state = "Go to addition"
            timer += 1
    elif(game_state == "Go to addition"):
        if(textbox_text == "Go up north and defeat the addition goblins"):
            textBox(textbox_text)
            if(stage==3):
                textbox_text = "Attack the addition goblins!"
        elif(textbox_text == "Attack the addition goblins!"):
            screen.blit(addition_goblin1_surface,addition_goblin1_hitbox)
            screen.blit(addition_goblin2_surface,addition_goblin2_hitbox)   
            screen.blit(addition_goblin3_surface,addition_goblin3_hitbox)     
            if(addition_goblin1_hitbox.colliderect(player_hitbox) or addition_goblin2_hitbox.colliderect(player_hitbox) or addition_goblin3_hitbox.colliderect(player_hitbox)):
                textbox_text = "1"
        elif(textbox_text == "1"):
            screen.blit(addition1, (300,250))
            screen.blit(addanswer1, addanswer1_hitbox)
            screen.blit(addanswer2, addanswer2_hitbox)
            screen.blit(addanswer2, addanswer3_hitbox)
            if(addanswer == 1):
                textbox_text = "2"

    if(stage>=2 and player_movement_enabled):
        if(player_x<-30):
            if(stage in left):
                stage -= 1
                player_hitbox.x = width
            else:
                player_hitbox.x = 0
                player_x = 0
        if(player_x>width+30):
            print(player_x)
            if(stage in right):
                stage += 1
                player_hitbox.x = 0
            else:
                player_hitbox.x = width
                player_x = width
        if(player_y<-30):
            if(stage in up):
                stage -= 5
                player_hitbox.y = height
            else:
                player_hitbox.y = 0
                player_y = 0
        if(player_y>height+30):
            if(stage in down):
                stage += 5
                player_hitbox.y = 0
            else:
                player_hitbox.y = height
                player_y = height

    if(player_visible == True):
        screen.blit(player_surface, player_hitbox)

    pygame.display.update()
    clock.tick(60)
