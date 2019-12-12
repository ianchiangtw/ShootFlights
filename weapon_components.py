# Python 3.7
# weapon_components.py
# Ian: ianisablackcat@gmail.com
# 2019.03.07

import pygame, time, random, threading
import program_data as pd
from pygame.sprite import Sprite


#玩家角色武器模板
#Player weapon templaate
class PlayerWeaponOne(Sprite):
    def __init__(self, screen, x, y, direction):
        super(PlayerWeaponOne, self).__init__()
        self.screen = screen
        #載入參數
        #Load parameters
        self.weapon_prms = pd.player_weapon_parameters()
        self.rect = pygame.Rect(0, 0, self.weapon_prms['width'], self.weapon_prms['height'])
        self.rect.centerx, self.rect.bottom = x, y
        self.x, self.y = self.rect.left, self.rect.top
        self.color = self.weapon_prms['color']
        self.factor = self.weapon_prms['factor']
        self.direction = direction
    
    #畫面繪製
    #Shape drawing
    def draw(self):
        if self.direction == 7:
            pygame.draw.polygon(self.screen, self.color, [[self.x, self.y],
                                                          [self.x - 2, self.y - 8],
                                                          [self.x, self.y - 10],
                                                          [self.x + 2, self.y - 2]])
        elif self.direction == 8:
            pygame.draw.rect(self.screen, self.color, self.rect)
        elif self.direction == 9:
            pygame.draw.polygon(self.screen, self.color, [[self.x, self.y],
                                                          [self.x - 2, self.y - 2],
                                                          [self.x, self.y - 10],
                                                          [self.x + 2, self.y - 8]])

    #移動位置更新
    #Moving position update
    def update(self):
        if self.direction == 7:
            self.x -= self.factor / 2
            self.y -= self.factor / 2
            self.rect.centerx = self.x
            self.rect.centery = self.y
        elif self.direction == 8:
            self.rect.bottom -= self.factor
        elif self.direction == 9:
            self.x += self.factor / 2
            self.y -= self.factor / 2
            self.rect.centerx = self.x
            self.rect.centery = self.y


#玩家角色炸彈模板
#Player bomb template
class Bomb(Sprite):
    def __init__(self, screen):
        super(Bomb, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0, 0, 500, 400)
        self.rect.center = self.screen_rect.center
        #參數設定
        #Set parameters
        self.color_1 = (250, 250, 250)
        self.color_2 = (220, 220, 0)
        self.color_3 = (220, 0, 0)
        self.radius_1 = 10
        self.radius_2 = 40
        self.radius_3 = 8
        self.width_1 = 10
        self.width_2 = 40
        self.width_3 = 8
        self.factor = 2

    #畫面繪製
    #Shape drawing
    def draw(self):
        pygame.draw.circle(self.screen, self.color_1, self.screen_rect.center, self.radius_1, self.width_1)
        pygame.draw.circle(self.screen, self.color_1, self.screen_rect.center, self.radius_2, self.width_2)
        pygame.draw.circle(self.screen, self.color_1, self.screen_rect.center, self.radius_3, self.width_3)

    #爆炸動畫位置更新
    #Animation position update
    def update(self):
        self.radius_3 += self.factor
        if self.radius_3 > 53:
            self.radius_2 += self.factor
        if self.radius_3 > 68:
            self.radius_1 += self.factor
        if self.radius_1 >= 350:
            self.rect = self.screen_rect

#一般敵方角色武器模板
#Enemy flight weapon template
class EnemyBullet(Sprite):
    def __init__(self, screen, bullet_prms, bullet_factor, x, y):
        super(EnemyBullet, self).__init__()
        self.screen = screen
        #載入參數
        #Load parameters
        self.factor = bullet_factor
        self.rect = pygame.Rect(0, 0, bullet_prms['width'], bullet_prms['height'])
        self.rect.centerx, self.rect.top = x, y
        self.y = int(self.rect.top)
        self.color = bullet_prms['color']

    #畫面繪製
    #Shape drawing
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    #子彈位置更新
    #Moving position update
    def update(self):
        self.y += self.factor
        self.rect.top = self.y


