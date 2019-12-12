# Python 3.7
# stage_components.py
# Ian: ianisablackcat@gmail.com
# 2019.03.07

import pygame, threading, time, random
import widgets as ws
import scripts_data as sp
import program_data as pd
import update as ud
from pygame.sprite import Group
from character_components import *


#開始畫面頁面模板
#Start page template
class OpeningPage:
    def __init__(self, screen, game_status):
        self.screen = screen
        #載入參數
        #Load parameters
        self.game_status = game_status
        self.op_imgs, self.op_rects, self.op_press = pd.opening_page_parameters(self.screen)
        self.op_flash_time = 0
        self.op_flash_ctrl = True

    #頁面執行迴圈
    #Page loop execution
    def play_stage(self):
        while True:
            if not self.game_status.get_current_scenes() == 0: break
            ws.op_key_events(self.game_status)
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

    #畫面繪製
    #Page drawing
    def draw(self):
        if not self.op_flash_ctrl and (time.time() - self.op_flash_time > 0.8):
            self.op_flash_ctrl = True
            self.op_flash_time = time.time()
        elif self.op_flash_ctrl and (time.time() - self.op_flash_time > 1.2):
            self.op_flash_ctrl = False
            self.op_flash_time = time.time()

        for img, rect in zip(self.op_imgs, self.op_rects):
            self.screen.blit(img, rect)
        if self.op_flash_ctrl: self.screen.blit(self.op_press[0], self.op_press[1])


#關卡模板
#Game level template
class Stage:
    def __init__(self, screen, game_status, stage_enemy_prms, boss_amount):
        self.screen = screen
        #載入目前關卡參數及劇本
        #Load level script parameters
        self.game_status = game_status
        self.stage_enemy_prms = stage_enemy_prms
        self.boss_amount = boss_amount
        self.enemies = Group()
        self.player_weapons = Group()
        self.bombs = Group()
        self.enemy_weapons = Group()
        self.bonuses = Group()
        self.bosses = Group()
        self.explode = Group()
        self.stars = []
        self.player = Player(self.screen)
        self.stage_scripts = sp.stage_01_scripts()
        self.script_time = 0
        self.script_marker = 0
        self.stage_clear = False
        self.game_status.set_stage_boss_amount(self.boss_amount)
        self.show_info = ShowStatusInfo(screen, game_status)

    #定義關卡頁面運行程式
    #Game level page execution
    def play_stage(self):
        #以多執行續執行關卡劇本
        #Run level scripts in multiple threads
        script_control = threading.Thread(target=self.script_line_control)
        script_control.start()
        #執行關卡主程式
        #Game level page loop execution
        while True:
            #判斷遊戲狀態或關卡是否結束否則執行跳轉頁面
            #Leave this page if game status or game is over
            if not self.game_status.get_game_active() or self.stage_clear:
                self.game_status.jump_to_settle_page()
                time.sleep(0.5)
                break
            #判斷目前頁面標籤與關卡劇本是否相符
            #Check if level and script are match
            if not self.game_status.get_current_scenes() == self.stage_enemy_prms['stage']: break
            #背景生成
            #Background generation
            ws.make_star(self.screen, self.stars, self.stage_enemy_prms['stage'])
            #鍵盤事件觸發
            #Keyboard event trigger
            ws.game_key_events(self.screen, self.game_status, self.player, self.player_weapons, self.bombs)
            #事件更新
            #Event update
            ud.update_game_screen_event(self.screen, self.game_status, self.player, self.enemies, self.bosses,
                                        self.player_weapons, self.bombs, self.enemy_weapons, self.bonuses, self.show_info,
                                        self.stars, self.explode)
            #確認我方角色生命餘量
            #Confirming player character life margin
            character_status = self.game_status.get_character_status()
            if character_status['remain_life'] < 0: self.game_status.set_gameover()
            if character_status['remain_boss'] == 0:
                self.stage_clear = True
                if self.game_status.get_current_scenes() == 3: self.game_status.set_gameover()

    #定義關卡劇本執行
    #Script execution
    def script_line_control(self):
        while True:
            time.sleep(1)
            #招喚魔王
            #Summon the level demon lord
            if self.script_marker == 15:
                for num in range(0, self.boss_amount):
                    new_boss = Boss(self.screen, self.game_status, self.stage_enemy_prms)
                    self.bosses.add(new_boss)
            if self.script_marker >= len(self.stage_scripts):
                now_script = self.stage_scripts[self.script_marker % len(self.stage_scripts)]
                print(now_script)
            else:
                now_script = self.stage_scripts[self.script_marker]
                print(now_script)
            self.performance(now_script)
            self.script_marker += 1
            #確認目前關卡狀態或頁面標籤
            #Confirm current level status or page label
            if not self.game_status.get_game_active(): break
            if self.game_status.get_current_scenes() == 99: break

    #定義劇本內容對應的執行
    #How to execute the script content
    def performance(self, script):
        if script == 0:
            return
        if script['qua'] == 1:
            new_enemy = Enemy(self.screen, self.stage_enemy_prms, script)
            self.enemies.add(new_enemy)
        else:
            temp_script = script.copy()
            for num in range(temp_script['qua']):
                temp_script['loc_x'] += 80
                new_enemy = Enemy(self.screen, self.stage_enemy_prms, temp_script)
                self.enemies.add(new_enemy)


