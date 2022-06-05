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
#from object.Mob import Mob
from pygame_menu.utils import make_surface
from data.Defs import User
from data.database_user import *

from pygame.math import Vector2 #mob.py에서 가져옴
from object.Effect import Boom

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
        self.enemyBullets =[]
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
        self.mob_velocity = 2
        self.mob_image = "./Image/catthema/attack/cat_att.png"
        #self.background_image = stage.background_image
        self.background_image = "Image/catthema/map1.png"
        self.background_music = "./Sound/bgm/bensound-evolution.wav"
        self.k = 0
        self.SB = 0
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
            


            # 입력 처리
            for event in pygame.event.get(): #동작을 했을때 행동을 받아오게됨
                if event.type ==pygame.QUIT:
                    self.SB=1 # SB 가 1이되면 while 문을 벗어나오게 됨
                if event.type == pygame.KEYDOWN: # 어떤 키를 눌렀을때!(키보드가 눌렸을 때)
                    if event.key == pygame.K_x:
                        self.SB=1
                    if event.key == pygame.K_z: #테스트용
                        self.score += 30
                if event.type == pygame.VIDEORESIZE: #창크기가 변경되었을 때
                    #화면 크기가 최소 300x390은 될 수 있도록, 변경된 크기가 그것보다 작으면 300x390으로 바꿔준다
                    width, height = max(event.w,300), max(event.h,390)

                    #크기를 조절해도 화면의 비율이 유지되도록, 가로와 세로 중 작은 것을 기준으로 종횡비(10:13)으로 계산
                    if(width<=height):
                        height = int(width * (13/10))
                    else:
                        width = int(height * (10/13))
                    
                    self.size =[width,height] #게임의 size 속성 변경
                    self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE) #창 크기 세팅
                    self.check_resize()
                    self.animation.on_resize(self)

            #몹을 확률적으로 발생시키기
            if(random.random()<self.mob_gen_rate):
                newMob = Mob(self.mob_image,{"x":50, "y":50},self.mob_velocity,0)
                newMob.set_XY((random.randrange(0,self.size[0]),0)) #set mob location randomly
                self.mobList.append(newMob)
            
            if random.random() < Default.item.value["powerup"]["spawn_rate"]:
                new_item = PowerUp(self.animation.animations["powerup"])
                new_item.set_XY((random.randrange(0,self.size[0]-new_item.sx),0))
                self.item_list.append(new_item)

            if random.random() < Default.item.value["bomb"]["spawn_rate"]:
                new_item = Bomb(self.animation.animations["bomb"])
                new_item.set_XY((random.randrange(0,self.size[0]-new_item.sx),0))
                self.item_list.append(new_item)

            if random.random() < Default.item.value["health"]["spawn_rate"]:
                new_item = Health(self.animation.animations["health"])
                new_item.set_XY((random.randrange(0,self.size[0]-new_item.sx),0))
                self.item_list.append(new_item)

            if random.random()< Default.item.value["speedup"]["spawn_rate"]:
                new_item = SpeedUp(self.animation.animations["speedup"])
                new_item.set_XY((random.randrange(0,self.size[0]-new_item.sx),0))
                self.item_list.append(new_item)
            
            #몹 객체 이동
            for mob in self.mobList:
                mob.move(self.size,self)

            for item in self.item_list:
                item.move(self)

            for effect in self.effect_list:
                effect.move(self)

            #적 투사체 이동
            for bullet in self.enemyBullets:
                bullet.move(self.size,self)
                bullet.show(self.screen)



            #몹 그리기
            for mob in self.mobList:
                mob.show(self.screen)

            for item in list(self.item_list):
                item.show(self.screen)

           
                        
            #self.character1.update(self)
            #self.character2.update(self)

            pygame.display.flip()

class Mob(Object):
    def __init__(self, img_path, size, velocity, missile):
        super().__init__(img_path, size, velocity)
        self.missile = missile
        self.is_targeted = False
        self.direction = Vector2(1,1)
        self.rad = 1
        self.kill_sfx = pygame.mixer.Sound(Default.effect.value["boom"]["sound"])
        self.kill_sfx.set_volume(Default.sound.value["sfx"]["volume"])

    def move(self, boundary, game):
        if (game.size[0] != self.boundary[0]/2) or (game.size[1] != self.boundary[1]): #update when screen resized
            self.on_resize(game)

        self.x += self.direction.y
        self.y += self.direction.x
        self.rad+=0.04*self.velocity #속도에 적절한 값을 곱하여, 각도 변경
        self.direction.from_polar((self.velocity*3,math.cos(self.rad)*70)) #속도에 비례한 길이를 갖고, 방향 sin함수를 따르는 벡터를 다음 방향으로 지정

        if self.x >= self.boundary[0]/2 - self.sx:
            self.x_inv = True

        if self.y >= boundary[1] - self.sy:
            game.mobList.remove(self)

    def destroy(self, game):
        self.kill_sfx.play()
        boom = Boom(game.animation.animations["destroy_effect"])
        mob_location = {"x":self.x+(self.sx/2), "y":self.y+(self.sy/2)}
        boom.set_XY((mob_location["x"] - boom.sx/2, mob_location["y"]- boom.sy/2))
        game.effect_list.append(boom)
        if self in game.mobList:
            game.mobList.remove(self)

