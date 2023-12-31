import pygame
import os

'''IMPORT SURFACES'''

base_path = os.path.dirname(__file__)

def loadImage(path):
    return pygame.image.load(base_path + '\\' + path)

# background
IMG_TtCp = loadImage('Assets\\images\\bg\\title_caption.png')
IMG_IgBg = loadImage('Assets\\images\\bg\\activebackground.png')

# menu
IMG_HmMnD = loadImage('Assets\\images\\menu\\dim.png')
IMG_HmMnF = loadImage('Assets\\images\\menu\\full.png')
IMG_HmMnB = loadImage('Assets\\images\\menu\\base.png')
IMG_HmMnO = loadImage('Assets\\images\\menu\\O.png')
IMG_HmMnE = loadImage('Assets\\images\\menu\\E.png')
IMG_HmMnH = loadImage('Assets\\images\\menu\\H.png')
IMG_HmMnCn = loadImage('Assets\\images\\menu\\chain.png')

IMG_HmMnSU = loadImage('Assets\\images\\menu\\buttonUP.png')
IMG_HmMnSD = loadImage('Assets\\images\\menu\\buttonDOWN.png')
IMG_HmMnSO = loadImage('Assets\\images\\menu\\buttonDISABLED.png')

IMG_HmMnScOF = loadImage('Assets\\images\\menu\\screen\\off.png')
IMG_HmMnScON = loadImage('Assets\\images\\menu\\screen\\on.png')
IMG_HmMnScUP = loadImage('Assets\\images\\menu\\screen\\up.png')
IMG_HmMnScDN = loadImage('Assets\\images\\menu\\screen\\down.png')
IMG_HmMnSc1 = loadImage('Assets\\images\\menu\\screen\\1.png')
IMG_HmMnSc2 = loadImage('Assets\\images\\menu\\screen\\2.png')
IMG_HmMnSc3 = loadImage('Assets\\images\\menu\\screen\\3.png')
IMG_HmMnSc4 = loadImage('Assets\\images\\menu\\screen\\4.png')
IMG_HmMnSc5 = loadImage('Assets\\images\\menu\\screen\\5.png')
IMG_HmMnSc6 = loadImage('Assets\\images\\menu\\screen\\6.png')
IMG_HmMnSc7 = loadImage('Assets\\images\\menu\\screen\\7.png')


# assets
IMG_IgIn = loadImage('Assets\\images\\indacator.png')
IMG_IgInA = loadImage('Assets\\images\\indacator_ACTIVE.png')

# buttons
IMG_IgBtHm = loadImage('Assets\\images\\home.png')
IMG_IgBtRs = loadImage('Assets\\images\\reset.png')
IMG_IgBtAd = loadImage('Assets\\images\\add.png')
IMG_IgBtMn = loadImage('Assets\\images\\minus.png')
IMG_IgBtHi = loadImage('Assets\\images\\hint.png')
IMG_IgBtHmA = loadImage('Assets\\images\\home_ACTIVE.png')
IMG_IgBtRsA = loadImage('Assets\\images\\reset_ACTIVE.png')
IMG_IgBtAdA = loadImage('Assets\\images\\add_ACTIVE.png')
IMG_IgBtMnA = loadImage('Assets\\images\\minus_ACTIVE.png')
IMG_IgBtHiA = loadImage('Assets\\images\\hint_ACTIVE.png')

# chips
c7 = loadImage('Assets\\images\\chips\\red.png')
c6 = loadImage('Assets\\images\\chips\\orange.png')
c5 = loadImage('Assets\\images\\chips\\yellow.png')
c4 = loadImage('Assets\\images\\chips\\green.png')
c3 = loadImage('Assets\\images\\chips\\light_blue.png')
c2 = loadImage('Assets\\images\\chips\\blue.png')
c1 = loadImage('Assets\\images\\chips\\purple.png')
ORDER = [c1, c2, c3, c4, c5, c6, c7]

'''RESIZE SURFACES'''

