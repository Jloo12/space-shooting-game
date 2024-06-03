from game_loader.imgAndMusic import *
from game_loader.render_functions import *
from game_objects.object_classes import *

# -1是循環播放
pygame.mixer.music.play(-1)

#遊戲迴圈
show_init = True
running = True
while running:
    if show_init:
        close = draw_init()#draw_init是true代表return的關閉視窗函式為True
        if close:
            break
        show_init = False
        
        player = Player()
        all_sprites.add(player)
        for i in range(8):
            new_rock()
        score = 0

    clock.tick(FPS)
    #取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    #更新遊戲
    all_sprites.update()
    #判斷石頭、子彈相撞
    hits = pygame.sprite.groupcollide(rocks, bullets, True, True)
    for hit in hits:
        random.choice(expl_sound).play()
        score += hit.radius
        expl = Explosion(hit.rect.center, "lg")
        all_sprites.add(expl)
        if random.random() >0.9:
            pow =Power(hit.rect.center)
            all_sprites.add(pow)
            powers.add(pow)
        new_rock()
    
    #判斷石頭、飛船相撞
    hits = pygame.sprite.spritecollide(player,rocks,True, pygame.sprite.collide_circle)
    for hit in hits:
        new_rock()
        expl = Explosion(hit.rect.center, "sm")
        all_sprites.add(expl)
        player.health -= hit.radius
        if player.health <= 0:
            death_expl = Explosion(player.rect.center, "player")
            all_sprites.add(death_expl)
            die_sound.play()
            player.lives -= 1
            player.health = 100
            player.hide()

    #判斷寶物、飛船相撞
    hits = pygame.sprite.spritecollide(player, powers, True)
    for hit in hits:
        if hit.type == "shield":
            player.health += 20
            if player.health > 100:
                player.health = 100
            shield_sound.play()
        elif hit.type == "gun":
            player.gunup()
            gun_sound.play()

    if player.lives == 0 and not(death_expl.alive()):
        show_init = True

    #畫面顯示
    screen.fill(BLACK)
    screen.blit(backgound_img,(0,0))
    all_sprites.draw(screen)
    draw_text(screen,str(score),18 ,WIDTH/2, 10)
    draw_health(screen, player.health, 5 ,15)
    draw_lives(screen, player.lives, player_mini_img, WIDTH - 100, 15)
    pygame.display.update()

pygame.quit()