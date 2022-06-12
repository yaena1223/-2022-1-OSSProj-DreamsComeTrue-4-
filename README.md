# 2022-1-OSSProj-DreamsComeTrue-4
## Team_DreamsComeTrue💭
![Github license](https://img.shields.io/github/license/CSID-DGU/2022-1-OSSProj-DreamsComeTrue-4)
![badges](https://img.shields.io/badge/OS-ubuntu-red)
![badges](https://img.shields.io/badge/IDE-VSCode-informational)
![badges](https://img.shields.io/badge/python-3-blue)
![badges](https://img.shields.io/badge/pygame-2.0.2-yellow)
![Generic badge](https://img.shields.io/badge/pygame_menu-4.2.0-yellow.svg)
![Generic badge](https://img.shields.io/badge/pymysql-1.0.2-orange.svg)

안녕하세요 팀 드림즈컴츄르 입니다 : ) 

```markdown
🤪 [이예나](https://github.com/yaena1223) (팀장) : 경영정보학과 18학번

🥰 [최다희](https://github.com/daheeda) (팀원) : 통계학과 19학번

😊 [정민경](https://github.com/kkong1007) (팀원) : 화공생물공학과 19학번
```

![Untitled](Readme%20md%20d956af960cc740b2937bd0fb546ca2af/Untitled.png)

- pygame를 기반으로 한 ‘동냥이’테마 shooting game/

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

4. 

```powershell
sudo apt-get install python3-tk
```

5. 게임 실행

```powershell
python3 Main.py
```

### How to play

---

[Default]

![Untitled](Readme%20md%20d956af960cc740b2937bd0fb546ca2af/Untitled%201.png)

[PVP Game]

![Untitled](Readme%20md%20d956af960cc740b2937bd0fb546ca2af/Untitled%202.png)

### Game preview

---

> 로그인/회원가입
> 

![Untitled](Readme%20md%20d956af960cc740b2937bd0fb546ca2af/Untitled%203.png)

- RDS 데이터베이스를 통해 user 정보 저장
- 로그인 버튼 클릭 시 아이디 & 비밀번호 입력 후 login 가능

> 기본 메뉴 화면
> 

![Untitled](Readme%20md%20d956af960cc740b2937bd0fb546ca2af/Untitled%204.png)

- 네브바를 통해 원하는 페이지 접근 가능
- 게임은 Stage모드와 Infinite모드로 구성
- 게임 외의 기능에는 캐릭터상점, 마이페이지, 랭킹, 도움말, 소리on/off 가 있음

> Stage 모드 game
> 

![Untitled](Readme%20md%20d956af960cc740b2937bd0fb546ca2af/Untitled%205.png)

- 3가지 map이 있으며 각각 stage1,2,3으로 구성
- 게임 시작 시 목표점수 안내창 확인 가능

> Infinite 모드 game
> 

![Untitled](Readme%20md%20d956af960cc740b2937bd0fb546ca2af/Untitled%206.png)

- 3가지 map으로 구성
- 목숨이 0이 될 경우 게임 종료
- 게임 종료 후 자동으로 랭킹이 등록됨
- 등록된 랭킹은 랭킹페이지에서 확인 가능

> PVP game
> 

![Untitled](Readme%20md%20d956af960cc740b2937bd0fb546ca2af/Untitled%207.png)

- 2인 플레이 게임으로 로그인 없이 이용 가능
- 120초의 제한 시간 내에 목숨이 0이 되거나 제한시간이 끝나면 게임 종료

> Mypage
> 

![Untitled](Readme%20md%20d956af960cc740b2937bd0fb546ca2af/Untitled%208.png)

![Untitled](Readme%20md%20d956af960cc740b2937bd0fb546ca2af/Untitled%209.png)

- 아이디, 점수, 보유 코인, 보유 캐릭터에 대한 정보 제공
- 캐릭터 선택 가능

> Character Store
> 

![Untitled](Readme%20md%20d956af960cc740b2937bd0fb546ca2af/Untitled%2010.png)

- 캐릭터 상점에서는 보유한 코인으로 캐릭터 구매 가능

### Credits

---

- Sounds: [https://github.com/CSID-DGU/2021-2-OSSProj-PlusAlpha-9](https://github.com/CSID-DGU/2021-2-OSSProj-PlusAlpha-9)
- Character image: Copyright 2022. Jung Mingyeong
- Item image: Copyright 2022. Jung Mingyeong
- Background image: Copyright 2022. Choi Dahee
- Attacker image: Copyright 2022. Choi Dahee

### References

---

- Origin Source: [https://github.com/CSID-DGU/2021-2-OSSProj-PlusAlpha-9](https://github.com/CSID-DGU/2021-2-OSSProj-PlusAlpha-9)
- Login/Signup Source:  https://github.com/CSID-DGU/2021-1-OSSPC-Tongsan1-2
