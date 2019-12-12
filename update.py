# Python 3.7
# update.py
# Ian: ianisablackcat@gmail.com
# 2019.03.07

import pygame
import widgets as ws
from weapon_components import *


#遊戲畫面更新
#Game screen drawing update
def update_game_screen_event(screen, game_status, player, enemies, bosses, player_weapons, bombs, enemy_weapons,
                             bonuses, show_info, stars, explode):
    screen.fill((0, 0, 0))
    update_star(stars)
    update_bonuses(game_status, player, bonuses)
    update_enemies(screen, game_status, player, enemies, enemy_weapons, bonuses, explode)
    update_enemy_weapons(screen, game_status, player, enemy_weapons, explode)
    update_player_weapons(screen, game_status, enemies, bosses, player_weapons, bonuses, explode)
    update_bosses(screen, game_status, player, bosses, enemy_weapons, explode)
    update_bombs(screen, game_status, enemies, bosses, bombs, bonuses, explode)
    player.update(game_status, player_weapons)
    update_explode(explode)
    show_info.update()
    for star in stars: star.draw()
    for bonus in bonuses.sprites(): bonus.draw()
    for enemy in enemies.sprites(): enemy.draw()
    for weapon in enemy_weapons.sprites(): weapon.draw()
    for weapon in player_weapons.sprites(): weapon.draw()
    for boss in bosses.sprites(): boss.draw()
    for bomb in bombs.sprites(): bomb.draw()
    for exp in explode.sprites(): exp.draw()
    player.draw()
    show_info.draw()
    pygame.display.flip()


#敵機繪製更新
#Enemy flight drawing update
def update_enemies(screen, game_status, player, enemies, enemy_weapons, bonuses, explode):
    enemies.update(enemy_weapons)
    for enemy in enemies.copy():
        if (enemy.x < -24) or (enemy.x > 1024):
            enemies.remove(enemy)
        elif enemy.y > 720:
            enemies.remove(enemy)
    collisions = pygame.sprite.spritecollide(player, enemies, True)
    if collisions:
        print(collisions)
        game_status.add_score('enemy', 1)
        ws.player_crashed(screen, game_status, player, explode)
        if collisions[0].bonus == 1:
            new_bonus = Bonus(screen, (collisions[0].x, collisions[0].y))
            bonuses.add(new_bonus)


#關卡魔王繪製更新
#Level demon lord drawing update
def update_bosses(screen, game_status, player, bosses, enemy_weapons, explode):
    bosses.update(player, enemy_weapons)
    for boss in bosses:
        if not boss.is_live():
            bosses.remove(boss)
            game_status.add_score('boss', 100)
            game_status.set_boss_cut()
    collinsions = pygame.sprite.spritecollide(player, bosses, False)
    if collinsions:
        for boss in collinsions:
            boss.hitted(20)
            ws.player_crashed(screen, game_status, player, explode)


#玩家武器攻擊繪製更新
#Player weapon attack drawing update
def update_player_weapons(screen, game_status, enemies, bosses, player_weapons, bonuses, explode):
    player_weapons.update()
    for weapon in player_weapons.sprites():
        if weapon.rect.bottom <= 0:
            player_weapons.remove(weapon)
        elif weapon.rect.centerx < 0 or weapon.rect.centerx > 1000:
            player_weapons.remove(weapon)
    position = ws.player_weapon_collisions(screen, game_status, enemies, bosses, player_weapons, explode)
    if position:
        new_bonus = Bonus(screen, position)
        bonuses.add(new_bonus)


#玩家炸彈攻擊繪製更新
#Player bomb attack drawing update
def update_bombs(screen, game_status, enemies, bosses, bombs, bonuses, explode):
    bombs.update()
    position_x, position_y = ws.bomb_collisions(screen, game_status, enemies, bombs, explode)
    for bomb in bombs.sprites():
        if bomb.radius_2 > 750:
            for boss in bosses:
                ws.hit_explode(screen, explode, boss.x, boss.y)
                boss.hitted(20)
            bombs.remove(bomb)
            game_status.set_bomb_exploding()
    if position_x:
        for x, y in zip(position_x, position_y):
            new_bonus = Bonus(screen, (x, y))
            bonuses.add(new_bonus)


#敵機武器攻擊繪製更新
#Enemy flight attack drawing update
def update_enemy_weapons(screen, game_status, player, enemy_weapons, explode):
    enemy_weapons.update()
    for weapon in enemy_weapons.sprites():
        if weapon.rect.top > 720:
            enemy_weapons.remove(weapon)
    ws.enemy_weapon_collisions(screen, game_status, player, enemy_weapons, explode)


#武器寶珠繪製更新
#Player weapon bonus drawing update
def update_bonuses(game_status, player, bonuses):
    bonuses.update()
    for bonus in bonuses:
        if not bonus.active:
            bonuses.remove(bonus)
    ws.bonuses_collisions(game_status, player, bonuses)


#背景星星繪製更新
#Backgraound star drawing update
def update_star(stars):
    for star in stars:
        star.update()
        if star.y >= 720:
            stars.remove(star)


#爆炸動畫繪製更新
#Explode animation drawing update
def update_explode(explode):
    explode.update()
    for exp in explode:
        if not exp.active:
            explode.remove(exp)
