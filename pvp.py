import os
import pygame
import pygame_menu
import random
import sys
from pygame.locals import *
from data.Defs import *

class Display:
    w_init = 1/2
    h_init = 8/9
    angle = 0
    help_scale = (0.4,0.4) 

class Utillization:
    x = 0
    y = 1

pygame.init()
infoObject = pygame.display.Info()
size = [int(infoObject.current_w*Display.w_init),int(infoObject.current_h*Display.h_init)] #사이즈 설정(w,h) 
screen = pygame.display.set_mode(size,pygame.RESIZABLE) #창크기 조정 가능 
ww, wh= pygame.display.get_surface().get_size() 
Default.game.value["size"]["x"] = size[0] #Default는 Defs.py에 선언되어 있는 클래스명
Default.game.value["size"]["y"] = size[1]
menu_image = pygame_menu.baseimage.BaseImage(image_path=Images.login.value,drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL) #메뉴 이미지, Images는 Defs.py에 선언되어 있는 클래스명
mytheme = pygame_menu.themes.THEME_BLUE # theme 종류 참고 : https://pygame-menu.readthedocs.io/en/3.5.2/_source/themes.html
mytheme.background_color = menu_image 
mytheme.widget_background_color = (150, 213, 252) #버튼 가독성 올리기 위해서 버튼 배경색 설정 : 하늘색
menu = pygame_menu.Menu('DreamsComeTrue', ww,wh,theme=mytheme) #상단바 팀 이름

#background = pygame.image.load(Images.start.value) #기존 코드에 있었는데 필요한지 몰겠음!
base_font = pygame.font.Font(None,32) #기본 폰트

class Pvp():
    def page(): # 첫화면 
        menu.clear()
        menu.add.button('2 Players')
        menu.add.vertical_margin(10)
        menu.add.button('    Quit    ', pygame_menu.events.EXIT)
        mytheme.widget_background_color = (0,0,0,0)

Pvp.page()

if __name__ == '__main__':

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.VIDEORESIZE:
                pass


        if (size != screen.get_size()): #현재 사이즈와 저장된 사이즈 비교 후 다르면 변경
            changed_screen_size = screen.get_size() #변경된 사이즈
            ratio_screen_size = (changed_screen_size[0],changed_screen_size[0]*783/720) #y를 x에 비례적으로 계산
            if(ratio_screen_size[0]<320): #최소 x길이 제한
                ratio_screen_size = (494,537)
            if(ratio_screen_size[1]>783): #최대 y길이 제한
                ratio_screen_size = (720,783)
            screen = pygame.display.set_mode(ratio_screen_size,pygame.RESIZABLE)
            window_size = screen.get_size()
            new_w, new_h = 1 * window_size[0], 1 * window_size[1]
            menu.resize(new_w, new_h)
            size = window_size
            print(f'New menu size: {menu.get_size()}')

        # 화면에 메뉴 그리기
        screen.fill((25, 0, 50)) #값 변경해보고 지워봤는데 큰 변화 없음. 없어도 되는 기능인듯?

        menu.update(events)
        menu.draw(screen)
        #pygame.draw.rect(screen,color,input_rect,2)


        pygame.display.flip() #화면이 계속 업데이트 될 수 있도록 설정