# 아이템 기본 클래스
class Item(Object):
    # 각 아이템은 해당 클래스를 상속 받음
    
    # Attributes :
    # self.x_inv : x축 이동방향의 반전 여부 (bool)
    # self.y_inv : y축 이동방향의 반전 여부 (bool)
    # self.spawned : 아이템 생성된 시간 (float)
    # self.blink_count : 깜빡임 애니메이션 중 다음 프레임까지 지난 시간 (float)
    # self.inc : 다음 애니메이션까지 지난 시간 (float)
    # self.inc_delay : 애니메이션 사이클이 끝나고 다시 반복할 때까지 걸리는 시간 (float)
    # self.sfx : 아이템 획득 효과음 (sound)
    def __init__(self, frames, frames_trans, anim_id):
        super().__init__("", Default.item.value["size"], Default.item.value["velocity"], frames, frames_trans, anim_id)
        self.x_inv = random.choice([True, False])
        self.y_inv = False
        self.spawned = time.time()
        self.blink_count = 0.0
        self.inc = 0.0
        self.inc_delay = 0.0
        self.sfx = pygame.mixer.Sound(Default.item.value["sound"])
        self.sfx.set_volume(Default.sound.value["sfx"]["volume"])

    # 아이템 이동 메소드
    def move(self, game): 
        if (game.size[0] != self.boundary[0]/2) or (game.size[1] != self.boundary[1]):
            self.on_resize(game)
        if self.x_inv == False:
            self.x += self.velocity
        else:
            self.x -= self.velocity
        if self.y_inv == False:
            self.y += self.velocity
        else:
            self.y -= self.velocity
        if self.x <= 0:
            self.x_inv = False
        elif self.y <= 0:
            self.y_inv = False
        elif self.x >= self.boundary[0]/2 - self.sx:
            self.x_inv = True
        elif self.y >= self.boundary[1] - self.sy:
            self.y_inv = True
        # rect 위치 업데이트
        self.update_rect((self.x, self.y))
        # 애니메이션 재생
        self.inc += Default.animation.value["speed"]
        self.inc = Utils.clamp(self.inc, 0.0, self.frame_count-1)
        if self.inc >= self.frame_count-1:
            self.inc_delay += Default.animation.value["speed"]
            if self.inc_delay >= Default.animation.value["interval"]:
                self.inc = 0.0
                self.inc_delay = 0.0
        self.current_frame = int(self.inc)
        if self.is_transparent == False:
            self.img = self.frames[int(self.inc)]
        else:
            self.img = self.frames_trans[int(self.inc)]
        # 아이템 생성 후 일정 시간 경과 시 깜빡이면서 소멸
        time_passed = time.time() - self.spawned
        time_left = Default.item.value["duration"] - time_passed 
        if time_left > 0:
            if time_left <= Default.animation.value["blink"]["duration"]:
                self.blink_count += Default.animation.value["blink"]["speed"]
                if(self.blink_count >= Default.animation.value["blink"]["frame"]):
                    if self.is_transparent == False:
                        self.img = self.frames_trans[int(self.inc)]
                        self.blink_count = 0.0
                        self.is_transparent = True
                    else:
                        self.img = self.frames[int(self.inc)]
                        self.blink_count = 0.0
                        self.is_transparent = False
        else:
            game.item_list.remove(self)

class Bomb(Item):
    # 폭탄 아이템: 획득 시 폭탄 카운터 증가
    def __init__(self, animation):
        super().__init__(animation.frames, animation.frames_trans, "bomb")

    # 캐릭터와 충돌 시  바로 실행
    '''def use(self, game):
        if self.is_collidable == True:
            self.sfx.play()
            game.character.bomb_count+=1
            self.is_collidable = False
            game.item_list.remove(self)'''


class Health(Item):
    # 목숨 아이템: 획득 시 목숨 증가
    def __init__(self, animation):
        super().__init__(animation.frames, animation.frames_trans, "health")

    # 캐릭터와 충돌 시  바로 실행
    def use(self, game):
        if self.is_collidable == True:
            self.sfx.play()
            game.life += 1
            self.is_collidable = False
            game.item_list.remove(self)

class PowerUp(Item):
    # 파워업 아이템: 획득 시 캐릭터 발사체 개수 증가
    def __init__(self, animation):
        super().__init__(animation.frames, animation.frames_trans, "powerup")

    # 캐릭터와 충돌 시  바로 실행
    '''def use(self, game):
        if self.is_collidable == True:
            self.sfx.play()
            fire_count = game.character.fire_count + 1
            n_min = Default.character.value["missile"]["min"]
            n_max = Default.character.value["missile"]["max"]
            if fire_count > n_max:
                game.character.auto_target = True
            game.character.fire_count  = Utils.clamp(fire_count, n_min, n_max)
            self.is_collidable = False
            game.item_list.remove(self)'''

class SpeedUp(Item):
    # 스피드업 아이템: 획득 시 캐릭터 이동/발사 속도 증가
    def __init__(self, animation):
        super().__init__(animation.frames, animation.frames_trans, "speedup")
        
    # 캐릭터와 충돌 시  바로 실행
    '''def use(self, game):
        if self.is_collidable == True:
            self.sfx.play()
            self.used = time.time()
            self.org_velocity = game.character.velocity
            self.org_fire_interval = game.character.fire_interval
            game.character.speed_up()
            self.is_collidable = False
            game.item_list.remove(self)'''