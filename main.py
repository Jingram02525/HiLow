
import pygame
import random
from pygame.locals import *
display_height = 600
display_width = 800
# Construct deck of cards
# suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
# rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
# cards = []
# for x in suits:
#     for y in rank:
#         cards.append(y + " of " + x)
# random.shuffle(cards)
# print(cards)
class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print("{} of {}".format(self.value, self.suit))
    
    def image_path(self):
        return "Card_images/PNG/{}{}.png".format(self.value, self.suit)

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["S", "H", "C", "D"]:
            for v in range(2, 15):
                self.cards.append(Card(s, v))
        random.shuffle(self.cards)

    def show(self):
        for c in self.cards:
            c.show() 

    def draw(self):
        return self.cards.pop()   

pygame.init()
gameDisplay = pygame.display.set_mode((display_width,display_height))
color = (255,255,255)
white = (255,255,255)
# light shade of the button
color_light = (170,170,170)
red = (255,0,0)
light_red = (255,127,80)
green = (0,255,0)
light_green = (144,238,144)  
# dark shade of the button
color_dark = (100,100,100)
pygame.display.set_caption('Hi - Low')
def text_objects(text, font):
    textSurface = font.render(text, True,(0,0,0))
    return textSurface, textSurface.get_rect()
# Variable to keep the main loop running
# picture of back of card
cardBack = pygame.image.load('Card_images/PNG/blue_back.png')
x = (display_width * 0.2)
y = (display_height * 0.2)
cardBack = pygame.transform.scale(cardBack, (int(cardBack.get_width() * 0.25), int(cardBack.get_height() * 0.25)))

# picture of card
# Hi button
# low button
running = True


# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            print(event.key)
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
    gameDisplay.fill((255,255,255))
    gameDisplay.blit(cardBack, (x,y))
    gameDisplay.blit(cardBack, (x + 10,y))
    gameDisplay.blit(cardBack, (x + 20,y))
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    is_higher = None
    if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
        pygame.draw.rect(gameDisplay, green,(150,450,100,50))
        if click[0] == 1:
            is_higher = False
    else:
        pygame.draw.rect(gameDisplay, light_green,(150,450,100,50))
    if 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450:
        pygame.draw.rect(gameDisplay, red,(550,450,100,50))
        if click[0] == 1:
            is_higher = True
    else:
        pygame.draw.rect(gameDisplay, light_red,(550,450,100,50))
    largeText = pygame.font.Font('freesansbold.ttf',85)
    TextSurf, TextRect = text_objects("Hi - Low", largeText)
    TextRect.center = ((display_width/2),50)
    gameDisplay.blit(TextSurf, TextRect)
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects("Low", smallText)
    textRect.center = ( (150+(100/2)), (450+(50/2)) )
    gameDisplay.blit(textSurf, textRect)
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects("High", smallText)
    textRect.center = ( (550+(100/2)), (450+(50/2)) )
    gameDisplay.blit(textSurf, textRect)
    # print(is_higher)
    pygame.display.update()     

    deck = Deck()
    card = deck.cards[0]  

    print(card.image_path())
