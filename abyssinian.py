# Python 3.7
# abyssinian.py
# Ian: ianisablackcat@gmail.com
# 2019.03.07


import pygame
from program_data import GameStatus
from stage_components import *
import program_data as pd


def abyssinian():
    #遊戲主程式函式, 初始化環境及變數
    #Main function, initialize enviroment variables
    game_status = GameStatus()
    sys_prms = pd.system_parameters()
    screen = pygame.display.set_mode((sys_prms['screen_width'], sys_prms['screen_height']))
    pygame.display.set_caption(sys_prms['screen_title'])
    pygame.mouse.set_visible(False)

    #主程式執行迴圈
    #Main game program loop
    while True:
        #Load the script, component tmplates and parameters based on the current level
        current_scenes = game_status.get_current_scenes()
        if current_scenes == 0:
            current_stage = OpeningPage(screen, game_status)
            current_stage.play_stage()
        elif current_scenes == 1:
            stage_enemy_prms, boss_amount = pd.stage_01_parameters()
            current_stage = Stage(screen, game_status, stage_enemy_prms, boss_amount)
            current_stage.play_stage()
        elif current_scenes == 2:
            stage_enemy_prms, boss_amount = pd.stage_02_parameters()
            current_stage = Stage(screen, game_status, stage_enemy_prms, boss_amount)
            current_stage.play_stage()
        elif current_scenes == 3:
            stage_enemy_prms, boss_amount = pd.stage_03_parameters()
            current_stage = Stage(screen, game_status, stage_enemy_prms, boss_amount)
            current_stage.play_stage()
        elif current_scenes == 99:
            current_stage = SettlePage(screen, game_status)
            current_stage.play_stage()


#執行主程式函式
#Run the main function
abyssinian()
