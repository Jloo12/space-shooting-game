import pygame
import os
from game_loader.colors import *
from game_loader.basic_settings import *


#載入圖片
backgound_img = pygame.image.load(os.path.join("img", "space.jpg")).convert()
player_img = pygame.image.load(os.path.join("img", "ship5.png")).convert()
player_mini_img = pygame.transform.scale(player_img,(25,19))
player_mini_img.set_colorkey(BLACK)
icon_img = pygame.image.load(os.path.join("icon.png"))
pygame.display.set_icon(icon_img)

# rock_img = pygame.image.load(os.path.join("img", "rock.png")).convert()
bullet_img = pygame.image.load(os.path.join("img", "bullet.png")).convert()
rock_imgs = []
for i in range(7):
    rock_imgs.append(pygame.image.load(os.path.join("img", f"rock{i}.png")).convert())
expl_anim = {}
expl_anim["lg"] = []
expl_anim["sm"] = []
expl_anim["player"] = []
for i in range(9):
    expl_img = (pygame.image.load(os.path.join("img", f"expl{i}.png")).convert())
    expl_img.set_colorkey(BLACK)
    expl_anim["lg"].append(pygame.transform.scale(expl_img,(75,75)))
    expl_anim["sm"].append(pygame.transform.scale(expl_img,(30,30)))
    player_expl_img = (pygame.image.load(os.path.join("img", f"player_expl{i}.png")).convert())
    player_expl_img.set_colorkey(BLACK)
    expl_anim["player"].append(player_expl_img)
power_imgs = {}
power_imgs["shield"]= pygame.image.load(os.path.join("img", "shield.png")).convert()
power_imgs["gun"] = pygame.image.load(os.path.join("img", "gun.png")).convert()


#載入音樂、音效
shoot_sound = pygame.mixer.Sound(os.path.join("sound", "shoot.wav"))
gun_sound = pygame.mixer.Sound(os.path.join("sound", "pow1.wav"))
shield_sound = pygame.mixer.Sound(os.path.join("sound", "pow0.wav"))
die_sound = pygame.mixer.Sound(os.path.join("sound", "rumble.ogg"))
expl_sound = [
    pygame.mixer.Sound(os.path.join("sound", "expl0.wav")),
    pygame.mixer.Sound(os.path.join("sound", "expl1.wav"))
]
# pygame.mixer.Sound.set_volume(0.5)
pygame.mixer.music.load(os.path.join("sound", "background.ogg"))
pygame.mixer.music.set_volume(0.4)

#載入文字
font_name = os.path.join("font.ttf")
# font_name = pygame.font.match_font('arial')

