from datetime import datetime

import pygame
import pygame_menu
import pymysql

# 데이터 베이스 관련 함수 집합
class Rank():
    # 객체 생성 시 데이터 베이스와 연결
    def __init__(self):     
        self.score_db = pymysql.connect(
            user = 'admin',
            passwd = 'the-journey',
            host = 'the-journey-db.cvfqry6l19ls.ap-northeast-2.rds.amazonaws.com',
            db = 'sys',
            charset = 'utf8'
        )

    # 데이터 베이스에서 데이터 불러오기
    # term : 기간 (current)    mode : 난이도 (easy, hard)
    def load_data(self, term, mode):    
        curs = self.score_db.cursor(pymysql.cursors.DictCursor)
        if term == 'current':
            if mode == 'easy':
                sql = 'select * from current_easy_score order by score desc'
            elif mode == 'hard':
                sql = 'select * from current_hard_score order by score desc'

      
        curs.execute(sql)
        data = curs.fetchall()
        curs.close()
        return data

    # 현재 가장 최근에 기록된 랭킹 데이터의 날짜 받아오기 -> 랭킹 갱신 판단 여부를 위해 필요한 함수
    def load_current_latest_data(self, mode):
        curs = self.score_db.cursor(pymysql.cursors.DictCursor)
        if mode == 'easy':
            sql = 'select * from current_easy_score order by date desc'
        elif mode == 'hard':
            sql = 'select * from current_hard_score order by date desc'
        curs.execute(sql)
        data = curs.fetchall()
        if(len(data) > 0):
            return str(data[0]['date'])
        # 이번 달 랭킹에 기록 된 데이터가 없으면 'no_current_data' 리턴
        else:
            return str('no_current_data')

    # 랭킹 검색하기
    # term : 기간 (current)    mode : 난이도 (easy, hard)     ID : 검색할 아이디
    def search_data(self, term, mode, ID):                                  
        if term == 'current':
            if mode == 'easy':
                data = self.load_data('current', 'easy')
            elif mode == 'hard':
                data = self.load_data('current', 'hard')


        for i in range(len(data)):
            if data[i]['ID'] == ID:
                return i+1
        # 일치하는 ID가 없으면 0 리턴
        return 0

    # 데이터 베이스에서 데이터 추가하기
    # term : 기간 (current)    mode : 난이도 (easy, hard)     ID : 입력받은 ID       score : 기록된 점수
    def add_data(self, term, mode, ID, score):                                   
        curs = self.score_db.cursor()
        now = datetime.now()
        if term == 'current':
            if mode == 'easy':
                sql = 'INSERT INTO current_easy_score (ID, score, date) VALUES (%s, %s, %s)'

            if mode == 'hard':
                sql = 'INSERT INTO current_hard_score (ID, score, date) VALUES (%s, %s, %s)'

        
        # 데이터 추가 시 자동적으로 현재 날짜가 같이 저장됨
        curs.execute(sql, (ID, score, now.strftime('%Y-%m-%d')))
        self.score_db.commit()
        curs.close()


    # ID 중복 체크하기    
    # mode : 난이도 (easy, hard)     ID : 검색할 ID
    def check_ID(self, mode, ID):
        curs = self.score_db.cursor()
        if mode == 'easy':
            sql = 'select * from current_easy_score where ID = binary(%s)'
        if mode == 'hard':
            sql = 'select * from current_hard_score where ID = binary(%s)'
        curs.execute(sql, (ID))
        data = curs.fetchall()
        curs.close()
        if(len(data)>0): return 0   # 중복임
        else: return 1              # 중복아님


    # 랭킹 갱신 여부 판단
    # 가장 최근에 기록된 랭킹의 날짜 데이터 받아와서 현재 날짜와 비교
    # 'no_current_data'일 경우 갱신 스킵
    def check_update(self):
        date_easy = self.load_current_latest_data('easy')
        date_hard = self.load_current_latest_data('hard')
        if(date_easy == 'no_current_data' and date_hard == 'no_current_data'):
            return
        else:
            if(date_easy == 'no_current_data'): date = date_hard
            elif(date_hard == 'no_current_data'): date = date_easy
            else: date = date_easy

            if(date[0:4] < datetime.now().strftime('%Y')): # Year 비교
                self.update_data()
            elif(date[5:7] < datetime.now().strftime('%m')): # month 비교
                self.update_data()
            else: return

            



