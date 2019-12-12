# Python 3.7
# program_data.py
# Ian: ianisablackcat@gmail.com
# 2019.03.07

import pygame.font
pygame.font.init()


#遊戲執行狀態紀錄標籤
#Game execution status label
class GameStatus:
    def __init__(self):
        self.current_scenes = 0
        self.next_stage = 1
        self.game_active = True
        self.bomb_exploding = False
        self.player_preset_life = 3
        self.player_preset_bomb = 3

        self.player_remain_life = 3
        self.player_remain_bomb = 3
        self.current_weapon = 1
        self.stage_remain_boss = 0

        self.current_enemy_score = 0
        self.current_boss_score = 0
        self.current_stage_score = 0
        self.total_score = 0

    def get_current_scenes(self):
        return self.current_scenes

    def get_game_active(self):
        return self.game_active

    def get_character_status(self):
        return {'remain_life': self.player_remain_life, 'remain_bomb': self.player_remain_bomb,
                'remain_boss': self.stage_remain_boss}

    def get_game_score(self):
        return {'enemy': self.current_enemy_score, 'boss': self.current_boss_score, 'stage': self.current_stage_score,
                'total': self.total_score}

    def get_bomb_exploding(self):
        return self.bomb_exploding

    def set_bomb_exploding(self):
        self.bomb_exploding = not self.bomb_exploding

    def set_bomb_cut(self):
        self.player_remain_bomb -= 1

    def set_player_cut(self):
        self.player_remain_life -= 1

    def set_bonus(self, prms):
        if prms == 99:
            self.current_weapon = 1
        else:
            self.current_weapon += prms
        if self.current_weapon > 4:
            self.current_weapon = 4

    def set_boss_cut(self):
        self.stage_remain_boss -= 1

    def set_gameover(self):
        self.game_active = False

    def set_stage_boss_amount(self, num):
        self.stage_remain_boss = num

    def jump_to_settle_page(self):
        self.current_scenes = 99

    def jump_to_next_stage(self):
        if self.game_active:
            self.current_scenes = self.next_stage
            self.next_stage += 1
            if self.next_stage == 4: self.next_stage = 0
            self.current_enemy_score = self.current_boss_score = 0
        else:
            self.current_scenes = 0
            self.next_stage = 1
            self.reset_game()
        pygame.event.clear()

    def add_score(self, score_type, num):
        if score_type == 'enemy':
            self.current_enemy_score += num
            self.current_stage_score = self.current_enemy_score + self.current_boss_score
            self.total_score += num
        elif score_type == 'boss':
            self.current_boss_score += num
            self.current_stage_score = self.current_enemy_score + self.current_boss_score
            self.total_score += num

    def reset_game(self):
        self.player_remain_life = self.player_preset_life
        self.player_remain_bomb = self.player_preset_bomb
        self.current_enemy_score = self.current_boss_score = self.current_stage_score = self.total_score = 0
        self.current_weapon = 1
        self.game_active = True


#開始頁面參數
#Start page parameters
def system_parameters():
    sys_prms = {'screen_width': 1000, 'screen_height': 720, 'screen_title': 'ABYSSINIAN'}
    return sys_prms


