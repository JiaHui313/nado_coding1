import os
import pygame
#########################################################
# 기본 초기화(반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 640 # 가로크기
screen_height = 480 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("팡팡게임") # 게임이름

# FPS(프레임 퍼 세컨드 frame per second)
clock = pygame.time.Clock()
#########################################################

# 1. 사용자가 해야 하는 게임 초기화(배경화면, 게임이미지, 캐릭터, 좌표, 속도, 폰트 등..)
#배경넣기
current_path = os.path.dirname(__file__) # 현재파일의 위치를 반환
image_path = os.path.join(current_path, "images") #이미지 폴더 위치 반환

background = pygame.image.load(os.path.join(image_path, "background.png"))

#stage만들기
stage =pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

#character 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height - stage_height




#이벤트 루프
running = True # 게임이 진행중인가를 확인하는 문장
while running:
  dt = clock.tick(30) #게임화면의 초당 프레임 수를 설정

  # 2. 이벤트 처리(키보드, 마우스 등...)
  for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
    if event.type == pygame.QUIT: #창닫는 이벤트가 발생한 경우에
      running = False # 게임이 진행중이 아님

  # 3. 게임 캐릭터 위치 정의
 
  #캐릭터를 화면 가로 경계값 안으로 조정
  
  #캐릭터를 화면 세로 경계값 안으로 조정
  

  # 4. 충돌처리
  #충돌처리를 위한 rect 정보 업데이트
 

  # 충돌체크
 

  # 5. 화면에 그리기
  screen.blit(background, (0,0))
  screen.blit(stage, (0,screen_height - stage_height))
  screen.blit(character, (character_x_pos, character_y_pos))
  # 타이머 집어넣기 #경과 시간 계사하기
 
  #만약 시간이 0이하이면 게임 종료
  
  pygame.display.update() # 반드시 게임화면을 다시 그리기!!!

#종료 직전 잠시 대기
pygame.time.delay(2000) #2초 정도 대기

# pygame 종료
pygame.quit()

















