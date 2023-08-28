import pygame
import math
import random

class Game():
    def __init__(self, surf, pallet, images, home):
        self.WIN = surf
        self.color = pallet
        self.images = images
        self.home = home
        
        self.IgButtons = [0, 0, 0, 0, 0]
        self.selected = 0
    
    # add chip
    def add(self, amt, a=0):
        if amt + a > 7 or amt + a < 1: return amt, self.home.reset(amt)
        return amt + a, self.home.reset(amt + a)
            
    # move chips
    def move(self, chips, start, dest):
        for i in range(1, 4):
            if start == i:
                piece = chips[i][-1]
                if len(chips[dest]) == 0:
                    chips[i].pop(-1)
                    chips[dest].append(piece)
                elif self.images.ORDER.index(piece) > self.images.ORDER.index(chips[dest][-1]):
                    chips[i].pop(-1)
                    chips[dest].append(piece)
        return chips
        
    def handleEvents(self, screens, cooldown):
        screen = self
        ACTIVE = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ACTIVE = False

            if event.type == pygame.MOUSEBUTTONDOWN and not cooldown:
                cooldown = True
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if mouse_x in range(15, 65) and mouse_y in range(15, 65): # home button
                    self.selected = 0
                    self.IgButtons[1] = 1
                    screen = self.home.open_home(self.home.chips)
                    cooldown = False
                if mouse_x in range(15, 65) and mouse_y in range(80, 130): # reset button
                    self.selected = 0
                    self.IgButtons[1] = 1
                    self.home.chips = self.home.reset(self.home.amount)
                if mouse_x in range(15, 65) and mouse_y in range(145, 195): # add button
                    self.selected = 0
                    self.IgButtons[2] = 1
                    self.home.amount, self.home.chips = self.add(self.home.amount, 1)
                if mouse_x in range(15, 65) and mouse_y in range(210, 260): # minus button
                    self.selected = 0
                    self.IgButtons[3] = 1
                    self.home.amount, self.home.chips = self.add(self.home.amount, -1)
                elif mouse_x > 80: # towers
                    if mouse_x >= 120 and mouse_x <= 350: 
                        if self.selected == 0 and len(self.home.chips[1]) > 0: self.selected = 1
                        else:
                            self.home.chips = self.move(self.home.chips, self.selected, 1)
                            self.selected = 0
                    elif mouse_x >= 410 and mouse_x <= 640: 
                        if self.selected == 0 and len(self.home.chips[2]) > 0: self.selected = 2
                        else: 
                            self.home.chips = self.move(self.home.chips, self.selected, 2)
                            self.selected = 0
                    elif mouse_x >= 700 and mouse_x <= 920: 
                        if self.selected == 0 and len(self.home.chips[3]) > 0: self.selected = 3
                        else: 
                            self.home.chips = self.move(self.home.chips, self.selected, 3)
                            self.selected = 0
                    else:
                        self.selected = 0
            
            if event.type == pygame.MOUSEBUTTONUP:
                cooldown = False
        
        if screen == self:
            self.home.draw_gamewind(self.IgButtons)
            self.home.draw_indic(self.home.chips, self.selected)
            self.home.draw_chips(self.home.chips, self.selected)
    
        for n, b in enumerate(self.IgButtons): # cooldown for button flash
            if b > 0: self.IgButtons[n] = b - 0.1
            
        return ACTIVE, screen, cooldown