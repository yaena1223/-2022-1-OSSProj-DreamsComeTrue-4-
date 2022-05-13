
import webbrowser
from sys import argv

import pygame
import pygame_menu
from data.Defs import *
from data.Rank import *
from pygame_menu.locals import ALIGN_CENTER
from pygame_menu.utils import make_surface
from pygame_menu.widgets.core.widget import Widget
from Login import *
from menu.LeaderBoardScrollMenu import *

class Mypage:
    def __init__(self,screen):
        self.size = screen.get_size()
        self.screen = screen
        self.mytheme = pygame_menu.Theme(
                widget_font = pygame_menu.font.FONT_BEBAS,
                widget_background_color = (150, 213, 252), #버튼 가독성 올리기 위해서 버튼 배경색 설정 : 하늘색
                title_font = pygame_menu.font.FONT_BEBAS,
                selection_color = (0,0,0), #선택됐을때 글씨색 설정
                widget_font_color = (255,255,255), #글씨색 설정
                title_background_color = (0,100,162),
                title_font_color = (255,255,255),
                title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL,
            )

        self.menu = pygame_menu.Menu('Mypage', self.size[0], self.size[1],
                            theme=self.mytheme)


        self.mytheme.widget_font_size = self.size[0] * 30//720

    def to_menu(self):
        self.menu.disable()

    # 화면 표시
    def show(self):
        self.menu.clear()
        self.menu.add.vertical_margin(40)
        self.menu.add.label(User.user_id)
        self.menu.add.button("back", self.to_menu)
        self.menu.mainloop(self.screen,bgfun = self.check_resize)

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
            self.menu.resize(new_w, new_h)
            self.menu._current._widgets_surface = make_surface(0,0)
            self.size = window_size
            print(f'New menu size: {self.menu.get_size()}')
            font_size = new_w * 30 //720
            self.mytheme.widget_font_size = font_size    
   

    def to_menu(self):
        self.menu.disable()
