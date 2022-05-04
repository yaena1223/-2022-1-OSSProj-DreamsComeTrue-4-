#드림즈컴츄르 추가 파일
import pymysql
import bcrypt

class Database:
    def __init__(self):     
        self.score_db = pymysql.connect(
        db="sys",
        host="database-2.cskg3bhzvpnw.ap-northeast-2.rds.amazonaws.com",
        port=3306,
        user="admin",
        passwd="dreamscometrue",
        charset = 'utf8'
        )

    def id_not_exists(self,input_id):
        curs = self.score_db.cursor(pymysql.cursors.DictCursor) #Dictionary cursor -> row 결과를 dictionary 형태로 리턴
        sql = "SELECT * FROM users WHERE user_id=%s"
        curs.execute(sql,input_id)  #input_id 데이터를 서버에 전송
        data = curs.fetchone()
        curs.close()
        if data:
            return False
        else:
            return True

    def match_idpw(self, id, pw): #아이디와 비번이 일치하는지 비교
        #input_password = pw.encode('utf-8') #입력번호 비밀번호 인코딩(문자 -> byte값으로)
        curs = self.score_db.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM users WHERE user_id=%s" 
        curs.execute(sql,id) #입력받은 id 서버로 전송
        data = curs.fetchone()  #입력받은 id와 일치하는 행 하나 선택
        curs.close()
        #check_password=bcrypt.checkpw(input_password,data['user_password'].encode('utf-8')) #입력한 비밀번호와 데이터베이스에 저장된 비밀번호 비교
        check_password= False
        if pw == data['user_password']:
            check_password = True
        return check_password

    def add_id(self, user_id): #아이디 추가
        curs = self.score_db.cursor()
        sql = "INSERT INTO users (user_id) VALUES (%s)" #users테이블에서 user_id 필드에 %s의 값을 삽입
        curs.execute(sql, user_id)
        self.score_db.commit()
        curs.close()


    def add_pw(self, user_pw, user_id): #비밀번호 & coin 초기값 추가 * 캐릭터 초기값은 1로(캐릭터 숫자로 표현)
        initial_coin = 0 #가입시, 보유한 coin 0으로 설정
        initial_character = 1
        '''new_pw = user_pw.encode('utf-8') #문자열을 byte값으로
        hashed_pw = bcrypt.hashpw(new_pw, bcrypt.gensalt()) #해싱
        curs = self.score_db.cursor()
        sql = "UPDATE users SET user_password=%s WHERE user_id=%s"
        curs.execute(sql, (hashed_pw, user_id)) #암호화된 비밀번호로 저장
        self.score_db.commit()'''
        curs = self.score_db.cursor()
        sql = "UPDATE users SET user_password=%s WHERE user_id=%s"
        curs.execute(sql,(user_pw, user_id))
        self.score_db.commit()
        curs = self.score_db.cursor()
        sql = "UPDATE users SET user_coin=%s WHERE user_id=%s"
        curs.execute(sql,(initial_coin, user_id)) #코인 초기값 추가
        self.score_db.commit()
        curs = self.score_db.cursor()
        sql = "UPDATE users SET user_character=%s WHERE user_id=%s"
        curs.execute(sql,(initial_character, user_id))
        self.score_db.commit()
        curs.close()


    