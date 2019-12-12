# Python 3.7
# scripts_data.py
# Ian: ianisablackcat@gmail.com
# 2019.03.06


#關卡1劇本
#Level 1 script
def stage_01_scripts():
    stage_scripts = [0,
                     {'qua': 1, 'loc_x': 50, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 150, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 800, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 1, 'loc_x': 200, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     # 5
                     {'qua': 3, 'loc_x': 550, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 0},
                     0,
                     {'qua': 1, 'loc_x': 600, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 2, 'loc_x': 50, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 450, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 1},
                     # 10
                     0,
                     {'qua': 1, 'loc_x': 200, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 500, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 300, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 1},
                     0,
                     # 15
                     {'qua': 1, 'loc_x': 400, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 600, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 800, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 2, 'loc_x': 350, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 800, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 1},
                     # 20
                     0,
                     {'qua': 2, 'loc_x': 150, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     0,
                     0,
                     {'qua': 2, 'loc_x': 450, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     # 25
                     0,
                     {'qua': 1, 'loc_x': 650, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 1},
                     0,
                     {'qua': 1, 'loc_x': 850, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 400, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 1},
                     # 30
                     {'qua': 1, 'loc_x': 800, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 1},
                     0,
                     {'qua': 3, 'loc_x': 400, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 750, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 1, 'loc_x': 200, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 1},
                     # 35
                     {'qua': 1, 'loc_x': 50, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     0,
                     0,
                     {'qua': 2, 'loc_x': 200, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 800, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 0},
                     # 40
                     {'qua': 1, 'loc_x': 500, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 1},
                     0,
                     {'qua': 1, 'loc_x': 650, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 1, 'loc_x': 300, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 2, 'loc_x': 800, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 0},
                     # 45
                     0,
                     {'qua': 1, 'loc_x': 200, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 600, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     0,
                     {'qua': 1, 'loc_x': 600, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 1},
                     # 50
                     {'qua': 1, 'loc_x': 200, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 50, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     0,
                     {'qua': 1, 'loc_x': 500, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 150, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     # 55
                     0,
                     {'qua': 1, 'loc_x': 550, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 0},
                     0,
                     {'qua': 1, 'loc_x': 400, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 1, 'loc_x': 200, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0}]
                     # 60
    return stage_scripts


#關卡2劇本
#Level 2 script
def stage_02_scripts():
    stage_scripts = [0,
                     {'qua': 2, 'loc_x': 50, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     0,
                     {'qua': 2, 'loc_x': 800, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 200, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 1},
                     # 5
                     {'qua': 3, 'loc_x': 550, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 300, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 1},
                     0,
                     {'qua': 2, 'loc_x': 50, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 450, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 1},
                     # 10
                     {'qua': 1, 'loc_x': 800, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 2, 'loc_x': 200, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     0,
                     {'qua': 1, 'loc_x': 300, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 3, 'loc_x': 200, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     # 15
                     {'qua': 1, 'loc_x': 400, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 2, 'loc_x': 600, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 800, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 2, 'loc_x': 350, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 1},
                     0,
                     # 20
                     0,
                     {'qua': 2, 'loc_x': 150, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 250, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 350, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 1},
                     0,
                     # 25
                     {'qua': 1, 'loc_x': 550, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 2, 'loc_x': 650, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     0,
                     {'qua': 1, 'loc_x': 850, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 400, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 0},
                     # 30
                     {'qua': 3, 'loc_x': 800, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 150, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 3, 'loc_x': 400, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     0,
                     {'qua': 1, 'loc_x': 200, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 1},
                     # 35
                     {'qua': 2, 'loc_x': 50, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     0,
                     {'qua': 1, 'loc_x': 600, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 2, 'loc_x': 200, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     0,
                     # 40
                     {'qua': 3, 'loc_x': 500, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     0,
                     {'qua': 3, 'loc_x': 650, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 300, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 2, 'loc_x': 800, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 0},
                     # 45
                     {'qua': 1, 'loc_x': 400, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     0,
                     {'qua': 1, 'loc_x': 600, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 3, 'loc_x': 800, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 0},
                     0,
                     # 50
                     {'qua': 2, 'loc_x': 200, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     0,
                     {'qua': 2, 'loc_x': 300, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 500, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 1},
                     0,
                     # 55
                     {'qua': 3, 'loc_x': 300, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     0,
                     {'qua': 2, 'loc_x': 800, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 400, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 1},
                     0]
                     # 60
    return stage_scripts


#關卡3劇本
#Level 3 script
def stage_03_scripts():
    stage_scripts = [0,
                     {'qua': 1, 'loc_x': 50, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 3, 'loc_x': 150, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 3, 'loc_x': 800, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 3, 'loc_x': 200, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     # 5
                     {'qua': 3, 'loc_x': 550, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 3, 'loc_x': 300, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 2, 'loc_x': 600, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 2, 'loc_x': 50, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 450, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 1},
                     # 10
                     {'qua': 2, 'loc_x': 800, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 200, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 2, 'loc_x': 500, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 3, 'loc_x': 300, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 3, 'loc_x': 200, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 1},
                     # 15
                     {'qua': 2, 'loc_x': 400, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 2, 'loc_x': 600, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 3, 'loc_x': 800, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 2, 'loc_x': 350, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 3, 'loc_x': 800, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 1},
                     # 20
                     {'qua': 3, 'loc_x': 50, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 2, 'loc_x': 150, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 2, 'loc_x': 250, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 1, 'loc_x': 350, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 2, 'loc_x': 450, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 1},
                     # 25
                     {'qua': 1, 'loc_x': 550, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 3, 'loc_x': 650, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 2, 'loc_x': 750, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 850, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 2, 'loc_x': 400, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 0},
                     # 30
                     {'qua': 1, 'loc_x': 800, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 3, 'loc_x': 150, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 3, 'loc_x': 400, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 3, 'loc_x': 750, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 200, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 1},
                     # 35
                     {'qua': 2, 'loc_x': 50, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 2, 'loc_x': 300, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 2, 'loc_x': 600, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 2, 'loc_x': 200, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 3, 'loc_x': 800, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 1},
                     # 40
                     {'qua': 3, 'loc_x': 500, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 50, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 3, 'loc_x': 650, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 300, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 2, 'loc_x': 800, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 0},
                     # 45
                     {'qua': 3, 'loc_x': 400, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 200, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 2, 'loc_x': 600, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 3, 'loc_x': 800, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 600, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 1},
                     # 50
                     {'qua': 3, 'loc_x': 200, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 1, 'loc_x': 50, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 2, 'loc_x': 300, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 2, 'loc_x': 500, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 2, 'loc_x': 150, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 1},
                     # 55
                     {'qua': 2, 'loc_x': 300, 'loc_y': -30, 'move_mode': 2, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 2, 'loc_x': 550, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 3, 'loc_x': 800, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 1},
                     {'qua': 3, 'loc_x': 400, 'loc_y': -30, 'move_mode': 1, 'attack_mode': 1, 'bonus': 0},
                     {'qua': 3, 'loc_x': 200, 'loc_y': -30, 'move_mode': 3, 'attack_mode': 1, 'bonus': 1}]
                     # 60
    return stage_scripts