#定義結算頁面
#Settle page template
class SettlePage:
    def __init__(self, screen, game_status):
        self.screen = screen
        #載入參數資料
        #Load parameters
        self.game_status = game_status
        self.game_active = self.game_status.get_game_active()
        self.stl_imgs, self.stl_rects, self.graphics_data = pd.settle_page_parameters(self.screen, self.game_active,
                                                                                      self.game_status.get_game_score())
        self.stl_flash_time = 0
        self.stl_flash_ctrl = True

        self.boss_img = pygame.image.load('images/boss_2.png').convert_alpha()
        self.boss_rect = self.boss_img.get_rect()
        self.boss_rect.center = (self.graphics_data['boss_x'], self.graphics_data['boss_y'])

    #頁面運行主程式
    #Page execution
    def play_stage(self):
        time.sleep(1)
        pygame.event.clear()
        while True:
            if not self.game_status.get_current_scenes() == 99: break
            ws.stl_key_events(self.game_status)
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()
        time.sleep(0.5)
        pygame.event.clear()

    #定義頁面繪製
    #Page drawing
    def draw(self):
        for num in range(0, 6):
            self.screen.blit(self.stl_imgs[num], self.stl_rects[num])
        if self.game_active:
            if not self.stl_flash_ctrl and (time.time() - self.stl_flash_time > 0.8):
                self.stl_flash_ctrl = True
                self.stl_flash_time = time.time()
            elif self.stl_flash_ctrl and (time.time() - self.stl_flash_time > 1.2):
                self.stl_flash_ctrl = False
                self.stl_flash_time = time.time()
            if self.stl_flash_ctrl: self.screen.blit(self.stl_imgs[6], self.stl_rects[6])

        pygame.draw.polygon(self.screen, self.graphics_data['gray_3'],
                            [[self.graphics_data['enemy_x']-24, self.graphics_data['enemy_y']+28],
                             [self.graphics_data['enemy_x']+24, self.graphics_data['enemy_y']+28],
                             [self.graphics_data['enemy_x']+24, self.graphics_data['enemy_y']+23],
                             [self.graphics_data['enemy_x'], self.graphics_data['enemy_y']+18],
                             [self.graphics_data['enemy_x']-24, self.graphics_data['enemy_y']+23]])
        pygame.draw.polygon(self.screen, self.graphics_data['gray_3'],
                            [[self.graphics_data['enemy_x']-11, self.graphics_data['enemy_y']+8],
                             [self.graphics_data['enemy_x']+11, self.graphics_data['enemy_y']+8],
                             [self.graphics_data['enemy_x']+11, self.graphics_data['enemy_y']+6],
                             [self.graphics_data['enemy_x'], self.graphics_data['enemy_y']+3],
                             [self.graphics_data['enemy_x']-11, self.graphics_data['enemy_y']+6]])
        pygame.draw.ellipse(self.screen, self.graphics_data['gray_1'],
                            [self.graphics_data['enemy_x']-5, self.graphics_data['enemy_y'], 11, 45])
        pygame.draw.polygon(self.screen, self.graphics_data['white'],
                            [[self.graphics_data['enemy_x'], self.graphics_data['enemy_y']+35],
                             [self.graphics_data['enemy_x']-1, self.graphics_data['enemy_y']+32],
                             [self.graphics_data['enemy_x']-1, self.graphics_data['enemy_y']+27],
                             [self.graphics_data['enemy_x']+1, self.graphics_data['enemy_y']+27],
                             [self.graphics_data['enemy_x']+1, self.graphics_data['enemy_y']+32]])
        pygame.draw.rect(self.screen, self.graphics_data['gray_3'],
                         [self.graphics_data['enemy_x']-8, self.graphics_data['enemy_y']+40, 16, 2])

        self.screen.blit(self.boss_img, self.boss_rect)


