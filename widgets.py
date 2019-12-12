# Python 3.7
# widgets.py
# Ian: ianisablackcat@gmail.com
# 2019.03.07

import sys, pygame, time, threading
from weapon_components import *
from character_components import Star


#開始頁面鍵盤事件觸發
#Start page keyboard events
def op_key_events(game_status):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_status.jump_to_next_stage()
            time.sleep(0.5)


#遊戲關卡頁面鍵盤事件觸發
#Game page keyboard events
def game_key_events(screen, game_status, player, player_weapons, bombs):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_status.set_gameover()
            time.sleep(0.5)
            sys.exit()
        elif event.type == pygame.KEYDOWN: game_keydown_event(event, screen, game_status, player, player_weapons, bombs)
        elif event.type == pygame.KEYUP: game_keyup_event(event, player)


#遊戲關卡頁面鍵盤按下事件觸發
#Press keyboard events in game page
def game_keydown_event(event, screen, game_status, player, player_weapons, bombs):
    if event.key == pygame.K_SPACE:
        player.attack = True
    elif event.key == pygame.K_RIGHT:
        player.forward_direction('right')
    elif event.key == pygame.K_LEFT:
        player.forward_direction('left')
    elif event.key == pygame.K_UP:
        player.forward_direction('up')
    elif event.key == pygame.K_DOWN:
        player.forward_direction('down')
    elif event.key == pygame.K_KP6:
        player.forward_direction('right')
    elif event.key == pygame.K_KP4:
        player.forward_direction('left')
    elif event.key == pygame.K_KP8:
        player.forward_direction('up')
    elif event.key == pygame.K_KP2:
        player.forward_direction('down')
    elif event.key == pygame.K_KP9:
        player.forward_direction('top_right')
    elif event.key == pygame.K_KP3:
        player.forward_direction('bottom_right')
    elif event.key == pygame.K_KP7:
        player.forward_direction('top_left')
    elif event.key == pygame.K_KP1:
        player.forward_direction('bottom_left')
    elif event.key == pygame.K_m:
        launch_bomb(screen, game_status, bombs)


#遊戲關卡頁面鍵盤放開事件觸發
#Release keyboard events in game page
def game_keyup_event(event, player):
    if event.key == pygame.K_SPACE:
        player.attack = False
    elif event.key == pygame.K_RIGHT:
        player.stop_direction('right')
    elif event.key == pygame.K_LEFT:
        player.stop_direction('left')
    elif event.key == pygame.K_UP:
        player.stop_direction('up')
    elif event.key == pygame.K_DOWN:
        player.stop_direction('down')
    if event.key == pygame.K_KP6:
        player.stop_direction('right')
    elif event.key == pygame.K_KP4:
        player.stop_direction('left')
    elif event.key == pygame.K_KP8:
        player.stop_direction('up')
    elif event.key == pygame.K_KP2:
        player.stop_direction('down')
    elif event.key == pygame.K_KP9:
        player.stop_direction('top_right')
    elif event.key == pygame.K_KP3:
        player.stop_direction('bottom_right')
    elif event.key == pygame.K_KP7:
        player.stop_direction('top_left')
    elif event.key == pygame.K_KP1:
        player.stop_direction('bottom_left')


#結算頁面鍵盤事件觸發
#Settle page keyboard events
def stl_key_events(game_status):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_status.jump_to_next_stage()


#玩家攻擊鍵盤觸發
#Player attack events
def player_attack(screen, game_status, x, y, player_weapons):
    if game_status.current_weapon == 1:
        new_bullet = PlayerWeaponOne(screen, x, y, 8)
        player_weapons.add(new_bullet)
    elif game_status.current_weapon == 2:
        temp = [-10, 10]
        for num in range(0, 2):
            new_bullet = PlayerWeaponOne(screen, x+temp[num], y, 8)
            player_weapons.add(new_bullet)
    elif game_status.current_weapon == 3:
        temp = [-10, 10, -30, 30]
        for num in range(0, 4):
            new_bullet = PlayerWeaponOne(screen, x+temp[num], y, 8)
            player_weapons.add(new_bullet)
    elif game_status.current_weapon == 4:
        temp = [-55, 55, -10, 10, -30, 30]
        for num in range(0, 6):
            new_bullet = PlayerWeaponOne(screen, x+temp[num], y, 8)
            player_weapons.add(new_bullet)


#玩家與敵機撞擊事件
#Player and enemy flight collision events
def player_crashed(screen, game_status, player, explode):
    hit_explode(screen, explode, player.x, player.y)
    status = game_status.get_character_status()
    if status['remain_life'] > 0:
        game_status.set_player_cut()
        time.sleep(0.5)
        player.reset_position(game_status)
    else:
        game_status.set_gameover()


#玩家子彈擊中敵機事件
#Player bullet hit enemy flight events
def player_weapon_collisions(screen, game_status, enemies, bosses, player_weapons, explode):
    position = []
    collinsions1 = pygame.sprite.groupcollide(player_weapons, enemies, True, True)
    if collinsions1:
        for col in collinsions1.values():
            hit_explode(screen, explode, col[0].x, col[0].y)
            if col[0].bonus == 1:
                position.append(col[0].x)
                position.append(col[0].y)
        game_status.add_score('enemy', len(collinsions1))
    collinsions2 = pygame.sprite.groupcollide(player_weapons, bosses, True, False)
    if collinsions2:
        for boss in collinsions2.values():
            hit_explode(screen, explode, boss[0].x, boss[0].y)
            boss[0].hitted(1)
    return position

#玩家炸彈集中敵機事件
#Player bomb hit enemy flight events
def bomb_collisions(screen, game_status, enemies, bombs, explode):
    position_x = []
    position_y = []
    collinsions = pygame.sprite.groupcollide(bombs, enemies, False, True)
    if collinsions:
        for temp_enemies in collinsions.values():
            game_status.add_score('enemy', len(temp_enemies))
            for enemy in temp_enemies:
                hit_explode(screen, explode, enemy.x, enemy.y)
                if enemy.bonus == 1:
                    position_x.append(enemy.x)
                    position_y.append(enemy.y)
    return position_x, position_y


#敵機攻擊擊中事件
#Enemy attack hit events
def enemy_weapon_collisions(screen, game_status, player, enemy_weapons, explode):
    if pygame.sprite.spritecollide(player, enemy_weapons, True):
        player_crashed(screen, game_status, player, explode)


#吞食武器寶珠事件
#Player weapon bonuses events
def bonuses_collisions(game_status, player, bonuses):
    if pygame.sprite.spritecollide(player, bonuses, True):
        game_status.set_bonus(1)


#玩家發射炸彈
#Player launches bomb
def launch_bomb(screen, game_status, bombs):
    status = game_status.get_character_status()
    if status['remain_bomb'] > 0 and not game_status.get_bomb_exploding():
        game_status.set_bomb_exploding()
        game_status.set_bomb_cut()
        new_bomb = Bomb(screen)
        bombs.add(new_bomb)


#背景星星生成
#Background stars generate
def make_star(screen, stars, factor):
    if len(stars) < 7:
        new_star = Star(screen, factor)
        stars.append(new_star)


#擊中動畫事件觸發
#Hit explosion animation events
def hit_explode(screen, explode, x, y):
    new_exp = HitExplode(screen, x, y)
    explode.add(new_exp)