#敵方魔王直線射擊武器模板
#Straight shooting weapon of level demon lord template
class BossBullet(Sprite):
    def __init__(self, screen, boss_prms, bullet_factor, start_x, start_y, target_x, target_y):
        super(BossBullet, self).__init__()
        self.screen = screen
        #載入參數
        #Load parameters
        self.color = boss_prms['bullet_color']
        self.radius = boss_prms['bullet_radius']
        self.rect_side_length = int(2 * (((self.radius ** 2) / 2) ** 0.5))
        self.rect = pygame.Rect(0, 0, self.rect_side_length, self.rect_side_length)
        self.rect.centerx, self.rect.centery = start_x, start_y
        self.x, self.y = int(self.rect.centerx), int(self.rect.centery)
        self.slope = bullet_factor / (((target_x - start_x) ** 2 + (target_y - start_y) ** 2) ** 0.5)
        self.factor_x = (target_x - start_x) * self.slope
        self.factor_y = (target_y - start_y) * self.slope

    #畫面繪製
    #Shape drawing
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.rect.centerx, self.rect.centery), self.radius)

    #子彈位置更新
    #Moving position update
    def update(self):
        self.x += self.factor_x
        self.y += self.factor_y
        self.rect.centerx = self.x
        self.rect.centery = self.y


#敵方魔王環狀射擊武器模板
#Circle shooting weapon of level demon lord template
class BossCircleBullet(Sprite):
    def __init__(self, screen, boss_prms, bullet_factor, start_x, start_y, factor_x, factor_y):
        super(BossCircleBullet, self).__init__()
        self.screen = screen
        #載入參數
        #Load parameters
        self.color = boss_prms['bullet_color']
        self.radius = boss_prms['bullet_radius']
        self.rect_side_length = int(2 * (((self.radius ** 2) / 2) ** 0.5))
        self.rect = pygame.Rect(0, 0, self.rect_side_length, self.rect_side_length)
        self.rect.centerx = start_x
        self.rect.centery = start_y
        self.x = int(self.rect.centerx)
        self.y = int(self.rect.centery)
        self.factor = bullet_factor
        self.factor_x = factor_x
        self.factor_y = factor_y

    #畫面繪製
    #Shape drawing
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.rect.centerx, self.rect.centery), self.radius)

    #子彈位置更新
    #Moving position update
    def update(self):
        self.x += (self.factor_x * self.factor)
        self.y += (self.factor_y * self.factor)
        self.rect.centerx = self.x
        self.rect.centery = self.y


#武器寶珠模板
#Weapon bonus template
class Bonus(Sprite):
    def __init__(self, screen, position):
        super(Bonus, self).__init__()
        self.screen = screen
        #載入參數
        #Load parameters
        self.x = position[0]
        self.y = position[1]
        self.rect = pygame.Rect(0, 0, 30, 30)
        self.text_1 = 'M'
        self.text_color = (0, 0, 0)
        self.back_color = (250, 175, 0)
        self.bonus_font = pygame.font.Font("font/msjhbd.ttc", 20)
        self.bonus_img = self.bonus_font.render(self.text_1, True, self.text_color)
        self.bonus_rect = self.bonus_img.get_rect()
        self.bonus_rect.center = self.rect.center = (self.x, self.y)
        self.radius = 15
        self.factor = 0.2
        self.factor_x = int(random.choice([1, -1])) * self.factor
        self.factor_y = int(random.choice([1, -1])) * self.factor
        self.start_time = time.time()
        self.active = True

    #畫面繪製
    #Shape drawing
    def draw(self):
        pygame.draw.circle(self.screen, self.back_color, self.bonus_rect.center, self.radius)
        self.screen.blit(self.bonus_img, self.bonus_rect)

    #子彈位置更新
    #Moving position update
    def update(self):
        if (time.time() - self.start_time) > 20: self.active = False
        if self.x < 50: self.factor_x = self.factor
        elif self.x > 950: self.factor_x = self.factor * -1
        if self.y < 50: self.factor_y = self.factor
        elif self.y > 670: self.factor_y = self.factor * -1
        self.x += self.factor_x
        self.y += self.factor_y
        self.bonus_rect.center = self.rect.center = (int(self.x), int(self.y))


#角色被擊中時的爆炸動畫
#Explosion animation when character be hitted
class HitExplode(Sprite):
    def __init__(self, screen, x, y):
        super(HitExplode, self).__init__()
        self.screen = screen
        #載入參數
        #Load parameters
        self.x, self.y = x, y
        self.exp_img = pygame.image.load('images/exp_1.png').convert_alpha()
        self.exp_rect = self.exp_img.get_rect()
        self.exp_rect.center = (self.x, self.y)
        self.exp_time = time.time()
        self.exp_num = 1
        self.active = True

    #載入爆炸動畫
    #Load picture
    def draw(self):
        self.screen.blit(self.exp_img, self.exp_rect)

    #動畫圖片更新
    #Animation pictures update
    def update(self):
        if time.time() - self.exp_time > 0.05:
            self.exp_num += 1
            if self.exp_num >= 4:
                self.active = False
            else:
                self.exp_img = pygame.image.load('images/exp_' + str(self.exp_num) + '.png').convert_alpha()
                self.exp_rect = self.exp_img.get_rect()
                self.exp_rect.center = (self.x, self.y)
                self.exp_time = time.time()
