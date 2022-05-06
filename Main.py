from collections import OrderedDict
from datetime import datetime
from os import system

import pygame
import pygame_menu

from data.CharacterDataManager import *
from data.Defs import *
from data.Rank import Rank
from data.StageDataManager import *
from menu.About import *
from menu.DifficultySelectMenu import *
from menu.HelpMenu import HelpMenu
from menu.LeaderBoardMenu import *
from menu.StageSelectMenu import *
from object.Character import *
from pygame_menu.locals import ALIGN_CENTER, ALIGN_LEFT, ALIGN_RIGHT
from pygame_menu.utils import make_surface
from pygame_menu.widgets.core.widget import Widget



class Main:
    def __init__(self,screen):
        #pygame.init()
        self.size = screen.get_size()
        self.screen = screen
        self.mytheme = pygame_menu.themes.THEME_BLUE.copy()
        self.menu = pygame_menu.Menu('Main', self.size[0], self.size[1],
                            theme=self.mytheme)
        self.menu_image = pygame_menu.baseimage.BaseImage(image_path=Images.start.value,drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
        self.mytheme.background_color = self.menu_image 
        self.background = pygame.image.load(Images.start.value)


       

    # 모드 선택 메뉴
    
    def show(self):
        self.menu.clear()
        self.menu.add.button('Select mode', self.show_mode)
        self.menu.add.vertical_margin(10)
        self.menu.add.button('Help',self.show_help)
        self.menu.add.vertical_margin(10)
        self.menu.add.button('About',self.show_info_menu)
        self.menu.add.vertical_margin(10)
        self.menu.add.button('Rank',self.show_rank)
        self.menu.add.vertical_margin(10)
        self.menu.add.button('Quit',pygame_menu.events.EXIT)
        self.menu.mainloop(self.screen,bgfun = self.check_resize)

    def show_mode(self):
            self.menu.clear()
            self.menu.add.button('Infinite Game',self.show_difficulty_select_menu)
            self.menu.add.button('Stage Game',self.show_stage_select_menu)
            self.menu.add.button('Back', self.back)
            self.menu.add.button('Quit', pygame_menu.events.EXIT)

    # 메인 메뉴로 돌아가기
    def back(self):
        self.menu.clear()
        self.menu.add.button('Select mode', self.show_mode)
        self.menu.add.button('Help',self.show_help)
        self.menu.add.button('About',self.show_info_menu)
        self.menu.add.button('Rank',self.show_rank)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

    # 저자 및 라이선스 정보 확인 화면 보여주기
    def show_info_menu(self):
        About(self.screen).show()

    # 난이도 선택 화면 보여주기
    def show_difficulty_select_menu(self):
        DifficultySelectMenu(self.screen).show()

    # 스테이지 선택 화면 보여주기
    def show_stage_select_menu(self):
        StageSelectMenu(self.screen).show()

    # 리더보드 화면 보여주기
    def show_rank(self):
        LeaderBoardMenu(self.screen).rank()

    # 도움말 화면 보여주기
    def show_help(self):
        HelpMenu(self.screen).show()

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


