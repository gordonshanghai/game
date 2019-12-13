import pygame

class Settings():
  '''存储外星人入侵中所有的设置'''
 
  def __init__(self):
    '''初始化设置'''
    #屏幕设置
    self.screen_width = 1000
    self.screen_height = 600
    self.bg_color = (230,230,230)  # 设置背景色 灰色
    
     
    #飞船设置
    self.ship_limit = 1
    self.ship_image_path = r'C:\Users\pc\Desktop\personal\1inchcolor'  # 飞船图片路径
     
    #子弹设置
    self.bullet_width = 5
    self.bullet_height = 10
    self.bullet_color = 200,60,0
    self.bullets_allowed = 5     # 允许屏幕中出现子弹的数量
    
    self.mixer = pygame.mixer
    self.mixer.init(11025)
    self.music = self.mixer.music
    self.bulletsound = r'C:\Users\pc\Desktop\game\fire.mp3'
    self.music.load(self.bulletsound)
    self.music.set_volume(2)
    
     
    #外星人设置
    self.fleet_drop_speed = 10
     
     
    #以什么样的速度加快游戏节奏
    self.speedup_scale = 2
    #外星人点数提高速度
    self.score_scale = 1.5
     
    self.initialize_dynamic_settings()
   
  def initialize_dynamic_settings(self):
    """初始化随游戏进行而变化的设置"""
    self.ship_speed_factor = 2
    self.bullet_speed_factor = 3
    self.alien_speed_factor = 1
     
    #fleet_direction为1表示向右移，为-1表示向左移
    self.fleet_direction = 1
     
    #计分
    self.alien_points = 50
     
  def increase_speed(self):
      self.ship_speed_factor *= self.speedup_scale
      self.bullet_speed_factor *= self.speedup_scale
      self.alien_speed_factor *= self.speedup_scale
      #self.alien_points = 50 
      self.alien_points = int(self.alien_points * self.score_scale)
      print(self.alien_points)
      """提高速度设置,外星人点数"""

  
sset = Settings()
sset.increase_speed()
print("111")
