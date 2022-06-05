import os
import pygame
import pygame_menu
import random
import sys
from pygame.locals import *
from data.Defs import *

direction = {None: (0, 0), pygame.K_w: (0, -2), pygame.K_s: (0, 2),
             pygame.K_a: (-2, 0), pygame.K_d: (2, 0)}

direction2 = {None: (0, 0), pygame.K_UP: (0, -2), pygame.K_DOWN: (0, 2),
             pygame.K_LEFT: (-2, 0), pygame.K_RIGHT: (2, 0)}

class Display:
    w_init = 1/2
    h_init = 8/9
    angle = 0
    help_scale = (0.4,0.4) 

class Utillization:
    x = 0
    y = 1

class Pvp:
    def __init__(self, screen):

        pygame.init()
        infoObject = pygame.display.Info()
        size = [int(infoObject.current_w*Display.w_init),int(infoObject.current_h*Display.h_init)] #사이즈 설정(w,h) 
        screen = pygame.display.set_mode(size,pygame.RESIZABLE) #창크기 조정 가능 
        ww, wh= pygame.display.get_surface().get_size() 
        Default.game.value["size"]["x"] = size[0] #Default는 Defs.py에 선언되어 있는 클래스명
        Default.game.value["size"]["y"] = size[1]


        #background = pygame.image.load(Images.start.value) #기존 코드에 있었는데 필요한지 몰겠음!
        base_font = pygame.font.Font(None,32) #기본 폰트


    def playGame(self):
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
                    size = window_size

                #배경 이미지 설정
                image1 = pygame.image.load("Image/Login.png") #왼쪽배경 이미지
                image1 = pygame.transform.scale(image1, (size[0]/2,size[1])) #왼쪽배경이미지 크기

                image2 = pygame.image.load("Image/Login.png") #오른쪽배경 이미지
                image2 = pygame.transform.scale(image2, (size[0]/2,size[1])) #오른쪽배경이미지 크기
                

                #방향키 설정
                direction = {None: (0, 0), pygame.K_w: (0, -2), pygame.K_s: (0, 2),
                            pygame.K_a: (-2, 0), pygame.K_d: (2, 0)}

                direction2 = {None: (0, 0), pygame.K_UP: (0, -2), pygame.K_DOWN: (0, 2),
                            pygame.K_LEFT: (-2, 0), pygame.K_RIGHT: (2, 0)}


                # 화면에 그리기
                screen.fill((25, 0, 50)) #값 변경해보고 지워봤는데 큰 변화 없음. 없어도 되는 기능인듯?
                screen.blit(image1, [0,0]) #왼쪽배경이미지 출력
                screen.blit(image2, [size[0]/2,0]) #왼쪽배경이미지 출력

                pygame.display.flip() #화면이 계속 업데이트 될 수 있도록 설정