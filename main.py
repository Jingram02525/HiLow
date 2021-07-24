from typing import final
import pygame
import random
import operator
from pygame.locals import *

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
   
    def image_path(self):
        return "Card_images/{}{}.png".format(self.value, self.suit)

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["S", "H", "C", "D"]:
            for v in range(2, 15):
                self.cards.append(Card(s, v))
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()  
    
    def empty(self):
        return len(self.cards) == 0

def text_objects(text, font):
    text_surface = font.render(text, True,(0,0,0))
    return text_surface, text_surface.get_rect()

def start():
    deck = Deck()
    guess_counter = 0
    card = deck.draw()
    card_comparison_result = ""
    return card, card_comparison_result, deck, guess_counter

def comparison(card, new_card, comparitor, guess_counter):
    if comparitor(card.value, new_card.value):
        card_comparison_result = "Correct!"
        guess_counter = guess_counter + 1
    else:
        card_comparison_result = "Incorrect..."
    return card_comparison_result, guess_counter, new_card


pygame.init()
pygame.display.set_caption('Hi - Low')

display_height = 600
display_width = 800
game_display = pygame.display.set_mode((display_width,display_height))

red = (255,0,0)
light_red = (255,127,80)
green = (0,255,0)
light_green = (144,238,144)  

card_back = pygame.image.load('Card_images/blue_back.png')
card_back = pygame.transform.scale(card_back, (int(card_back.get_width() * 0.25), int(card_back.get_height() * 0.25)))
card_back_x_coordinate = (display_width * 0.2)
card_back_y_coordinate = (display_height * 0.2)

card, card_comparison_result, deck, guess_counter = start()
running = True

while running:
    game_display.fill((255,255,255))
    game_display.blit(card_back, (card_back_x_coordinate, card_back_y_coordinate))
    game_display.blit(card_back, (card_back_x_coordinate + 10,card_back_y_coordinate))
    game_display.blit(card_back, (card_back_x_coordinate + 20,card_back_y_coordinate))
    
    pygame.draw.rect(game_display, green,(150,450,100,50))
    pygame.draw.rect(game_display, red,(550,450,100,50))
    card_face = pygame.image.load(card.image_path())
    card_face = pygame.transform.scale(card_face, (int(card_face.get_width() * 0.25), int(card_face.get_height() * 0.25)))
    game_display.blit(card_face, (card_back_x_coordinate + 300,card_back_y_coordinate))
    
    large_text = pygame.font.Font('freesansbold.ttf',85)
    small_text = pygame.font.Font("freesansbold.ttf",20)
    
    title_text, title_text_rect = text_objects("Hi - Low", large_text)
    title_text_rect.center = ((display_width/2),50)
    game_display.blit(title_text, title_text_rect)
    
    low_button_text, low_button_text_rect = text_objects("Low", small_text)
    low_button_text_rect.center = ( (150+(100/2)), (450+(50/2)) )
    game_display.blit(low_button_text, low_button_text_rect)
    
    high_button_text, high_button_text_rect = text_objects("High", small_text)
    high_button_text_rect.center = ( (550+(100/2)), (450+(50/2)) )
    game_display.blit(high_button_text, high_button_text_rect)
    
    individual_result_text, individual_result_text_rect = text_objects(card_comparison_result, large_text)
    individual_result_text_rect.center = ((display_width/2),560)
    game_display.blit(individual_result_text, individual_result_text_rect)
    
    if deck.empty():
        game_display.fill((255,255,255))
        
        final_result_text_1, final_result_text_1_rect = text_objects("You got " + str(guess_counter), large_text)
        final_result_text_1_rect.center = ((display_width/2),300)
        game_display.blit(final_result_text_1, final_result_text_1_rect)
        
        final_result_text_2, final_result_text_2_rect = text_objects(" out of 51 correct.", large_text)
        final_result_text_2_rect.center = ((display_width/2),380)
        game_display.blit(final_result_text_2, final_result_text_2_rect)
        
        pygame.draw.rect(game_display, light_green,(150,450,100,50))
        restart_button_text, restart_button_text_rect = text_objects("Restart", small_text)
        restart_button_text_rect.center = ( (150+(100/2)), (450+(50/2)) )
        game_display.blit(restart_button_text, restart_button_text_rect)
        
        for event in pygame.event.get():
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                if 150+100 > event.pos[0] > 150 and 450+50 > event.pos[1] > 450:
                    card, card_comparison_result, deck, guess_counter = start()
                    
    else:
        for event in pygame.event.get():
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:

                if 150+100 > event.pos[0] > 150 and 450+50 > event.pos[1] > 450:            
                    new_card = deck.draw()
                    card_comparison_result, guess_counter, card = comparison(card, new_card, operator.gt, guess_counter)
                    pygame.draw.rect(game_display, light_green,(150,450,100,50))

                if 550+100 > event.pos[0] > 550 and 450+50 > event.pos[1] > 450:            
                    new_card = deck.draw()
                    card_comparison_result, guess_counter, card = comparison(card, new_card, operator.lt, guess_counter)
                    pygame.draw.rect(game_display, light_red,(550,450,100,50))
        
    pygame.display.update()            