#定義關卡頁面的遊戲資訊顯示
#Game info display on game page
class ShowStatusInfo:
    def __init__(self, screen, game_status):
        self.screen = screen
        self.game_status = game_status
        self.color_prms = pd.show_status_info_parameters()
        self.character_status = self.game_status.get_character_status()
        self.remain_font = pygame.font.Font("font/comic.ttf", 30)
        self.remain_life = str(self.character_status['remain_life'])
        self.remain_bomb = str(self.character_status['remain_bomb'])
        self.remain_life_img = self.remain_font.render(self.remain_life, True, self.color_prms['white'])
        self.remain_bomb_img = self.remain_font.render(self.remain_bomb, True, self.color_prms['white'])
        self.remain_life_rect = self.remain_life_img.get_rect()
        self.remain_life_rect.center = (980, 690)
        self.remain_bomb_rect = self.remain_bomb_img.get_rect()
        self.remain_bomb_rect.center = (30, 690)

    #定義訊息繪製
    #Shape drawing
    def draw(self):
        pygame.draw.circle(self.screen, self.color_prms['red_1'], (950, 700), 10)
        pygame.draw.circle(self.screen, self.color_prms['red_1'], (960, 700), 10)
        pygame.draw.polygon(self.screen, self.color_prms['red_1'], [(940, 700), (955, 715), (970, 700)])
        pygame.draw.circle(self.screen, self.color_prms['blue_1'], (15, 693), 5)
        pygame.draw.polygon(self.screen, self.color_prms['blue_1'], [(10, 693), (10, 713), (20, 713), (20, 693)])
        self.screen.blit(self.remain_life_img, self.remain_life_rect)
        self.screen.blit(self.remain_bomb_img, self.remain_bomb_rect)

    #定義訊息繪製更新
    #Drawing update
    def update(self):
        self.character_status = self.game_status.get_character_status()
        self.remain_life = str(self.character_status['remain_life'])
        self.remain_bomb = str(self.character_status['remain_bomb'])
        self.remain_life_img = self.remain_font.render(self.remain_life, True, self.color_prms['white'])
        self.remain_bomb_img = self.remain_font.render(self.remain_bomb, True, self.color_prms['white'])
        self.remain_life_rect = self.remain_life_img.get_rect()
        self.remain_life_rect.center = (985, 700)
        self.remain_bomb_rect = self.remain_bomb_img.get_rect()
        self.remain_bomb_rect.center = (40, 700)
