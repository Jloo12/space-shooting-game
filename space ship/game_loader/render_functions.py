from game_loader.basic_settings import *
from game_loader.imgAndMusic import *
from game_objects.object_classes import Rock

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

def new_rock():
    r = Rock()
    all_sprites.add(r)
    rocks.add(r)

#畫出血量條
def draw_health(surf, hp , x , y):
    if hp <0:
        hp = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (hp/100)*BAR_LENGTH
    outline_rect = pygame.Rect(x,y,BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x , y , fill ,BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect , 2)

#畫出生命數量
def draw_lives(surf, lives, img, x, y):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30*i
        img_rect.y = y
        surf.blit(img, img_rect)

#製作初始畫面
def draw_init():
    screen.blit(backgound_img,(0,0))
    draw_text(screen,"射擊遊戲",64, WIDTH/2, HEIGHT/4)
    draw_text(screen,"WASD鍵移動飛船 空白鍵發射子彈", 22 ,WIDTH/2, HEIGHT/2)
    draw_text(screen,"按任意鍵開始", 18, WIDTH/2, HEIGHT*3/4)
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            elif event.type == pygame.KEYUP:
                waiting = False
                return False
