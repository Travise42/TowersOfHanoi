import pygame
import math
import random
from surfaces import *

'''CREATE WINDOW'''

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Towers of Hanoi")
FPS = 100

'''CREATE PALLET'''

# colors
class color():
    LIGHT_GREY = (225, 225, 225)
    GREY = (88, 88, 88)

'''DRAWING'''

# draw title screen
def draw_titlewind():
    WIN.fill(color.GREY)

    WIN.blit(pygame.transform.rotate(pygame.transform.scale(c7, (560, 560)), 25), (0, 160))
    WIN.blit(pygame.transform.rotate(pygame.transform.scale(c4, (430, 430)), -30), (380, 100))
    WIN.blit(pygame.transform.rotate(pygame.transform.scale(c2, (300, 300)), -15), (260, 80))
    WIN.blit(pygame.transform.rotate(pygame.transform.scale(c5, (260, 260)), 50), (460, 0))
    WIN.blit(pygame.transform.rotate(pygame.transform.scale(c3, (180, 180)), 18), (430, -10))

    WIN.blit(IMG_TtCp, (319, 700))

# close title screen
def close_title():
    time = 100

    for t in range(time):
        check_close()

        WIN.fill(color.GREY)

        WIN.blit(pygame.transform.rotate(pygame.transform.scale(c7, (560, 560)), 25 - t), (0, 160 + t*28))
        WIN.blit(pygame.transform.rotate(pygame.transform.scale(c4, (430, 430)), -30 - t), (380, 100 + t*21))
        WIN.blit(pygame.transform.rotate(pygame.transform.scale(c2, (300, 300)), -15 - t), (260, 80 + t*15))
        WIN.blit(pygame.transform.rotate(pygame.transform.scale(c5, (260, 260)), 50 - t), (460, 0 + t*13))
        WIN.blit(pygame.transform.rotate(pygame.transform.scale(c3, (180, 180)), 18 + t), (430, -10 + t*9))

        pygame.display.update()

    return('home')

# bring down and swing menu
def show_menu():
    time = 50
    menu_full, chain = IMG_HmMnF, IMG_HmMnCn
    #button_off = pygame.transform.rotate(IMG_HmMnSO, 15)

    for t in range(time):
        check_close()
        
        WIN.fill(color.GREY)
        WIN.blit(chain, (320, t*12 - 660))
        WIN.blit(chain, (680, t*12 - 760))
        WIN.blit(menu_full, (40, t*12 - 660))

        pygame.display.update()

    tilt, speed = 0, 6
    for _ in range(speed*12):
        check_close()
                
        tilt -= speed
        if tilt > 0: speed += 0.6 if speed < 0 else 0.3
        if tilt < 0: speed -= 0.6 if speed > 0 else 0.3

        draw_menu(tilt, True)

        pygame.display.update()

# pull menu up
def hide_menu():
    time = 50
    menu, menu_full, chain = IMG_HmMnB, IMG_HmMnF, IMG_HmMnCn

    for t in range(time):
        check_close()
        
        WIN.fill(color.GREY)
        WIN.blit(chain, (320, -70 - t*12))
        WIN.blit(chain, (680, -170 - t*12))
        WIN.blit(menu_full, (40, -70 - t*12))

        pygame.display.update()

# place menu on screen with tilt
def draw_menu(tilt, swinging=False, amt=0):
    chain = pygame.transform.rotate(IMG_HmMnCn, -tilt/3)
    menu_full = pygame.transform.rotate(IMG_HmMnF, -tilt/4)
    button_on = IMG_HmMnSU
    button_off = IMG_HmMnSD
    screen_off = IMG_HmMnScOF
    screen_up = IMG_HmMnScUP
    screen_down = IMG_HmMnScDN
    screen_on = IMG_HmMnScON

    WIN.fill(color.GREY)
    WIN.blit(chain, (330 - chain.get_width()/2 - tilt, -35 + 170 - chain.get_height()/2 - abs(tilt/3) - tilt))
    WIN.blit(chain, (690 - chain.get_width()/2 - tilt, -135 + 170 - chain.get_height()/2 - abs(tilt/3) + tilt/2))

    flick = random.choices(['O E H', 'O E', 'O H', 'E H', 'O', 'E', 'H', ''], weights=(1000, 8, 8, 8, 2, 2, 2, 1), k=1)[0]

    if swinging:
        WIN.blit(menu_full, (529.5-menu_full.get_width()/2 - tilt*3, 419.5 - menu_full.get_height()/2 - abs(tilt/3)))

    else:
        menu_base = IMG_HmMnB
        menu_O = IMG_HmMnO
        menu_E = IMG_HmMnE
        menu_H  = IMG_HmMnH

        WIN.blit(menu_base, (40, -70))
        if 'O' in flick: WIN.blit(menu_O, (40, -70))
        if 'E' in flick: WIN.blit(menu_E, (40, -70))
        if 'H' in flick: WIN.blit(menu_H, (40, -70))
        WIN.blit(button_on, (40, -70))

        if amt == 1:
            WIN.blit(screen_up, (40, -70))
            WIN.blit(IMG_HmMnSc1, (40, -70))
        elif amt == 7:
            WIN.blit(screen_down, (40, -70))
            WIN.blit(IMG_HmMnSc7, (40, -70))
        elif amt in range(2, 6 + 1):
            WIN.blit(screen_on, (40, -70))
            if amt == 2: WIN.blit(IMG_HmMnSc2, (40, -70))
            if amt == 3: WIN.blit(IMG_HmMnSc3, (40, -70))
            if amt == 4: WIN.blit(IMG_HmMnSc4, (40, -70))
            if amt == 5: WIN.blit(IMG_HmMnSc5, (40, -70))
            if amt == 6: WIN.blit(IMG_HmMnSc6, (40, -70))
        else:
            WIN.blit(screen_off, (40, -70))

