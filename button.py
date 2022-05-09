import pygame
import pygame_menu
from pygame.locals import *
from data.Defs import *

class button():   # 버튼 class
   
    def __init__(self, board_width, board_height, x_rate, y_rate, width_rate, height_rate, img=''):   # 버튼 생성
        self.x = board_width * x_rate   # 버튼 x 좌표
        self.y = board_height * y_rate   # 버튼 y 좌표
        self.width = int(board_width * width_rate)   # 버튼의 너비
        self.height = int(board_height * height_rate)   # 버튼의 높이
        self.x_rate = x_rate   
        self.y_rate = y_rate
        self.width_rate = width_rate
        self.height_rate = height_rate
        # self.id = id
        self.image = img

    def change(self, board_width, board_height):   # 버튼 위치, 크기 바꾸기
        self.x = board_width * self.x_rate   # x 좌표
        self.y = board_height * self.y_rate   # y 좌표
        self.width = int(board_width * self.width_rate)   # 너비
        self.height = int(board_height * self.height_rate)   # 높이

    def draw(self, win, outline=None):   # 버튼 보이게 만들기 
        if outline:
            draw_image(screen, self.image, self.x, self.y, self.width, self.height)
            
    def isOver(self, pos):   # 마우스의 위치에 따라 버튼 누르기 -> pos[0]: 마우스의 x 좌표 / pos[1]: 마우스의 y 좌표
        if pos[0] > self.x - (self.width / 2) and pos[0] < self.x + (self.width / 2):   # 좌측 화면/우측 화면 넘어가기 전, 
            if pos[1] > self.y - (self.height / 2) and pos[1] < self.y + (self.height / 2):   # 상/하단 화면 넘어가기 전, 
                return True
        return False

    def isOver_2(self, pos):
        #start 화면에서 single,pvp,help,setting을 위해서 y좌표 좁게 인식하도록
        if pos[0] > self.x - (self.width / 2) and pos[0] < self.x + (self.width / 2):
            if pos[1] > self.y - (self.height / 4) and pos[1] < self.y + (self.height / 4):#243줄에서의 2을 4로 바꿔주면서 좁게 인식할수 있도록함. 더 좁게 인식하고 싶으면 숫자 늘려주기#
                return True
        return False

def draw_image(window, img_path, x, y, width, height):
    x = x - (width / 2)   # 이미지 그리는 위치: 좌측 상단 기준 -> 2로 나누기 
    y = y - (height / 2)
    image = pygame.image.load(img_path)
    image = pygame.transform.smoothscale(image, (width, height))
    window.blit(image, (x, y))

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
size = [int(infoObject.current_w*Display.w_init),int(infoObject.current_h*Display.h_init)]
screen = pygame.display.set_mode(size,pygame.RESIZABLE)
ww, wh= pygame.display.get_surface().get_size()
Default.game.value["size"]["x"] = size[0]
Default.game.value["size"]["y"] = size[1]

board_width = 800   # 가로 위치
board_height = 450   # 세로 위치

# 버튼 확인
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

        
        #방향키 설정
        direction = {None: (0, 0), pygame.K_w: (0, -2), pygame.K_s: (0, 2),
                    pygame.K_a: (-2, 0), pygame.K_d: (2, 0)}

        direction2 = {None: (0, 0), pygame.K_UP: (0, -2), pygame.K_DOWN: (0, 2),
                    pygame.K_LEFT: (-2, 0), pygame.K_RIGHT: (2, 0)}


        # 화면에 그리기
        image1 = pygame.image.load("Image/Login.png") 
        image1 = pygame.transform.scale(image1, (size[0],size[1])) 
        screen.blit(image1, [0,0]) 

        #                board_width, board_height, x_rate, y_rate, width_rate, height_rate, img=''):
        button1 = button(100, 300, 1, 1, 1.5, 1, "Image/catthema/map1.png")
        button2 = button(100, 300, 3, 1, 1.5, 1, "Image/catthema/map2.png")
        button3 = button(100, 300, 5, 1, 1.5, 1, "Image/catthema/map3.png")
        #                     (screen, self.image, self.x, self.y, self.width, self.height)

        # 화면 비율에 맞춰서 크기 바뀌도록 수정해야함.0509
        button1.draw(screen, (0, 0, 0))
        button2.draw(screen, (0, 0, 0))
        button3.draw(screen, (0, 0, 0))
        pos = pygame.mouse.get_pos()
        button1.isOver(pos)

        pygame.display.flip()