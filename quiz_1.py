# 퀴즈) 하늘에서 떨어지는 똥 피하는 게임 만드시오

# [게임조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동가능

# 2. 똥은 화면 가장 위에서 떨어짐. x좌표는 매번 랜덤으로 설정

# 3. 캐릭터가 똥을 피하면 다음 똥이 계속 떨어짐.

# 4. 캐릭터가 똥과 충돌하면 게임 종료

# 5. fps는 30으로 고정

# [게임이미지]
# 1. 배경: 640 * 480 (세로, 가로) - background.png
# 2. 캐릭터: 70 * 70 -character.png
# 3. 똥: 70 * 70 - enemy.png

import random
import pygame
#########################################################
# 기본 초기화(반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("똥피하는 게임") # 게임이름

# FPS(프레임 퍼 세컨드 frame per second)
clock = pygame.time.Clock()
#########################################################

# 1. 사용자가 해야 하는 게임 초기화(배경화면, 게임이미지, 캐릭터, 좌표, 속도, 폰트 등..)
#배경 만들기
background = pygame.image.load("C:\\Users\\rkgpt\\OneDrive\\Desktop\\혼공파\\pygame_basic\\background.png")

#캐릭터 만들기
character = pygame.image.load("C:\\Users\\rkgpt\\OneDrive\\Desktop\\혼공파\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width/2)
character_y_pos = (screen_height - character_height)

#캐릭터 움직이기(이동위치)
to_x = 0
character_speed = 10

#똥 만들기
ddong = pygame.image.load("C:\\Users\\rkgpt\\OneDrive\\Desktop\\혼공파\\pygame_basic\\enemy.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0
ddong_speed = 10


#이벤트 루프
running = True # 게임이 진행중인가를 확인하는 문장
while running:
  dt = clock.tick(30) #게임화면의 초당 프레임 수를 설정

  # 2. 이벤트 처리(키보드, 마우스 등...)
  for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
    if event.type == pygame.QUIT: #창닫는 이벤트가 발생한 경우에
      running = False # 게임이 진행중이 아님
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        to_x -= character_speed
      elif event.key == pygame.K_RIGHT:
        to_x += character_speed

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.KEY_RIGHT:
        to_x = 0

  # 3. 게임 캐릭터 위치 정의
  character_x_pos += to_x

  if character_x_pos < 0: #캐릭터를 화면 가로 경계값 안으로 조정
    character_x_pos = 0
  elif character_x_pos > (screen_width - character_width):
    character_x_pos = screen_width - character_width

  ddong_y_pos += ddong_speed

  if ddong_y_pos > screen_height:
    ddong_y_pos = 0
    ddong_x_pos = random.radnint(0 ,(screen_width - ddong_width))


  # 4. 충돌처리 #충돌처리를 위한 rect 정보 업데이트
  character_rect = character.get_rect()
  character_rect.left = character_x_pos
  character_rect.top = character_y_pos

  ddong_rect = ddong.get_rect()
  ddong_rect.left = ddong_x_pos
  ddong_rect.top = ddong_y_pos

  if character_rect.colliderect(ddong_rect):# 충돌체크
    print("충!돌! 게임오버")
    running = False
  
  # 5. 화면에 그리기(배경, 캐릭터, 똥)
  screen.blit(background, (0,0)) # 배경 그리기(배경, 위치)
  screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
  screen.blit(ddong, (ddong_x_pos, ddong_y_pos)) # 적 그리기

 
  
  pygame.display.update() # 반드시 게임화면을 다시 그리기!!!

#종료 직전 잠시 대기
#pygame.time.delay(2000) #2초 정도 대기

# pygame 종료
pygame.quit()