# close home screen
def close_home(chips):
    time = 200

    hide_menu()

    for t in range(time):
        check_close()

        # draw game background
        draw_gamewind()
        draw_chips(chips)
        draw_indic(chips)

        # draw sliding wall
        pygame.draw.rect(WIN, color.GREY, pygame.Rect(0, 0, WIDTH - t*5, HEIGHT))

        pygame.display.update()

    return('game')

# open home screen
def open_home(chips):
    time = 200

    for t in range(time):
        check_close()

        # draw game background
        draw_gamewind()
        draw_chips(chips)
        draw_indic(chips)

        # draw sliding wall
        pygame.draw.rect(WIN, color.GREY, pygame.Rect(0, 0, WIDTH - (time - t)*5, HEIGHT))

        pygame.display.update()

    show_menu()

    return('home')

# draw game background
def draw_gamewind(btns=[False, False, False, False, False]):
    WIN.fill(color.LIGHT_GREY)
    WIN.blit(IMG_IgBg, (0, 0))
    # draw lit and unlit buttons
    if btns[0] > 0: WIN.blit(IMG_IgBtHmA, (17, 15))
    else: WIN.blit(IMG_IgBtHm, (17, 15))
    if btns[1] > 0: WIN.blit(IMG_IgBtRsA, (17, 80))
    else: WIN.blit(IMG_IgBtRs, (17, 80))
    if btns[2] > 0: WIN.blit(IMG_IgBtAdA, (17, 145))
    else: WIN.blit(IMG_IgBtAd, (17, 145))
    if btns[3] > 0: WIN.blit(IMG_IgBtMnA, (17, 210))
    else: WIN.blit(IMG_IgBtMn, (17, 210))
    if btns[4] > 0: WIN.blit(IMG_IgBtHiA, (17, 740))
    else: WIN.blit(IMG_IgBtHi, (17, 740))

# draw game chips
def draw_chips(chips, s=0):
    for h, c in enumerate(chips[1]): 
        if c == chips[1][-1] and s == 1:
            c = c.convert_alpha()
            c.fill((250, 250, 250, 128), special_flags=pygame.BLEND_RGBA_MULT)
        WIN.blit(c, (110, 650 - (h + 1)*70))
    for h, c in enumerate(chips[2]): 
        if c == chips[2][-1] and s == 2:
            c = c.convert_alpha()
            c.fill((250, 250, 250, 128), special_flags=pygame.BLEND_RGBA_MULT)
        WIN.blit(c, (400, 650 - (h + 1)*70))
    for h, c in enumerate(chips[3]): 
        if c == chips[3][-1] and s == 3:
            c = c.convert_alpha()
            c.fill((250, 250, 250, 128), special_flags=pygame.BLEND_RGBA_MULT)
        WIN.blit(c, (690, 650 - (h + 1)*70))

# draw game arrows
def draw_indic(chips, s=0):
    if s == 0:
        WIN.blit(IMG_IgIn, (160, 50))
        WIN.blit(IMG_IgIn, (450, 50))
        WIN.blit(IMG_IgIn, (740, 50))
        return
    c = ORDER.index(chips[s][-1])
    if chips[1] == []: WIN.blit(IMG_IgInA, (160, 50))
    else:
        if c >= ORDER.index(chips[1][-1]): WIN.blit(IMG_IgInA, (160, 50))
        else: WIN.blit(IMG_IgIn, (160, 50))
    if chips[2] == []: WIN.blit(IMG_IgInA, (450, 50))
    else:
        if c >= ORDER.index(chips[2][-1]): WIN.blit(IMG_IgInA, (450, 50))
        else: WIN.blit(IMG_IgIn, (450, 50))
    if chips[3] == []: WIN.blit(IMG_IgInA, (740, 50))
    else:
        if c >= ORDER.index(chips[3][-1]): WIN.blit(IMG_IgInA, (740, 50))
        else: WIN.blit(IMG_IgIn, (740, 50))

