import pygame
from pygame.sprite import Sprite
import time
 
class Bullet(Sprite):
  '''飞船子弹进行管理'''
 
  def __init__(self,ai_settings,screen,ship):
    super(Bullet,self).__init__()
    self.screen = screen
 
    # 创建子弹矩形初始位置（0,0,3,15）分别对应lef，top，宽，高
    self.rect = pygame.Rect(0,0,ai_settings.bullet_width, ai_settings.bullet_height) 
    self.rect.centerx = ship.rect.centerx # 设置中心点x轴坐标跟飞船一致,子弹从飞船射出
    self.rect.top = ship.rect.top     # 设置y轴坐标顶部跟飞船一致
 
    # 设置成小数进行计算
    self.top = float(self.rect.top)

 
    self.color = ai_settings.bullet_color
    self.speed_factor = ai_settings.bullet_speed_factor
 
  def update(self):
      

    self.top -=self.speed_factor  #子弹向上飞，即y值减少
    #print("111",self.top)
    self.rect.top = self.top
    #print(self.rect.top)    
    #self.rect.centerx -= 2*self.speed_factor
    
    #self.speed = ai_settings.bullet_speed_factor
    

 
  def draw_bullet(self):
    pygame.draw.rect(self.screen,self.color,self.rect)

    
