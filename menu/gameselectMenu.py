from button import *
import pygame
import pygame_menu
from menu.CharacterSelectMenu import *
import pygame
import pygame_menu
from data.CharacterDataManager import *
from data.Stage import Stage
from data.StageDataManager import *
from game.StageGame import StageGame
from pygame_menu.utils import make_surface
from menu.CharacterSelectMenu import *

class gameselectMenu:

    def __init__(self,screen):
        
        self.size = screen.get_size()
        self.screen = screen
       
        self.board_width=changed_screen_size[0]
        self.board_height=changed_screen_size[1]  

        self.map1 = button(board_width, board_height, 0.2, 0.3, 0.2, 0.2, "Image/catthema/map1.png")
        self.map2 = button(board_width, board_height, 0.5, 0.3, 0.2, 0.2, "Image/catthema/map2.png")
        self.map3 = button(board_width, board_height, 0.8, 0.3, 0.2, 0.2, "Image/catthema/map3.png")

        self.level_map1 = button(board_width, board_height, 0.2, 0.5, 0.2, 0.05, "Image/catthema/level1.png")
        self.level_map2 = button(board_width, board_height, 0.5, 0.5, 0.2, 0.05, "Image/catthema/level1.png")
        self.level_map3 = button(board_width, board_height, 0.8, 0.5, 0.2, 0.05, "Image/catthema/level1.png")
        
        self.buttonlist=[self.map1,self.map2,self.map3,self.level_map1,self.level_map2,self.level_map3]

        self.stage_level = 1

        self.stage_data = StageDataManager.loadStageData()
        self.selectedChapter = [list(self.stage_data["chapter"].keys())[0]]
        self.selectedStage = ["1"]
    
    #Selector 위젯에는 아이템을 튜플 형태로 넣어줘야하므로 변환 함수
    def toTuple(self,str):
        return (str,str)

    def start_stage_game(self):
        # 현재 selector가 선택하고 있는 항목을 get_value로 가져오고, 그것의 키를 [0][0]을 통해 가져온다.
        selected_chapter = self.chapterSelector.get_value()[0][0]
        selected_stage = self.stageSelector.get_value()[0][0]

    def show(self,screen):
        # 버튼 draw
        for button in enumerate(self.buttonlist):
            button[1].draw(screen,(0,0,0))

        pos = pygame.mouse.get_pos() # mouse

        if event.type == pygame.MOUSEMOTION:

            if self.map1.isOver(pos):
                self.map1.image="Image/catthema/map1_dark.png"
                self.map1.draw(screen(0,0,0))
            pygame.display.update()

            if self.map2.isOver(pos):
                self.map2.image="Image/catthema/map2_dark.png"
                self.map2.draw(screen(0,0,0))
            pygame.display.update()

            if self.map3.isOver(pos):
                self.map3.image="Image/catthema/map3_dark.png"
                self.map3.draw(screen(0,0,0))
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if self.level_map1.isOver(pos):
                if self.stage_level == 1 :
                    self.level_map1.image= "Image/catthema/level2.png"
                    self.stage_level = 2
                    self.selectedStage = ["2"]
                pygame.display.update()

                if self.stage_level == 2 :
                    self.level_map1.image= "Image/catthema/level3.png"
                    self.stage_level = 3
                    self.selectedStage = ["3"]
                pygame.display.update()

                if self.stage_level == 3 :
                    self.level_map1.image= "Image/catthema/level1.png"
                    self.stage_level = 1
                    self.selectedStage = ["1"]
                pygame.display.update()






        
        