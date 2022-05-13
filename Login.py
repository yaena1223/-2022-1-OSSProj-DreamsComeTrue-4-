from collections import OrderedDict
from datetime import datetime
from os import system
from turtle import color
from menu.DifficultySelectMenu import *
import pygame
import pygame_menu
import pymysql
from Main import *
from data.database_user import *
from data.Defs import *
from data.Defs import User
from menu.gameselectMenu import gameselectMenu

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
font_size = 30
class Login:
    id = ''
    password = ''
    database = Database()
    coin = 0
    char = 1
    def __init__(self):
        menu_image = pygame_menu.baseimage.BaseImage(image_path=Images.login.value,drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL) #메뉴 이미지, Images는 Defs.py에 선언되어 있는 클래스명
        self.mytheme = pygame_menu.Theme(
            widget_font = pygame_menu.font.FONT_8BIT,
            widget_background_color = (150, 213, 252), #버튼 가독성 올리기 위해서 버튼 배경색 설정 : 하늘색
            title_font = pygame_menu.font.FONT_BEBAS,
            selection_color = (0,0,0), #선택됐을때 글씨색 설정
            widget_font_color = (255,255,255), #글씨색 설정
            title_background_color = (0,100,162),
            title_font_color = (255,255,255),
            title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL,
            widget_font_size = 30
        )
        self.mytheme.background_color = menu_image
        self.menu = pygame_menu.Menu('DreamsComeTrue', ww,wh,theme=self.mytheme) #상단바 



    def first_page(self): # 첫화면 
        self.menu.clear()
        b1 = self.menu.add.button(' Sign Up ', self.show_signup)
        self.menu.add.vertical_margin(10)
        b2= self.menu.add.button('   Login   ', self.login_page)
        self.menu.add.vertical_margin(10)
        b3 = self.menu.add.button('2 Players', self.pvp_page)
        self.menu.add.vertical_margin(10)
        b4 = self.menu.add.button('    Quit    ', pygame_menu.events.EXIT)

    def login_page(self): ##로그인 페이지
        self.menu.clear()
        #login.mytheme.widget_background_color = (0,0,0,0) #투명 배경
        self.menu.add.text_input('ID : ', maxchar=100, onchange=self.get_id)
        self.menu.add.text_input('PASSWORD : ', maxchar=100, onchange=self.get_pw,password=True, password_char='*')
        b1 = self.menu.add.button('  Login  ', self.login)
        b2 = self.menu.add.button('  Back  ', self.first_page)
        b3 = self.menu.add.button('  Quit  ', pygame_menu.events.EXIT)

        #mytheme.widget_background_color = (150, 213, 252)

    def login(self):
        if self.id:
            if self.database.id_not_exists(self.id) is False:
                if self.password and self.database.match_idpw(self.id, self.password):
                    print("로그인 성공")
                    print(self.id)
                    User.user_id = self.id
                    self.login_success()
                    # 계정의 coin,char 값 가져오기 => 아직 안함. 수정 필요
                    '''coin=self.database.load_exp_data(self.id) #로그인 성공하면 경험치 데이터베이스에서 받아오기
                    char=self.database.load_char_data(self.id)
                    if char==1:
                        Var.lst = Var.char1_lst
                    elif char==2:
                        Var.lst = Var.char2_lst
                    elif char==3:
                        Var.lst = Var.char3_lst
                    Var.user_id = self.id '''
                    
                   

                else:
                    print("비밀번호 틀림")
                    self.password_fail()
                    
            else:
                print("로그인 실패")
                self.login_fail()
                
        else:
            print("이건뭘까")
            self.login_page()

    def password_fail(self):
        self.menu.clear()
        self.menu.add.vertical_margin(10)
        self.menu.add.label("ID or Password Incorrect", selectable=False)
        self.menu.add.vertical_margin(10)
        self.menu.add.button('  back  ', self.login_page)


    def login_fail(self):
        self.menu.clear()
        self.menu.add.vertical_margin(10)
        self.menu.add.label("ID or Password Incorrect", selectable=False)
        self.menu.add.vertical_margin(10)
        self.menu.add.button('  back  ', self.login_page)

    #아이디 input값으로 변경

    def get_id(self,value):
        self.id = value
        

    #비밀번호 입력값으로 변경
    def get_pw(self,value):
        self.password=value

    def save_id(self,value): #아이디 데이터베이스에 저장
        self.id=value
        print("출력:" ,value)
        if self.database.id_not_exists(self.id): #id가 데이터베이수애 존재하지않으면
            self.database.add_id(self.id) #데이터베이스에 저장(회원가입)
        else:
            self.signup_fail()

    def save_password(self,value): #비밀번호 데이터베이스에 저장
        self.password=value
        self.database.add_pw(self.password,self.id)

    def show_signup(self):
        self.menu.clear()
        #mytheme.widget_background_color = (0,0,0,0) #투명 배경
        self.menu.add.text_input('ID : ', maxchar=15, onreturn=self.save_id) #현재의 문제점 : enter를 눌러야만 저장됨.
        self.menu.add.text_input('PASSWORD : ', maxchar=50, onreturn=self.save_password,password=True, password_char='*')
        self.menu.add.button('  Sign Up  ', self.login_page)
        self.menu.add.button('  back  ', self.first_page)
        self.menu.add.button('  Quit   ', pygame_menu.events.EXIT)

    def login_success(self):
        #Main(screen).show()
        game=gameselectMenu(screen)
        if __name__ == '__main__':
            while True:
                game.show(screen)
                pygame.display.flip()


    def signup_fail(self):
        self.menu.clear()
        self.menu.add.vertical_margin(10)
        self.menu.add.label("    ID Already Exists     ", selectable=False)
        self.menu.add.vertical_margin(10)
        self.menu.add.button('  back  ', self.show_signup)

    def pvp_page(self): #2인 플레이어
        self.menu.clear()
        self.menu.add.button('  back  ', self.first_page)

login = Login()
login.first_page()   

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
            font_size = new_w * 30 //720
            #print(font_size)
            login.mytheme.widget_font_size = font_size
            login.menu.resize(new_w, new_h)
            size = window_size
            print(f'New menu size: {login.menu.get_size()}')
            
            
            

             

        # 화면에 메뉴 그리기
        screen.fill((25, 0, 50)) #값 변경해보고 지워봤는데 큰 변화 없음. 없어도 되는 기능인듯?
        
        login.menu.update(events)
        login.menu.draw(screen)
        #pygame.draw.rect(screen,color,input_rect,2)


        pygame.display.flip() #화면이 계속 업데이트 될 수 있도록 설정