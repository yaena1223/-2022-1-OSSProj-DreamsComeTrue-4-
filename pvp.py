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

class Pvp:
    def __init__(self):
      
        # 1. 게임초기화 
        pygame.init()

        # 2. 게임창 옵션 설정
        infoObject = pygame.display.Info()
        title = "2player game"
        pygame.display.set_caption(title) # 창의 제목 표시줄 옵션
        self.size = [infoObject.current_w,infoObject.current_h]
        self.screen = pygame.display.set_mode(self.size,pygame.RESIZABLE)
        
        
    def background(self):
        #배경 이미지 설정
        image1 = pygame.image.load("Image/Login.png") #왼쪽배경 이미지
        image1 = pygame.transform.scale(image1, (self.size[0]/2,self.size[1])) #왼쪽배경이미지 크기

        image2 = pygame.image.load("Image/Login.png") #오른쪽배경 이미지
        image2 = pygame.transform.scale(image2, (self.size[0]/2,self.size[1])) #오른쪽배경이미지 크기

        self.screen.fill((25, 0, 50)) #값 변경해보고 지워봤는데 큰 변화 없음. 없어도 되는 기능인듯?
        self.screen.blit(image1, [0,0]) #왼쪽배경이미지 출력
        self.screen.blit(image2, [self.size[0]/2,0]) #왼쪽배경이미지 출력

        pygame.display.flip() #화면이 계속 업데이트 될 수 있도록 설정

    # 화면 크기 조정 감지 및 비율 고정
    def check_resize(self):
        if (self.size != self.screen.get_size()): #현재 사이즈와 저장된 사이즈 비교 후 다르면 변경
            changed_screen_size = self.screen.get_size() #변경된 사이즈
            ratio_screen_size = (changed_screen_size[0],changed_screen_size[0]*783/720) #y를 x에 비례적으로 계산
            if(ratio_screen_size[0]<320): #최소 x길이 제한
                ratio_screen_size = (494,537)
            if(ratio_screen_size[1]>783): #최대 y길이 제한
                ratio_screen_size = (720,783)
            self.screen = pygame.display.set_mode(ratio_screen_size,
                                                    pygame.RESIZABLE)
            window_size = self.screen.get_size()
            new_w, new_h = 1 * window_size[0], 1 * window_size[1]
            self.resize(new_w, new_h)
            self.size = window_size
            #self._current._widgets_surface = make_surface(0,0)
            print(f'New menu size: {self.get_size()}')

pvp = Pvp()
pvp.background()
'''
    def background(self):
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
'''