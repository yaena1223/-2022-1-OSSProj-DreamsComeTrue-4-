from button import *
import pygame
import pygame_menu
from data.CharacterDataManager import *
from data.Stage import Stage
from data.StageDataManager import *
from game.StageGame import StageGame
from pygame_menu.utils import make_surface
from menu.CharacterSelectMenu import *
from pygame.locals import *
from data.Rank import Rank
from data.Defs import *
from menu.StageSelectMenu import *
from menu.LeaderBoardMenu import *
from menu.Mypage2 import *


class gameselectMenu:
    def __init__(self,screen):
        
        self.size = screen.get_size()
        self.screen = screen
        changed_screen_size = screen.get_size()
        self.board_width=changed_screen_size[0] # x
        self.board_height=changed_screen_size[1] # y

        self.map1 = button(self.board_width, self.board_height, 0.2, 0.3, 0.2, 0.2, "Image/catthema/map1.png")
        self.map2 = button(self.board_width, self.board_height, 0.5, 0.3, 0.2, 0.2, "Image/catthema/map2.png")
        self.map3 = button(self.board_width, self.board_height, 0.8, 0.3, 0.2, 0.2, "Image/catthema/map3.png")

        self.level_map1 = button(self.board_width, self.board_height, 0.2, 0.5, 0.2, 0.05, "Image/catthema/level1.png")
        self.level_map2 = button(self.board_width, self.board_height, 0.5, 0.5, 0.2, 0.05, "Image/catthema/level1.png")
        self.level_map3 = button(self.board_width, self.board_height, 0.8, 0.5, 0.2, 0.05, "Image/catthema/level1.png")
        
        self.rankpage = button(self.board_height,self.board_height,0.8,0.1,0.1,0.05,"Image/catthema/RANK.png")
        self.mypage = button(self.board_height,self.board_height,0.5,0.1,0.1,0.05,"Image/catthema/MYPAGE.png")
        self.gamemode = button(self.board_height,self.board_height,0.3,0.1,0.1,0.05,"Image/catthema/STAGE.png")
        self.store = button(self.board_height,self.board_height,0.1,0.1,0.1,0.05,"Image/catthema/STORE.png")

        self.buttonlist=[self.map1,self.map2,self.map3,self.level_map1,self.level_map2,self.level_map3,
        self.rankpage,self.mypage,self.gamemode,self.store]

        self.stage_level_map1 = "1"
        self.stage_level_map2 = "1"
        self.stage_level_map3 = "1"

        self.temp1 = self.level_map1.image
        self.temp2 = self.level_map2.image
        self.temp3 = self.level_map3.image

        self.stage_data = StageDataManager.loadStageData() # 스테이지 데이터
        self.character_data = CharacterDataManager.load() # 캐릭터 데이터
        self.selectedChapter = [list(self.stage_data["chapter"].keys())[0]] 

        self.stay=0

    def show(self,screen):        

        screen.fill((255, 255, 255)) # 배경 나중에 바꾸기.

        for self.button in enumerate(self.buttonlist): # 버튼 그리기
            self.button[1].draw(screen,(0,0,0))

        for event in pygame.event.get():

            pos = pygame.mouse.get_pos() # mouse

            if event.type == pygame.QUIT:
                pygame.quit()
                break

            if event.type == pygame.MOUSEMOTION: # 마우스모션

                if self.map1.isOver(pos): # 이미지 바꿈
                    self.map1.image="Image/catthema/map1_dark.png"
                else : self.map1.image="Image/catthema/map1.png" 
                pygame.display.update()

                if self.map2.isOver(pos):
                    self.map2.image="Image/catthema/map2_dark.png"
                else : self.map2.image="Image/catthema/map2.png" 
                pygame.display.update()

                if self.map3.isOver(pos):
                    self.map3.image="Image/catthema/map3_dark.png"
                else : self.map3.image="Image/catthema/map3.png" 
                pygame.display.update()
                
                if self.level_map1.isOver(pos):
                    if self.stage_level_map1 == "1":
                        self.level_map1.image="Image/catthema/level2.png"
                    elif self.stage_level_map1 == "2":
                        self.level_map1.image="Image/catthema/level3.png"
                    elif self.stage_level_map1 == "3":
                        self.level_map1.image="Image/catthema/level1.png"
                else : self.level_map1.image=self.temp1
                pygame.display.update()

                if self.level_map2.isOver(pos):
                    if self.stage_level_map2 == "1":
                        self.level_map2.image="Image/catthema/level2.png"
                    elif self.stage_level_map2 == "2":
                        self.level_map2.image="Image/catthema/level3.png"
                    elif self.stage_level_map2 == "3":
                        self.level_map2.image="Image/catthema/level1.png"
                else : self.level_map2.image=self.temp2
                pygame.display.update()

                if self.level_map3.isOver(pos):
                    if self.stage_level_map3 == "1":
                        self.level_map3.image="Image/catthema/level2.png"
                    elif self.stage_level_map3 == "2":
                        self.level_map3.image="Image/catthema/level3.png"
                    elif self.stage_level_map3 == "3":
                        self.level_map3.image="Image/catthema/level1.png"
                else : self.level_map3.image=self.temp3
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONUP: # 마우스 클릭

                if self.map1.isOver(pos): # 맵 선택하면 게임이랑 연결시키기
                    self.stage_map=Stage(self.stage_data["chapter"]["Dongguk university"][self.stage_level_map1])
                    StageGame(self.character_data,self.character_data[0],self.stage_map).main()
                pygame.display.update()

                if self.map2.isOver(pos): # 맵 선택하면 게임이랑 연결시키기
                    self.stage_map=Stage(self.stage_data["chapter"]["Night view"][self.stage_level_map2])
                    StageGame(self.character_data,self.character_data[0],self.stage_map).main()
                pygame.display.update()

                if self.map3.isOver(pos): # 맵 선택하면 게임이랑 연결시키기
                    self.stage_map=Stage(self.stage_data["chapter"]["Namsan"][self.stage_level_map3])
                    StageGame(self.character_data,self.character_data[0],self.stage_map).main()
                pygame.display.update()

                if self.level_map1.isOver(pos):
                    if self.stage_level_map1 == "1" :
                        self.temp1 = "Image/catthema/level2.png" # 이미지 바꾸기
                        self.stage_level_map1 = "2" # 바뀐 레벨로 저장.
                    
                    elif self.stage_level_map1 == "2" :
                        self.temp1 = "Image/catthema/level3.png" # 이미지 바꾸기
                        self.stage_level_map1 = "3" # 바뀐 레벨로 저장.
                    
                    elif self.stage_level_map1 == "3" :
                        self.temp1 = "Image/catthema/level1.png" # 이미지 바꾸기
                        self.stage_level_map1 = "1" # 바뀐 레벨로 저장.
                pygame.display.update()

                if self.level_map2.isOver(pos):
                    if self.stage_level_map2 == "1" :
                        self.temp2 = "Image/catthema/level2.png" # 이미지 바꾸기
                        self.stage_level_map2 = "2" # 바뀐 레벨로 저장.
            
                    elif self.stage_level_map2 == "2" :
                        self.temp2 = "Image/catthema/level3.png" # 이미지 바꾸기
                        self.stage_level_map2 = "3" # 바뀐 레벨로 저장.
                
                    elif self.stage_level_map2 == "3" :
                        self.temp2 = "Image/catthema/level1.png" # 이미지 바꾸기
                        self.stage_level_map2 = "1" # 바뀐 레벨로 저장.
                pygame.display.update()

                if self.level_map3.isOver(pos):
                    if self.stage_level_map3 == "1" :
                        self.temp3 = "Image/catthema/level2.png" # 이미지 바꾸기
                        self.stage_level_map3 = "2" # 바뀐 레벨로 저장.

                    elif self.stage_level_map3 == "2" :
                        self.temp3 = "Image/catthema/level3.png" # 이미지 바꾸기
                        self.stage_level_map3 = "3" # 바뀐 레벨로 저장.

                    elif self.stage_level_map3 == "3" :
                        self.temp3 = "Image/catthema/level1.png" # 이미지 바꾸기
                        self.stage_level_map3 = "1" # 바뀐 레벨로 저장.

                pygame.display.update()

                if self.mypage.isOver(pos):
                    Mypage(self.screen).show()

                if self.rankpage.isOver(pos):
                    LeaderBoardMenu(self.screen).rank()

                
                    
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
            self.menu.get_current().resize(new_w,new_h)
            self.size = window_size
            print(f'New menu size: {self.menu.get_size()}')
            self.menu._current._widgets_surface = make_surface(0,0)

