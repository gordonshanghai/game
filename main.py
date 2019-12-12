import pygame
 
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from pygame.sprite import Group
import game_functions as gf
from scoreboard import Scoreboard
import threading

exitFlag = 0

class mythread(threading.Thread): 
    def __init__(self,threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID

        
        
    def run_game(self):
        pygame.init()    # 初始化背景设置
        ai_settings = Settings()    # 全局设置
     
        screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
        pygame.display.set_caption('yilia_battle_alien')  # 标题
        #新建Play按钮
        play_button = Button(ai_settings,screen,"Play")
        #if stats.game_active:
      
      
        #创建一个用于存储游戏统计信息的实例,并创建记分牌
        stats = GameStats(ai_settings)
        sb = Scoreboard(ai_settings, screen, stats)
        # 创建飞船
        ship = Ship(ai_settings,screen)
        # 创建子弹编组
        bullets = Group()
       
        #创建一个外星人
        aliens = Group() 
        #创建外星人群
        gf.create_fleet(ai_settings,screen,ship,aliens) 
        backimage = pygame.image.load(r'C:\Users\pc\Desktop\game\background.jpg').convert()
        background = pygame.transform.smoothscale(backimage,(1000,600))
        # 开始游戏主循环
        while True: 
            
            screen.blit(background,(0,0))          
            
        # 监视键盘和鼠标事件
        
            gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
         
            if stats.game_active:
                
                # 移动飞船
                gf.update_ship(ship)
                # 更新子弹位置
                gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
                #更新外星人
                gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
            # 更新屏幕
            gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
            
            print("done here")
      
    def play_music(self):
        mixer = pygame.mixer
        mixer.init(11025)
        music = mixer.music
        backgroundsound = r'C:\Users\pc\Desktop\game\nervous.mp3'
        music.load(backgroundsound)
        music.set_volume(3)
        #for i in range(3):
        music.play(loops = -1)
        print("test here",type(music))
        


if __name__ =='__main__':

    thread1 = threading.Thread(target=mythread.run_game, args=(1,))
    thread1.start()
    
    thread2 = threading.Thread(target=mythread.play_music, args=(2,))
    thread2.start()
    
    
    
    
    thread1.join() 
    thread2.join()


# try:
#     _thread.start_new_thread(play_music())
#     _thread.start_new_thread(run_game())
#     
# except:
#     print("some wrong with thread")




        

         
                                     