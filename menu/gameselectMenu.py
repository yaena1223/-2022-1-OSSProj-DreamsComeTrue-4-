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
from data.Defs import *
from menu.StageSelectMenu import *

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
        
        self.buttonlist=[self.map1,self.map2,self.map3,self.level_map1,self.level_map2,self.level_map3]

        self.stage_level = "1"

        self.stage_data = StageDataManager.loadStageData() # 스테이지 데이터
        self.character_data = CharacterDataManager.load() # 캐릭터 데이터
        self.selectedChapter = [list(self.stage_data["chapter"].keys())[0]] 
        self.selectedStage = ["1"]

    def show(self,screen): 
        # 버튼 그리기
        for button in enumerate(self.buttonlist):
            button[1].draw(screen,(0,0,0))

        for event in pygame.event.get():

            pos = pygame.mouse.get_pos() # mouse

            if event.type == pygame.QUIT:
                pygame.quit()
                break

            if event.type == pygame.MOUSEMOTION: # 마우스모션

                if self.map1.isOver(pos): # 이미지 바꿈
                    self.map1.image="Image/catthema/map1_dark.png"
                    self.map1.draw(screen,(0,0,0))
                pygame.display.update()

                if self.map2.isOver(pos):
                    self.map2.image="Image/catthema/map2_dark.png"
                    self.map2.draw(screen,(0,0,0))
                pygame.display.update()

                if self.map3.isOver(pos):
                    self.map3.image="Image/catthema/map3_dark.png"
                    self.map3.draw(screen,(0,0,0))
                pygame.display.update()

                if self.level_map1.isOver(pos):
                    print("")
                pygame.display.update()

                if self.level_map2.isOver(pos):
                    self.level_map2.draw(screen,(0,0,0))
                pygame.display.update()

                if self.level_map3.isOver(pos):
                    self.level_map3.draw(screen,(0,0,0))
                pygame.display.update()


            if event.type == pygame.MOUSEBUTTONDOWN: # 마우스 클릭

                if self.map1.isOver(pos):
                    self.stage_map=Stage(self.stage_data["chapter"]["Dongguk university"][self.stage_level])
                    StageGame(self.character_data,self.character_data[0],self.stage_map).main()
                pygame.display.update()

                if self.stage_level == "1":
                    if self.level_map1.isOver(pos):
                        self.level_map1.image= "Image/catthema/level2.png"
                        self.level_map1.draw(screen,(0,0,0))
                        self.stage_level = "2" # 바뀐 레벨로 저장.
                        self.selectedStage = ["2"]
                    pygame.display.update()

                # if self.level_map1.isOver(pos): # 레벨 바꿈
                #     if self.stage_level == "1" :
                #         self.level_map1.image= "Image/catthema/level2.png"
                #         self.level_map1.draw(screen,(0,0,0))
                #         self.stage_level = "2" # 바뀐 레벨로 저장.
                #         self.selectedStage = ["2"]
                #     pygame.display.update()

                #     if self.stage_level == "2" :
                #         self.level_map1.image= "Image/catthema/level3.png"
                #         self.level_map1.draw(screen,(0,0,0))
                #         self.stage_level = "3"
                #         self.selectedStage = ["3"]
                #     pygame.display.update()

                #     if self.stage_level == "3" :
                #         self.level_map1.image= "Image/catthema/level1.png"
                #         self.level_map1.draw(screen,(0,0,0))
                #         self.stage_level = "1"
                #         self.selectedStage = ["1"]
                #     pygame.display.update()






        
        