import pygame
import math
import random

class Home():
    def __init__(self, surf, pallet, images, title, size):
        self.WIN = surf
        self.color = pallet
        self.images = images
        self.title = title
        
        self.amount = 3
        self.chips = self.reset(self.amount)
        
        self.WIDTH, self.HEIGHT = size
        
    # reset button - resets chips back to preset
    def reset(self, amt=0):
        new = []
        for a in range(1, amt + 1): new.append(self.images.ORDER[7 - a])
        return {1: new[::-1], 2:[], 3:[]}
    
    # draw game chips
    def draw_chips(self, chips, s=0):
        for h, c in enumerate(chips[1]): 
            if c == chips[1][-1] and s == 1:
                c = c.convert_alpha()
                c.fill((250, 250, 250, 128), special_flags=pygame.BLEND_RGBA_MULT)
            self.WIN.blit(c, (110, 650 - (h + 1)*70))
        for h, c in enumerate(chips[2]): 
            if c == chips[2][-1] and s == 2:
                c = c.convert_alpha()
                c.fill((250, 250, 250, 128), special_flags=pygame.BLEND_RGBA_MULT)
            self.WIN.blit(c, (400, 650 - (h + 1)*70))
        for h, c in enumerate(chips[3]): 
            if c == chips[3][-1] and s == 3:
                c = c.convert_alpha()
                c.fill((250, 250, 250, 128), special_flags=pygame.BLEND_RGBA_MULT)
            self.WIN.blit(c, (690, 650 - (h + 1)*70))
            
    
    # draw game arrows
    def draw_indic(self, chips, s=0):
        if s == 0:
            self.WIN.blit(self.images.IMG_IgIn, (160, 50))
            self.WIN.blit(self.images.IMG_IgIn, (450, 50))
            self.WIN.blit(self.images.IMG_IgIn, (740, 50))
            return
        c = self.images.ORDER.index(chips[s][-1])
        if chips[1] == []: self.WIN.blit(self.images.IMG_IgInA, (160, 50))
        else:
            if c >= self.images.ORDER.index(chips[1][-1]): self.WIN.blit(self.images.IMG_IgInA, (160, 50))
            else: self.WIN.blit(self.images.IMG_IgIn, (160, 50))
        if chips[2] == []: self.WIN.blit(self.images.IMG_IgInA, (450, 50))
        else:
            if c >= self.images.ORDER.index(chips[2][-1]): self.WIN.blit(self.images.IMG_IgInA, (450, 50))
            else: self.WIN.blit(self.images.IMG_IgIn, (450, 50))
        if chips[3] == []: self.WIN.blit(self.images.IMG_IgInA, (740, 50))
        else:
            if c >= self.images.ORDER.index(chips[3][-1]): self.WIN.blit(self.images.IMG_IgInA, (740, 50))
            else: self.WIN.blit(self.images.IMG_IgIn, (740, 50))
    
    # open home screen
    def open_home(self, chips):
        time = 200

        for t in range(time):
            self.title.check_close()

            # draw game background
            self.draw_gamewind()
            self.draw_chips(chips)
            self.draw_indic(chips)

            # draw sliding wall
            pygame.draw.rect(self.WIN, self.color.GREY, pygame.Rect(0, 0, self.WIDTH - (time - t)*5, self.HEIGHT))

            pygame.display.update()

        self.title.show_menu()

        return self
    
    # close home screen
    def close_home(self, chips):
        time = 200

        self.hide_menu()

        for t in range(time):
            self.title.check_close()

            # draw game background
            self.draw_gamewind()
            self.draw_chips(chips)
            self.draw_indic(chips)

            # draw sliding wall
            pygame.draw.rect(self.WIN, self.color.GREY, pygame.Rect(0, 0, self.WIDTH - t*5, self.HEIGHT))

            pygame.display.update()
    
    # pull menu up
    def hide_menu(self):
        time = 50
        menu, menu_full, chain = self.images.IMG_HmMnB, self.images.IMG_HmMnF, self.images.IMG_HmMnCn

        for t in range(time):
            self.title.check_close()
            
            self.WIN.fill(self.color.GREY)
            self.WIN.blit(chain, (320, -70 - t*12))
            self.WIN.blit(chain, (680, -170 - t*12))
            self.WIN.blit(menu_full, (40, -70 - t*12))

            pygame.display.update()
            
    # draw game background
    def draw_gamewind(self, btns=[False, False, False, False, False]):
        self.WIN.fill(self.color.LIGHT_GREY)
        self.WIN.blit(self.images.IMG_IgBg, (0, 0))
        # draw lit and unlit buttons
        if btns[0] > 0: self.WIN.blit(self.images.IMG_IgBtHmA, (17, 15))
        else: self.WIN.blit(self.images.IMG_IgBtHm, (17, 15))
        if btns[1] > 0: self.WIN.blit(self.images.IMG_IgBtRsA, (17, 80))
        else: self.WIN.blit(self.images.IMG_IgBtRs, (17, 80))
        if btns[2] > 0: self.WIN.blit(self.images.IMG_IgBtAdA, (17, 145))
        else: self.WIN.blit(self.images.IMG_IgBtAd, (17, 145))
        if btns[3] > 0: self.WIN.blit(self.images.IMG_IgBtMnA, (17, 210))
        else: self.WIN.blit(self.images.IMG_IgBtMn, (17, 210))
        if btns[4] > 0: self.WIN.blit(self.images.IMG_IgBtHiA, (17, 740))
        else: self.WIN.blit(self.images.IMG_IgBtHi, (17, 740))
    
    def handleEvents(self, screens, cooldown):
        screen = self
        ACTIVE = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ACTIVE = False

            if event.type == pygame.MOUSEBUTTONDOWN and not cooldown:
                cooldown = True
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if mouse_x in range(305, 575) and mouse_y in range(373, 665):
                    self.chips = self.reset(self.amount)
                    self.close_home(self.chips)
                    screen = screens[2]
                    cooldown = False
                elif math.sqrt((mouse_x - 715)**2 + (mouse_y - 375)**2) < 20:
                    if self.amount < 7: self.amount += 1
                elif math.sqrt((mouse_x - 720)**2 + (mouse_y - 420)**2) < 20:
                    if self.amount > 1: self.amount -= 1

            if event.type == pygame.MOUSEBUTTONUP:
                cooldown = False
        
        if screen == self:
            # functions
            screens[0].draw_menu(0, False, self.amount)
    
        return ACTIVE, screen, cooldown