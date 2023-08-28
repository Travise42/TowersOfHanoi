import pygame
import math
import random

class Title():
    def __init__(self, surf, pallet, images):
        self.WIN = surf
        self.color = pallet
        self.images = images
        
        self.tilt = 0

    # close title screen
    def close_title(self):
        time = 100

        for t in range(time):
            self.check_close()

            self.WIN.fill(self.color.GREY)

            self.WIN.blit(pygame.transform.rotate(pygame.transform.scale(self.images.c7, (560, 560)), 25 - t), (0, 160 + t*28))
            self.WIN.blit(pygame.transform.rotate(pygame.transform.scale(self.images.c4, (430, 430)), -30 - t), (380, 100 + t*21))
            self.WIN.blit(pygame.transform.rotate(pygame.transform.scale(self.images.c2, (300, 300)), -15 - t), (260, 80 + t*15))
            self.WIN.blit(pygame.transform.rotate(pygame.transform.scale(self.images.c5, (260, 260)), 50 - t), (460, 0 + t*13))
            self.WIN.blit(pygame.transform.rotate(pygame.transform.scale(self.images.c3, (180, 180)), 18 + t), (430, -10 + t*9))

            pygame.display.update()
    
    def check_close(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
    # bring down and swing menu
    def show_menu(self):
        time = 50
        menu_full, chain = self.images.IMG_HmMnF, self.images.IMG_HmMnCn
        #button_off = pygame.transform.rotate(IMG_HmMnSO, 15)

        for t in range(time):
            self.check_close()
            
            self.WIN.fill(self.color.GREY)
            self.WIN.blit(chain, (320, t*12 - 660))
            self.WIN.blit(chain, (680, t*12 - 760))
            self.WIN.blit(menu_full, (40, t*12 - 660))

            pygame.display.update()

        self.tilt, speed = 0, 6
        for _ in range(speed*12):
            self.check_close()
                    
            self.tilt -= speed
            if self.tilt > 0: speed += 0.6 if speed < 0 else 0.3
            if self.tilt < 0: speed -= 0.6 if speed > 0 else 0.3

            self.draw_menu(self.tilt, True)

            pygame.display.update()
            
    # place menu on screen with tilt
    def draw_menu(self, tilt, swinging=False, amt=0):
        chain = pygame.transform.rotate(self.images.IMG_HmMnCn, -tilt/3)
        menu_full = pygame.transform.rotate(self.images.IMG_HmMnF, -tilt/4)
        button_on = self.images.IMG_HmMnSU
        button_off = self.images.IMG_HmMnSD
        screen_off = self.images.IMG_HmMnScOF
        screen_up = self.images.IMG_HmMnScUP
        screen_down = self.images.IMG_HmMnScDN
        screen_on = self.images.IMG_HmMnScON

        self.WIN.fill(self.color.GREY)
        self.WIN.blit(chain, (330 - chain.get_width()/2 - tilt, -35 + 170 - chain.get_height()/2 - abs(tilt/3) - tilt))
        self.WIN.blit(chain, (690 - chain.get_width()/2 - tilt, -135 + 170 - chain.get_height()/2 - abs(tilt/3) + tilt/2))

        flick = random.choices(['O E H', 'O E', 'O H', 'E H', 'O', 'E', 'H', ''], weights=(1000, 8, 8, 8, 2, 2, 2, 1), k=1)[0]

        if swinging:
            self.WIN.blit(menu_full, (529.5 - menu_full.get_width()/2 - tilt*3, 419.5 - menu_full.get_height()/2 - abs(tilt/3)))

        else:
            menu_base = self.images.IMG_HmMnB
            menu_O = self.images.IMG_HmMnO
            menu_E = self.images.IMG_HmMnE
            menu_H  = self.images.IMG_HmMnH

            self.WIN.blit(menu_base, (40, -70))
            if 'O' in flick: self.WIN.blit(menu_O, (40, -70))
            if 'E' in flick: self.WIN.blit(menu_E, (40, -70))
            if 'H' in flick: self.WIN.blit(menu_H, (40, -70))
            self.WIN.blit(button_on, (40, -70))

            if amt == 1:
                self.WIN.blit(screen_up, (40, -70))
                self.WIN.blit(self.images.IMG_HmMnSc1, (40, -70))
            elif amt == 7:
                self.WIN.blit(screen_down, (40, -70))
                self.WIN.blit(self.images.IMG_HmMnSc7, (40, -70))
            elif amt in range(2, 6 + 1):
                self.WIN.blit(screen_on, (40, -70))
                if amt == 2: self.WIN.blit(self.images.IMG_HmMnSc2, (40, -70))
                if amt == 3: self.WIN.blit(self.images.IMG_HmMnSc3, (40, -70))
                if amt == 4: self.WIN.blit(self.images.IMG_HmMnSc4, (40, -70))
                if amt == 5: self.WIN.blit(self.images.IMG_HmMnSc5, (40, -70))
                if amt == 6: self.WIN.blit(self.images.IMG_HmMnSc6, (40, -70))
            else:
                self.WIN.blit(screen_off, (40, -70))
            
    # draw title screen
    def draw_titlewind(self):
        self.WIN.fill(self.color.GREY)

        self.WIN.blit(pygame.transform.rotate(pygame.transform.scale(self.images.c7, (560, 560)), 25), (0, 160))
        self.WIN.blit(pygame.transform.rotate(pygame.transform.scale(self.images.c4, (430, 430)), -30), (380, 100))
        self.WIN.blit(pygame.transform.rotate(pygame.transform.scale(self.images.c2, (300, 300)), -15), (260, 80))
        self.WIN.blit(pygame.transform.rotate(pygame.transform.scale(self.images.c5, (260, 260)), 50), (460, 0))
        self.WIN.blit(pygame.transform.rotate(pygame.transform.scale(self.images.c3, (180, 180)), 18), (430, -10))

        self.WIN.blit(self.images.IMG_TtCp, (319, 700))

    def handleEvents(self, screens, cooldown):
        screen = self
        ACTIVE = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ACTIVE = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    screen = self.close_title()
                    screen = screens[1]
                    self.show_menu()

            if event.type == pygame.MOUSEBUTTONDOWN and not cooldown:
                screen = self.close_title()
                screen = screens[1]
                self.show_menu()

            if event.type == pygame.MOUSEBUTTONUP:
                cooldown = False

        if screen == self:
            # functions
            self.draw_titlewind()
        
        return ACTIVE, screen, cooldown