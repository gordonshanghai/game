import pygame
from pygame.sprite import Sprite
 
class Ship(Sprite):
  '''飞船所有信息'''
 
  def __init__(self,ai_settings,screen):
    """初始化飞船，并设置其起始位置"""
    super(Ship,self).__init__()
    self.screen=screen
    self.ai_settings = ai_settings
 
    # 加载飞船图片、获取外接矩形
    #self.image = pygame.image.load(self.ai_settings.ship_image_path)  # 加载图片
    self.image = pygame.image.load(r'C:\Users\pc\Desktop\game\xixi.jpg')
    self.image = pygame.transform.smoothscale(self.image,(40,60))
    self.rect = self.image.get_rect()  # 获取图片外接矩形
    self.screen_rect = screen.get_rect()    #获取屏幕外接矩形
    print("self.rect.height= ",self.rect.height)
 
    # 将每搜新飞船放到并木底部中心
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom
    assert self.rect.top == self.rect.bottom - self.rect.height
    
    # 设置成浮点类型
    self.center = float(self.rect.centerx)   # self.rect.centerx设置不了浮点数 只能另设置一个变量进行运算
    self.top = float(self.rect.bottom - self.rect.height )
    
    
    self.bottom = float(self.rect.bottom)
    
 
    # 移动标志
    self.moving_right = False
    self.moving_left = False
    self.moving_up = False
    self.moving_down = False
 
  def blitme(self):
    '''在指定位置绘制飞船'''
    self.screen.blit(self.image,self.rect)
 
  def update(self):
    # 向右移动飞船
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.center +=self.ai_settings.ship_speed_factor
    # 向左移动飞船
    if self.moving_left and self.rect.left > self.screen_rect.left:
      self.center -= self.ai_settings.ship_speed_factor
      
    if self.moving_up and self.rect.top > self.screen_rect.top:
      self.top -= self.ai_settings.ship_speed_factor
      
    if self.moving_down and self.rect.top < self.screen_rect.bottom-self.rect.height:
      self.top += self.ai_settings.ship_speed_factor      
 
    self.rect.centerx = self.center
    self.rect.top = self.top
 
  def center_ship(self):
    """让飞船在屏幕上居中"""
    self.center = self.screen_rect.centerx
    self.top = self.screen_rect.bottom-self.rect.height
    print("ship loc",self.center,self.top)