'''FUNCTIONS'''

# move chips
def move(chips, start, dest):
    for i in range(1, 4):
        if start == i:
            piece = chips[i][-1]
            if len(chips[dest]) == 0:
                chips[i].pop(-1)
                chips[dest].append(piece)
            elif ORDER.index(piece) > ORDER.index(chips[dest][-1]):
                chips[i].pop(-1)
                chips[dest].append(piece)
    return chips

def check_close():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

'''BUTTONS'''

# reset button - resets chips back to preset
def reset(amt=0):
    new = []
    for a in range(1, amt + 1): new.append(ORDER[7 - a])
    return {1: new[::-1], 2:[], 3:[]}

# add chip
def add(amt, a=0):
    if amt + a > 7 or amt + a < 1: return amt, reset(amt)
    return amt + a, reset(amt + a)

'''MAIN PROGRAM'''

def main():
    amount = 3
    chips = reset(amount)
    selected = 0
    cooldown = False
    screen = 'title'
    IgButtons = [0, 0, 0, 0, 0]
    tilt = 0

    clock = pygame.time.Clock()
    ACTIVE = True
    while ACTIVE:
        clock.tick(FPS)

        '''TITLE SCREEN'''

        if screen == 'title':
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ACTIVE = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        screen = close_title()
                        show_menu()

                if event.type == pygame.MOUSEBUTTONDOWN and not cooldown:
                    screen = close_title()
                    show_menu()

                if event.type == pygame.MOUSEBUTTONUP:
                    cooldown = False

            # functions
            draw_titlewind()

        '''HOME SCREEN'''

        if screen == 'home':
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ACTIVE = False

                if event.type == pygame.MOUSEBUTTONDOWN and not cooldown:
                    cooldown = True
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if mouse_x in range(305, 575) and mouse_y in range(373, 665):
                        chips = reset(amount)
                        screen = close_home(chips)
                        cooldown = False
                    elif math.sqrt((mouse_x - 715)**2 + (mouse_y - 375)**2) < 20:
                        if amount < 7: amount += 1
                    elif math.sqrt((mouse_x - 720)**2 + (mouse_y - 420)**2) < 20:
                        if amount > 1: amount -= 1

                if event.type == pygame.MOUSEBUTTONUP:
                    cooldown = False
            
            # functions
            draw_menu(tilt, False, amount)

        '''IN GAME'''

        if screen == 'game':
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ACTIVE = False

                if event.type == pygame.MOUSEBUTTONDOWN and not cooldown:
                    cooldown = True
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if mouse_x in range(15, 65) and mouse_y in range(15, 65): # home button
                        selected = 0
                        IgButtons[1] = 1
                        screen = open_home(chips)
                        cooldown = False
                    if mouse_x in range(15, 65) and mouse_y in range(80, 130): # reset button
                        selected = 0
                        IgButtons[1] = 1
                        chips = reset(amount)
                    if mouse_x in range(15, 65) and mouse_y in range(145, 195): # add button
                        selected = 0
                        IgButtons[2] = 1
                        amount, chips = add(amount, 1)
                    if mouse_x in range(15, 65) and mouse_y in range(210, 260): # minus button
                        selected = 0
                        IgButtons[3] = 1
                        amount, chips = add(amount, -1)
                    elif mouse_x > 80: # towers
                        if mouse_x >= 120 and mouse_x <= 350: 
                            if selected == 0 and len(chips[1]) > 0: selected = 1
                            else:
                                chips = move(chips, selected, 1)
                                selected = 0
                        elif mouse_x >= 410 and mouse_x <= 640: 
                            if selected == 0 and len(chips[2]) > 0: selected = 2
                            else: 
                                chips = move(chips, selected, 2)
                                selected = 0
                        elif mouse_x >= 700 and mouse_x <= 920: 
                            if selected == 0 and len(chips[3]) > 0: selected = 3
                            else: 
                                chips = move(chips, selected, 3)
                                selected = 0
                        else:
                            selected = 0
                
                if event.type == pygame.MOUSEBUTTONUP:
                    cooldown = False
            
            if screen == 'game':
                # functions
                draw_gamewind(IgButtons)
                draw_indic(chips, selected)
                draw_chips(chips, selected)
        
            for n, b in enumerate(IgButtons): # cooldown for button flash
                if b > 0: IgButtons[n] = b - 0.1
        
        pygame.display.update()

    pygame.quit()

# only run program when ran directly
if __name__ == "__main__":
    main()