#開始頁面參數
#Start page parameters
def opening_page_parameters(screen):
    screen_rect = screen.get_rect()
    op_top = "ABYSSINIAN"
    op_L1 = "PRESS < SPACE > TO START"
    op_L2L = "top left : <Num_7>"
    op_L2M = "up : UP or <Num_8>"
    op_L2R = "top right : <Num_9>"
    op_L3L = "left : LEFT or <Num_4>"
    op_L3R = "right : RIGHT or <Num_6>"
    op_L4L = "bottom left : <Num_1>"
    op_L4M = "down : DOWN or <Num_2>"
    op_L4R = "bottom right : <Num_3>"
    op_L5 = "attack : <SPACE>        bomb : <M>"
    op_bottom = "Ian Chiang 2019"
    op_top_color = (210, 40, 50)
    op_L1_color = (240, 240, 0)
    op_content_color = (210, 210, 210)
    op_bottom_color = (0, 0, 255)
    op_top_font = pygame.font.Font("font/comicbd.ttf", 120)
    op_L1_font = pygame.font.Font("font/comic.ttf", 50)
    op_content_font = pygame.font.Font("font/calibri.ttf", 20)
    op_bottom_font = pygame.font.Font("font/comic.ttf", 20)
    op_top_img = op_top_font.render(op_top, True, op_top_color)
    op_L1_img = op_L1_font.render(op_L1, True, op_L1_color)
    op_L2L_img = op_content_font.render(op_L2L, True, op_content_color)
    op_L2M_img = op_content_font.render(op_L2M, True, op_content_color)
    op_L2R_img = op_content_font.render(op_L2R, True, op_content_color)
    op_L3L_img = op_content_font.render(op_L3L, True, op_content_color)
    op_L3R_img = op_content_font.render(op_L3R, True, op_content_color)
    op_L4L_img = op_content_font.render(op_L4L, True, op_content_color)
    op_L4M_img = op_content_font.render(op_L4M, True, op_content_color)
    op_L4R_img = op_content_font.render(op_L4R, True, op_content_color)
    op_L5_img = op_content_font.render(op_L5, True, op_content_color)
    op_bottom_img = op_bottom_font.render(op_bottom, True, op_bottom_color)
    op_top_rect = op_top_img.get_rect()
    op_top_rect.centerx, op_top_rect.top = screen_rect.centerx, 120
    op_L1_rect = op_L1_img.get_rect()
    op_L1_rect.centerx, op_L1_rect.top = screen_rect.centerx, 340
    op_L2L_rect = op_L2L_img.get_rect()
    op_L2M_rect = op_L2M_img.get_rect()
    op_L2R_rect = op_L2R_img.get_rect()
    op_L2L_rect.left, op_L2L_rect.y = 150, 450
    op_L2M_rect.centerx, op_L2M_rect.y = screen_rect.centerx, 450
    op_L2R_rect.right, op_L2R_rect.y = 850, 450
    op_L3L_rect = op_L3L_img.get_rect()
    op_L3R_rect = op_L3R_img.get_rect()
    op_L3L_rect.left, op_L3L_rect.y = 150, 480
    op_L3R_rect.right, op_L3R_rect.y = 850, 480
    op_L4L_rect = op_L4L_img.get_rect()
    op_L4M_rect = op_L4M_img.get_rect()
    op_L4R_rect = op_L4R_img.get_rect()
    op_L4L_rect.left, op_L4L_rect.y = 150, 510
    op_L4M_rect.centerx, op_L4M_rect.y = screen_rect.centerx, 510
    op_L4R_rect.right, op_L4R_rect.y = 850, 510
    op_L5_rect = op_L5_img.get_rect()
    op_L5_rect.centerx, op_L5_rect.top = screen_rect.centerx, 540
    op_bottom_rect = op_bottom_img.get_rect()
    op_bottom_rect.centerx, op_bottom_rect.top = screen_rect.centerx, 680
    op_imgs = [op_top_img, op_L2L_img, op_L2M_img, op_L2R_img, op_L3L_img, op_L3R_img, op_L4L_img,
               op_L4M_img, op_L4R_img, op_L5_img, op_bottom_img]
    op_rects = [op_top_rect, op_L2L_rect, op_L2M_rect, op_L2R_rect, op_L3L_rect, op_L3R_rect, op_L4L_rect,
               op_L4M_rect, op_L4R_rect, op_L5_rect, op_bottom_rect]
    op_press = [op_L1_img, op_L1_rect]
    return op_imgs, op_rects, op_press


#關卡1敵方角色數量設定
#Level 1 amount of quantity
def stage_01_parameters():
    stage_enemy_prms = {'stage': 1, 'enemy_fighter_factor': 0.1, 'enemy_bullet_factor': 0.5, 'enemy_fire_rate': 6,
                        'boss_factor': 1, 'boss_bullet_factor': 0.5, 'boss_fire_rate': 4}
    boss_amount = 1
    return stage_enemy_prms, boss_amount


#關卡2敵方角色數量設定
#Level 2 amount of quantity
def stage_02_parameters():
    stage_enemy_prms = {'stage': 2, 'enemy_fighter_factor': 0.2, 'enemy_bullet_factor': 0.5, 'enemy_fire_rate': 5,
                        'boss_factor': 1, 'boss_bullet_factor': 1, 'boss_fire_rate': 4}
    boss_amount = 2
    return stage_enemy_prms, boss_amount


#關卡3敵方角色數量設定
#Level 3 amount of quantity
def stage_03_parameters():
    stage_enemy_prms = {'stage': 3, 'enemy_fighter_factor': 0.3, 'enemy_bullet_factor': 1, 'enemy_fire_rate': 4,
                        'boss_factor': 1.5, 'boss_bullet_factor': 1.5, 'boss_fire_rate': 4}
    boss_amount = 3
    return stage_enemy_prms, boss_amount


