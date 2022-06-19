# 2022-1-OSSProj-DreamsComeTrue-4
## Team_DreamsComeTrue💭
![Github license](https://img.shields.io/github/license/CSID-DGU/2022-1-OSSProj-DreamsComeTrue-4)
![badges](https://img.shields.io/badge/OS-ubuntu-red)
![badges](https://img.shields.io/badge/IDE-VSCode-informational)
![badges](https://img.shields.io/badge/python-3-blue)
![badges](https://img.shields.io/badge/pygame-2.0.2-yellow)
![Generic badge](https://img.shields.io/badge/pygame_menu-4.2.0-yellow.svg)
![Generic badge](https://img.shields.io/badge/pymysql-1.0.2-orange.svg)  

---
🤪 [이예나](https://github.com/yaena1223) (팀장) : 경영정보학과 18학번

🥰 [최다희](https://github.com/daheeda) (팀원) : 통계학과 19학번

😊 [정민경](https://github.com/kkong1007) (팀원) : 화공생물공학과 19학번

---

![로그인2](https://user-images.githubusercontent.com/77571090/173226976-b3931216-9b16-4b4a-8633-20877e6a0f3b.png)
<br/></br>안녕하세요 팀 드림즈컴츄르 입니다 : ) <br/>
pygame를 기반으로 한 ‘동냥이’테마 shooting game입니다.

<br/></br>
### How to run

---

1. python3 설치

```powershell
sudo apt-get update
sudo apt install python3
```

2. pygame, pygame_menu 설치

```powershell
sudo pip3 install pygame==2.0.2
sudo pip3 install pygame_menu==4.2.0
```

3. pymysql 설치

```powershell
sudo pip3 install pymysql==1.0.2
```

4. tkinter 설치

```powershell
sudo apt-get install python3-tk
```

5. 게임 실행

```powershell
python3 Main.py
```

<br/></br>
### How to play

---

[Default]

![Untitled 1](https://user-images.githubusercontent.com/77571090/173226458-42aebf24-adb0-4114-a6f4-3965f8265fa1.png)

[PVP Game]

![Untitled 2](https://user-images.githubusercontent.com/77571090/173226507-7f20b997-f228-4524-a342-0950155b7a54.png)

<br/></br>
### Game preview

---

> 로그인/회원가입
> 

![Untitled 3](https://user-images.githubusercontent.com/77571090/173226588-f944264c-47ef-4dc5-b43e-0299c668f1b8.png)

- RDS 데이터베이스를 통해 user 정보 저장
- 로그인 버튼 클릭 시 아이디 & 비밀번호 입력 후 login 가능

<br/>

> 기본 메뉴 화면
> 

![Untitled 4](https://user-images.githubusercontent.com/77571090/173226613-11cc2f44-ff0e-484c-ad65-04d95198ba85.png)

- 네브바를 통해 원하는 페이지 접근 가능
- 게임은 Stage모드와 Infinite모드로 구성
- 게임 외의 기능에는 캐릭터상점, 마이페이지, 랭킹, 도움말, 소리on/off 가 있음

<br/>

> Stage 모드 game
> 

![Untitled 5](https://user-images.githubusercontent.com/77571090/173226634-d00874f5-2f96-4844-b89e-87f1c7d9d42a.png)

- 3가지 map이 있으며 각각 stage1,2,3으로 구성
- 게임 시작 시 목표점수 안내창 확인 가능

<br/>

> Infinite 모드 game
> 

![Untitled 6](https://user-images.githubusercontent.com/77571090/173226657-804ed977-00b7-4093-901f-c2cf7cecb3fa.png)

- 3가지 map으로 구성
- 목숨이 0이 될 경우 게임 종료
- 게임 종료 후 자동으로 랭킹이 등록됨
- 등록된 랭킹은 랭킹페이지에서 확인 가능

<br/>

> PVP game
> 

![Untitled 7](https://user-images.githubusercontent.com/77571090/173226689-3ccc27fd-5318-4674-8582-475ce0d12dec.png)

- 2인 플레이 게임으로 로그인 없이 이용 가능
- 120초의 제한 시간 내에 목숨이 0이 되거나 제한시간이 끝나면 게임 종료

<br/>

> Mypage
> 

![Untitled 8](https://user-images.githubusercontent.com/77571090/173226699-8d68ec9c-68ec-447b-bc7f-93dc54df0759.png)


- 아이디, 점수, 보유 코인, 보유 캐릭터에 대한 정보 제공
- 캐릭터 선택 가능

<br/>

> Character Store
> 

![Untitled 10](https://user-images.githubusercontent.com/77571090/173226710-060422c1-2444-49e6-91d6-8d7eb053f189.png)

- 캐릭터 상점에서는 보유한 코인으로 캐릭터 구매 가능

<br/></br>
### 시연영상
https://www.youtube.com/watch?v=pP2DY6C4dr8
<br/></br>
### Credits

---

- Sounds: [https://github.com/CSID-DGU/2021-2-OSSProj-PlusAlpha-9](https://github.com/CSID-DGU/2021-2-OSSProj-PlusAlpha-9)
- Character image: Copyright 2022. Jung Mingyeong
- Item image: Copyright 2022. Jung Mingyeong
- Background image: Copyright 2022. Choi Dahee
- Attacker image: Copyright 2022. Choi Dahee

<br/></br>
### References

---

- Origin Source: [https://github.com/CSID-DGU/2021-2-OSSProj-PlusAlpha-9](https://github.com/CSID-DGU/2021-2-OSSProj-PlusAlpha-9)
- Login/Signup Source:  https://github.com/CSID-DGU/2021-1-OSSPC-Tongsan1-2

