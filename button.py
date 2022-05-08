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
size = [int(infoObject.current_w*Display.w_init),int(infoObject.current_h*Display.h_init)] #사이즈 설정(w,h) 
screen = pygame.display.set_mode(size,pygame.RESIZABLE) #창크기 조정 가능 
ww, wh= pygame.display.get_surface().get_size() 
Default.game.value["size"]["x"] = size[0] #Default는 Defs.py에 선언되어 있는 클래스명
Default.game.value["size"]["y"] = size[1]


image1 = pygame.image.load("Image/Login.png") 
image1 = pygame.transform.scale(image1, (size[0],size[1])) 
screen.blit(image1, [0,0]) 

board_width = 800   # 가로 위치
board_height = 450   # 세로 위치

#                board_width, board_height, x_rate, y_rate, width_rate, height_rate, img=''):
button1 = button(400, board_height, 0.5, 0.9, 0.37, 0.17, "Image/Catus.png")
button2 = button(board_width, board_height, 0.5, 0.9, 0.37, 0.17, "Image/Catus.png")
#                     (screen, self.image, self.x, self.y, self.width, self.height)

button1.draw(screen, (0, 0, 0))
button2.draw(screen, (0, 0, 0))

pygame.display.update() # 0506 버튼 원하는 위치 설정, 근데 화면 바로 꺼짐.