

import pygame
import pygame_menu
from data.CharacterDataManager import *
from data.Defs import *
from data.Stage import Stage
from data.StageDataManager import *
from data.database_user import Database
from game.InfiniteGame import *
from pygame_menu.locals import ALIGN_RIGHT
from pygame_menu.utils import make_surface

# 캐릭터 선택 메뉴
class CharacterStoreMenu:
    image_widget: 'pygame_menu.widgets.Image'
    item_description_widget: 'pygame_menu.widgets.Label'

    def __init__(self,screen):
        # 화면 받고 화면 크기 값 받기
        self.screen = screen
        self.size = screen.get_size()

        #menu_image = pygame_menu.baseimage.BaseImage(image_path='./Image/Login.png',drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
        self.mytheme = pygame_menu.themes.THEME_ORANGE.copy()
        #mytheme.widget_font = pygame_menu.font.FONT_8BIT
        #mytheme.widget_background_color = (150, 213, 252) #버튼 가독성 올리기 위해서 버튼 배경색 설정 : 하늘색
        self.mytheme.title_font = pygame_menu.font.FONT_BEBAS
        self.mytheme.selection_color = (255,255,255) #선택됐을때 글씨색 설정
        self.mytheme.widget_font_color = (255,255,255) #글씨색 설정
        self.mytheme.title_background_color = (0,100,162)
        self.mytheme.title_font_color = (255,255,255)
        self.mytheme.widget_font = pygame_menu.font.FONT_BEBAS
        #self.mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL
        self.mytheme.background_color = (0,0,0)

        self.menu = pygame_menu.Menu('Select Character...', self.size[0], self.size[1],
                            theme=self.mytheme)


        #캐릭터 데이터를 json에서 불러온다
        self.character_data = CharacterDataManager.load()

        self.show()
        self.menu.mainloop(self.screen,bgfun = self.check_resize)

    def to_menu(self):
        self.menu.disable()

    #메뉴 구성하고 보이기
    def show(self):  
        #캐릭터 선택 메뉴 구성
        characters = []
        front_image_path = [Images.cat1.value,Images.cat2.value, Images.cat3.value, Images.cat4.value]
        for idx in range(len(self.character_data)):
            characters.append((self.character_data[idx].name, idx))
        self.character_imgs = []
        for idx in range(len(front_image_path)):       
            default_image = pygame_menu.BaseImage(
                image_path=front_image_path[idx]
            ).scale(0.5, 0.5)
            self.character_imgs.append(default_image.copy())
        
        self.character_selector = self.menu.add.selector(
            title='Character :\t',
            items=characters,
            onchange=self.on_selector_change
        )
        self.image_widget = self.menu.add.image(
            image_path=self.character_imgs[0],
            padding=(25, 0, 0, 0)  # top, right, bottom, left
        )
        self.item_description_widget = self.menu.add.label(title = "Unlocked" if self.character_data[0].is_unlocked == True else "Locked")
        self.frame_v = self.menu.add.frame_v(350, 160, margin=(10, 0))
        # 각 캐릭터의 능력치 표시
        self.power = self.frame_v.pack(self.menu.add.progress_bar(
            title="Power",
            default=int((self.character_data[0].missile_power/Default.character.value["max_stats"]["power"])*100),
            progress_text_enabled = False,
            box_progress_color = Color.RED.value
        ), ALIGN_RIGHT)
        self.fire_rate = self.frame_v.pack(self.menu.add.progress_bar(
            title="Fire Rate",
            default=int((Default.character.value["max_stats"]["fire_rate"]/self.character_data[0].org_fire_interval)*100),
            progress_text_enabled = False,
            box_progress_color =Color.BLUE.value
        ), ALIGN_RIGHT)
        self.velocity = self.frame_v.pack(self.menu.add.progress_bar(
            title="Mobility",
            default=int((self.character_data[0].org_velocity/Default.character.value["max_stats"]["mobility"])*100),
            progress_text_enabled = False,
            box_progress_color = Color.GREEN.value
        ), ALIGN_RIGHT)
        self.mytheme.widget_background_color = (150, 213, 252)
        self.menu.add.button("SELECT",self.select_character)
        self.menu.add.vertical_margin(10)
        self.menu.add.button("    BACK    ",self.to_menu)
        self.update_from_selection(int(self.character_selector.get_value()[0][1]))
        self.mytheme.widget_background_color = (0,0,0,0)

    def select_character(self): #게임 시작 함수

        # 캐릭터 셀릭터가 선택하고 있는 데이터를 get_value 로 가져와서, 그 중 Character 객체를 [0][1]로 접근하여 할당
        selected_idx = self.character_selector.get_value()[0][1]

        #캐릭터가 열려있는지 확인
        if (self.character_data[selected_idx].is_unlocked): #캐릭터가 열려있다면
            User.character = selected_idx
            #print(User.character)
            database = Database()
            database.set_char()

            
            
            

            
        else:
            print("character locked")
            print(self.character_data[selected_idx].name)
            self.showCharactereLockedScreen(self.character_data[selected_idx].name)
            #print(User.character)

            



    # 잠긴 캐릭터 선택 시 보여지는 화면
    def showCharactereLockedScreen(self, character):       
        self.menu.clear()
        if(character == 'cat2'):
            self.menu.add.image(Images.F5S1_locked.value)
        elif(character == 'cat3'):
            self.menu.add.image(Images.F5S4_locked.value)
        elif(character == 'cat4'):
            self.menu.add.image(Images.Tank_locked.value)

        self.menu.add.label("")
        #self.mytheme.widget_background_color = (150, 213, 252)
        self.menu.add.button('back', self.back_from_locked)
        self.menu.mainloop(self.screen,bgfun = self.check_resize)

    def back_from_locked(self):
        self.menu.disable()
        self.__init__(self.screen)



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
            self.size = window_size
            self.menu._current._widgets_surface = make_surface(0,0)
            print(f'New menu size: {self.menu.get_size()}')

    # 캐릭터 변경 시 실행
    def on_selector_change(self, selected, value: int) -> None:
        self.update_from_selection(value)

    # 캐릭터 선택 시 캐릭터 이미지 및 능력치 위젯 업데이트
    def update_from_selection(self, selected_value, **kwargs) -> None:
        self.current = selected_value
        self.image_widget.set_image(self.character_imgs[selected_value])
        self.power.set_value(int((self.character_data[selected_value].missile_power/Default.character.value["max_stats"]["power"])*100))
        self.fire_rate.set_value(int((Default.character.value["max_stats"]["fire_rate"]/self.character_data[selected_value].org_fire_interval)*100))
        self.velocity.set_value(int((self.character_data[selected_value].org_velocity/Default.character.value["max_stats"]["mobility"])*100))
        self.item_description_widget.set_title(title = "Unlocked" if self.character_data[selected_value].is_unlocked == True else "Locked")