#結算頁面參數
#Settle page parameters
def settle_page_parameters(screen, game_active, score):
    screen_rect = screen.get_rect()
    stl_title1 = 'STAGE CLEAR'
    stl_title2 = 'GAME OVER'
    stl_L3L = 'STAGE SCORE'
    stl_L4 = 'TOTAL SCORE  '
    stl_press = 'PRESS SPACE TO NEXT STAGE'
    stl_title_color = (255, 255, 0)
    stl_color = (255, 255, 255)
    stl_L4_color = (255, 0, 0)
    stl_press_color = (0, 0, 255)
    stl_title_font = pygame.font.Font("font/comicbd.ttf", 100)
    stl_font = pygame.font.Font("font/comic.ttf", 50)
    stl_L5_font = pygame.font.Font("font/comicbd.ttf", 70)
    stl_press_font = pygame.font.Font("font/comicbd.ttf", 50)
    stl_title1_img = stl_title_font.render(stl_title1, True, stl_title_color)
    stl_title2_img = stl_title_font.render(stl_title2, True, stl_title_color)
    stl_L1_img = stl_font.render(str(score['enemy']), True, stl_color)
    stl_L2_img = stl_font.render(str(score['boss']), True, stl_color)
    stl_L3L_img = stl_font.render(stl_L3L, True, stl_color)
    stl_L3R_img = stl_font.render(str(score['stage']), True, stl_color)
    stl_L4_img = stl_L5_font.render(stl_L4 + str(score['total']), True, stl_L4_color)
    stl_press_img = stl_press_font.render(stl_press, True, stl_press_color)
    stl_title1_rect = stl_title1_img.get_rect()
    stl_title1_rect.centerx, stl_title1_rect.centery = screen_rect.centerx, 100
    stl_title2_rect = stl_title2_img.get_rect()
    stl_title2_rect.centerx, stl_title2_rect.centery = screen_rect.centerx, 100
    stl_L1_rect = stl_L1_img.get_rect()
    stl_L1_rect.right, stl_L1_rect.centery = 800, 210
    stl_L2_rect = stl_L2_img.get_rect()
    stl_L2_rect.right, stl_L2_rect.centery = 800, 290
    stl_L3L_rect = stl_L3L_img.get_rect()
    stl_L3L_rect.left, stl_L3L_rect.centery = 200, 370
    stl_L3R_rect = stl_L3R_img.get_rect()
    stl_L3R_rect.right, stl_L3R_rect.centery = 800, 370
    stl_L4_rect = stl_L4_img.get_rect()
    stl_L4_rect.center = 500, 480
    stl_press_rect = stl_press_img.get_rect()
    stl_press_rect.centerx, stl_press_rect.centery = screen_rect.centerx, 600
    graphics_data = {'enemy_x': 385, 'enemy_y': 190, 'boss_x': 385, 'boss_y': 290, 'white': (255, 255, 255),
                     'gray_1': (140, 140, 140), 'gray_3': (100, 100, 100), 'boss_color': (255, 0, 0)}
    if game_active:
        stl_imgs1 = [stl_title1_img, stl_L1_img, stl_L2_img, stl_L3L_img, stl_L3R_img, stl_L4_img, stl_press_img]
        stl_rects1 = [stl_title1_rect, stl_L1_rect, stl_L2_rect, stl_L3L_rect, stl_L3R_rect, stl_L4_rect,
                      stl_press_rect]
        return stl_imgs1, stl_rects1, graphics_data
    else:
        stl_imgs2 = [stl_title2_img, stl_L1_img, stl_L2_img, stl_L3L_img, stl_L3R_img, stl_L4_img]
        stl_rects2 = [stl_title2_rect, stl_L1_rect, stl_L2_rect, stl_L3L_rect, stl_L3R_rect, stl_L4_rect]
        return stl_imgs2, stl_rects2, graphics_data


#遊戲畫面顯示資訊參數
#Game info display parameters
def show_status_info_parameters():
    color_prms = {'white': (255, 255, 255), 'red_1': (210, 40, 50), 'blue_1': (0, 0, 255)}
    return color_prms


#玩家角色參數
#Player character parameters
def player_parameters():
    color_prms = {'gray_1': (140, 140, 140), 'gray_2': (120, 120, 120), 'red_1': (210, 40, 50), 'red_2': (180, 20, 30),
                  'yellow_1': (240, 240, 0)}
    player_prms = {'factor': 1}
    return color_prms, player_prms


#一般敵機參數
#Enemy flight parameters
def enemy_parameters():
    color_prms = {'white': (255, 255, 255), 'gray_1': (140, 140, 140), 'gray_3': (100, 100, 100)}
    bullet_prms = {'width': 5, 'height': 10, 'color': (240, 240, 0)}
    return color_prms, bullet_prms


#關卡魔王參數
#Level demon lord parameters
def boss_parameters():
    boss_prms = {'color': (255, 0, 0), 'life_value': 30, 'bullet_color': (255, 125, 40), 'bullet_radius': 8}
    bullet_dirction_prmsx1 = [0.309, 0, -0.309, -0.5878, -0.809, -0.9511]
    bullet_dirction_prmsy1 = [0.9511, 1, 0.9511, 0.809, 0.5878, 0.309]
    bullet_dirction_prmsx2 = [0.309, 0, -0.309, 0.5878, 0.809, 0.9511]
    bullet_dirction_prmsy2 = [0.9511, 1, 0.9511, 0.809, 0.5878, 0.309]
    return boss_prms, [bullet_dirction_prmsx1, bullet_dirction_prmsy1, bullet_dirction_prmsx2, bullet_dirction_prmsy2]


#玩家武器參數
#Player weapon parameters
def player_weapon_parameters():
    bullet_prms = {'width': 5, 'height': 10, 'color': (0, 0, 255), 'factor': 2}
    return bullet_prms


#玩家炸彈參數
#Player bomb parameters
def player_bomb_parameters():
    pass