# assets
IMG_IgIn = pygame.transform.scale(IMG_IgIn, (150, 150))
IMG_IgInA = pygame.transform.scale(IMG_IgInA, (150, 150))

# buttons
IMG_IgBtHm = pygame.transform.scale(IMG_IgBtHm, (50, 50))
IMG_IgBtRs = pygame.transform.scale(IMG_IgBtRs, (50, 50))
IMG_IgBtAd = pygame.transform.scale(IMG_IgBtAd, (50, 50))
IMG_IgBtMn = pygame.transform.scale(IMG_IgBtMn, (50, 50))
IMG_IgBtHi = pygame.transform.scale(IMG_IgBtHi, (50, 50))

IMG_IgBtHmA = pygame.transform.scale(IMG_IgBtHmA, (50, 50))
IMG_IgBtRsA = pygame.transform.scale(IMG_IgBtRsA, (50, 50))
IMG_IgBtAdA = pygame.transform.scale(IMG_IgBtAdA, (50, 50))
IMG_IgBtMnA = pygame.transform.scale(IMG_IgBtMnA, (50, 50))
IMG_IgBtHiA = pygame.transform.scale(IMG_IgBtHiA, (50, 50))

# menu
IMG_HmMnF = pygame.transform.rotate(pygame.transform.scale(IMG_HmMnF, (800, 800)), 15)
IMG_HmMnD = pygame.transform.rotate(pygame.transform.scale(IMG_HmMnD, (800, 800)), 15)
IMG_HmMnB = pygame.transform.rotate(pygame.transform.scale(IMG_HmMnB, (800, 800)), 15)
IMG_HmMnO = pygame.transform.rotate(pygame.transform.scale(IMG_HmMnO, (800, 800)), 15)
IMG_HmMnE = pygame.transform.rotate(pygame.transform.scale(IMG_HmMnE, (800, 800)), 15)
IMG_HmMnH = pygame.transform.rotate(pygame.transform.scale(IMG_HmMnH, (800, 800)), 15)
IMG_HmMnSU = pygame.transform.rotate(pygame.transform.scale(IMG_HmMnSU, (800, 800)), 15)
IMG_HmMnSD = pygame.transform.rotate(pygame.transform.scale(IMG_HmMnSD, (800, 800)), 15)
IMG_HmMnSO = pygame.transform.rotate(pygame.transform.scale(IMG_HmMnSO, (800, 800)), 15)

IMG_HmMnScOF = pygame.transform.rotate(pygame.transform.scale(IMG_HmMnScOF, (800, 800)), 15)
IMG_HmMnScON = pygame.transform.rotate(pygame.transform.scale(IMG_HmMnScON, (800, 800)), 15)
IMG_HmMnScUP = pygame.transform.rotate(pygame.transform.scale(IMG_HmMnScUP, (800, 800)), 15)
IMG_HmMnScDN = pygame.transform.rotate(pygame.transform.scale(IMG_HmMnScDN, (800, 800)), 15)
IMG_HmMnSc1 = pygame.transform.rotate(pygame.transform.scale(IMG_HmMnSc1, (800, 800)), 15)
IMG_HmMnSc2 = pygame.transform.rotate(pygame.transform.scale(IMG_HmMnSc2, (800, 800)), 15)
IMG_HmMnSc3 = pygame.transform.rotate(pygame.transform.scale(IMG_HmMnSc3, (800, 800)), 15)
IMG_HmMnSc4 = pygame.transform.rotate(pygame.transform.scale(IMG_HmMnSc4, (800, 800)), 15)
IMG_HmMnSc5 = pygame.transform.rotate(pygame.transform.scale(IMG_HmMnSc5, (800, 800)), 15)
IMG_HmMnSc6 = pygame.transform.rotate(pygame.transform.scale(IMG_HmMnSc6, (800, 800)), 15)
IMG_HmMnSc7 = pygame.transform.rotate(pygame.transform.scale(IMG_HmMnSc7, (800, 800)), 15)