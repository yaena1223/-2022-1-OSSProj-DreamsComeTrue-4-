from button import *
import pygame
import pygame_menu
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

        self.level1_map1 = button(board_width, board_height, 0.2, 0.5, 0.1, 0.1, "Image/Catus1.png")
        self.level2_map1 = button(board_width, board_height, 0.2, 0.5, 0.1, 0.1, "Image/Catus1.png")
        self.level3_map1 = button(board_width, board_height, 0.2, 0.5, 0.1, 0.1, "Image/Catus1.png")

        self.level1_map2 = button(board_width, board_height, 0.5, 0.5, 0.1, 0.1, "Image/Catus1.png")
        self.level2_map2 = button(board_width, board_height, 0.5, 0.5, 0.1, 0.1, "Image/Catus1.png")
        self.level3_map2 = button(board_width, board_height, 0.5, 0.5, 0.1, 0.1, "Image/Catus1.png")

        self.level1_map3 = button(board_width, board_height, 0.8, 0.5, 0.1, 0.1, "Image/Catus1.png")
        self.level2_map3 = button(board_width, board_height, 0.8, 0.5, 0.1, 0.1, "Image/Catus1.png")
        self.level3_map3 = button(board_width, board_height, 0.8, 0.5, 0.1, 0.1, "Image/Catus1.png")

        self.buttonlist=[button1,button2,button3,level1_map1,level2_map1,level3_map1,level1_map2,level2_map2,
        level3_map2,level1_map3,level2_map3,level3_map3]

        self.stage_level = 1

    def show(self,screen):
        # 버튼 draw
        for button in enumerate(self.buttonlist):
            button[1].draw(screen,(0,0,0))

        pos = pygame.mouse.get_pos() # mouse

        if event.type == pygame.MOUSEMOTION:

            if self.map1.isOver(pos): # map1
                self.map1.image="Image/.png"
                self.map1.draw(screen, (0, 0, 0))
            pygame.display.update()

            if self.map2.isOver(pos): # map2
                self.map2.image="Image/.png"
                self.map2.draw(screen, (0, 0, 0))
            pygame.display.update()

            if self.map3.isOver(pos): # map3
                self.map3.image="Image/.png"
                self.map3.draw(screen, (0, 0, 0))
            pygame.display.update()

            if self.level1_map1.isOver(pos): # level 1일때, 마우스 위치하면 이미지 바뀜.
                self.level1_map1.image="Image/.png"
                self.level1_map1.draw(screen, (0, 0, 0))
            pygame.display.update()

            if self.level2_map1.isOver(pos): # level 2일때, 마우스 위치하면 이미지 바뀜.
                self.level2_map1.image="Image/.png"
                self.level2_map1.draw(screen, (0, 0, 0))
            pygame.display.update()

            if self.level3_map1.isOver(pos): # level 3일때, 마우스 위치하면 이미지 바뀜.
                self.level3_map1.image="Image/.png"
                self.level3_map1.draw(screen, (0, 0, 0))
            pygame.display.update()

            if self.level1_map2.isOver(pos): # level 1일때, 마우스 위치하면 이미지 바뀜.
                self.level1_map2.image="Image/.png"
                self.level1_map2.draw(screen, (0, 0, 0))
            pygame.display.update()

            if self.level2_map2.isOver(pos): # level 2일때, 마우스 위치하면 이미지 바뀜.
                self.level2_map2.image="Image/.png"
                self.level2_map2.draw(screen, (0, 0, 0))
            pygame.display.update()

            if self.level3_map2.isOver(pos): # level 3일때, 마우스 위치하면 이미지 바뀜.
                self.level3_map2.image="Image/.png"
                self.level3_map2.draw(screen, (0, 0, 0))
            pygame.display.update()

            if self.level1_map3.isOver(pos): # level 1일때, 마우스 위치하면 이미지 바뀜.
                self.level1_map3.image="Image/.png"
                self.level1_map3.draw(screen, (0, 0, 0))
            pygame.display.update()

            if self.level2_map3.isOver(pos): # level 2일때, 마우스 위치하면 이미지 바뀜.
                self.level2_map3.image="Image/.png"
                self.level2_map3.draw(screen, (0, 0, 0))
            pygame.display.update()

            if self.level3_map3.isOver(pos): # level 3일때, 마우스 위치하면 이미지 바뀜.
                self.level3_map3.image="Image/.png"
                self.level3_map3.draw(screen, (0, 0, 0))
            pygame.display.update()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if self.map1.isOver(pos):
                self.stage_level
            pygame.display.update()

            if self.map2.isOver(pos):
                self.stage_level
            pygame.display.update()

            if self.map3.isOver(pos):
                self.stage_level
            pygame.display.update()

            if self.level1_map1.isOver(pos):
                self.level1_map1.image="Image/Catus1.png" # 2로
                self.stage_level=2 # stage 변경
            pygame.display.update()

            if self.level2_map1.isOver(pos):
                self.level2_map1.image="Image/Catus1.png" # 2로
                self.stage_level=3 # stage 변경
            pygame.display.update()

            if self.level3_map1.isOver(pos):
                self.level3_map1.image="Image/Catus1.png" # 2로
                self.stage_level=1 # stage 변경
            pygame.display.update()

            if self.level1_map2.isOver(pos):
                self.level1_map2.image="Image/Catus1.png" # 2로
                self.stage_level=2 # stage 변경
            pygame.display.update()

            if self.level2_map2.isOver(pos):
                self.level2_map2.image="Image/Catus1.png" # 2로
                self.stage_level=3 # stage 변경
            pygame.display.update()

            if self.level3_map2.isOver(pos):
                self.level3_map2.image="Image/Catus1.png" # 2로
                self.stage_level=1 # stage 변경
            pygame.display.update()

            if self.level1_map3.isOver(pos):
                self.level1_map3.image="Image/Catus1.png" # 2로
                self.stage_level=2 # stage 변경
            pygame.display.update()

            if self.level2_map3.isOver(pos):
                self.level2_map3.image="Image/Catus1.png" # 2로
                self.stage_level=3 # stage 변경
            pygame.display.update()

            if self.level3_map3.isOver(pos):
                self.level3_map3.image="Image/Catus1.png" # 2로
                self.stage_level=1 # stage 변경
            pygame.display.update()




        
        