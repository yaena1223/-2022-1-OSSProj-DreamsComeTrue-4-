import pygame
import pygame_menu
import sys
import random
from pygame.locals import *
import time
from boss.Boss import Boss
from boss.Bullet import Bullet
from data.Animation import AnimationManager

import random
import time
from collections import OrderedDict
from typing import Sized

import pygame
import pygame_menu
from boss.Boss import Boss
from boss.Bullet import Bullet
from data.Animation import AnimationManager
from data.CharacterDataManager import *
from data.Defs import *
from data.StageDataManager import *
from object.Item import *
from object.Mob import Mob
from pygame_menu.utils import make_surface
from data.Defs import User
from data.database_user import *

import time

class pvp :
    
    def __init__(self,character_data,character1,character2,stage):

        # 1. 게임초기화 
        pygame.init()
        self.stage_cleared = False

        # 2. 게임창 옵션 설정
        infoObject = pygame.display.Info()
        title = "PVP game"
        pygame.display.set_caption(title) # 창의 제목 표시줄 옵션
        self.size = [infoObject.current_w,infoObject.current_h]
        self.screen = pygame.display.set_mode(self.size,pygame.RESIZABLE)
        # 3. 게임 내 필요한 설정
        self.clock = pygame.time.Clock() # 이걸로 FPS설정함

        # 4. 게임에 필요한 객체들을 담을 배열 생성, 변수 초기화, pvp
        self.animation = AnimationManager()
        self.mobList = []
        self.item_list = []
        self.effect_list = []
        self.character_data = character_data
        #self.stage = stage

        self.goal_time = 120 # play 120초
        self.character1 = character1 # player1 character
        self.character2 = character2 # player2 character
        self.score_player1 = 0 # player1 score
        self.score_player2 = 0 # player2 score
        self.life_player1 = 3 # player1 life
        self.life_player2 = 3 # player2 life

        self.startTime = time.time()
        self.mob_gen_rate = 0.01
        #self.mob_image = stage.mob_image
        #self.background_image = stage.background_image
        self.background_image = "Image/catthema/map1.png"
        self.background_music = "./Sound/bgm/bensound-evolution.wav"
        self.k = 0
        self.SB = 0
        self.coin = 0 
        #self.infowindow_image = "Image/catthema/map1.png"

        # 방향키 
        self.direction1 = {None: (0, 0), pygame.K_w: (0, -2), pygame.K_s: (0, 2),
                    pygame.K_a: (-2, 0), pygame.K_d: (2, 0)} #player1

        self.direction2 = {None: (0, 0), pygame.K_UP: (0, -2), pygame.K_DOWN: (0, 2),
                    pygame.K_LEFT: (-2, 0), pygame.K_RIGHT: (2, 0)} #playter2

    def main(self):
        # 메인 이벤트
        pygame.mixer.init()
        pygame.mixer.music.load(self.background_music)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)

        while self.SB==0:
            #fps 제한을 위해 한 loop에 한번 반드시 호출해야합니다.
            self.clock.tick(30)
            
            #화면 흰색으로 채우기
            self.screen.fill(Color.WHITE.value)
            
            # pvp 모드를 위한 배경 분리
            background1 = pygame.image.load(self.background_image)
            background2 = pygame.image.load(self.background_image)
            background1 = pygame.transform.scale(background1, (self.size[0]/2,self.size[1])) #왼쪽
            background2 = pygame.transform.scale(background2, (self.size[0]/2,self.size[1])) #오른쪽
            background1_width = background1.get_width()
            background1_height = background1.get_height()
            background2_width = background2.get_width()
            background2_height = background2.get_height()
            background1_copy = background1.copy()
            background2_copy = background2.copy()

            self.screen.blit(background1,  [0,0]) 
            self.screen.blit(background1, [self.size[0]/2, 0])

            pygame.display.flip()