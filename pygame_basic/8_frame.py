import pygame
#########################################################
# 기본 초기화(반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("게임샘플1") # 게임이름

# FPS(프레임 퍼 세컨드 frame per second)
clock = pygame.time.Clock()
#########################################################

# 1. 사용자가 해야 하는 게임 초기화(배경화면, 게임이미지, 캐릭터, 좌표, 속도, 폰트 등..)
#이벤트 루프
running = True # 게임이 진행중인가를 확인하는 문장
while running:
  dt = clock.tick(30) #게임화면의 초당 프레임 수를 설정

  # 2. 이벤트 처리(키보드, 마우스 등...)
  for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
    if event.type == pygame.QUIT: #창닫는 이벤트가 발생한 경우에
      running = False # 게임이 진행중이 아님

  # 3. 게임 캐릭터 위치 정의
  character_x_pos += to_x * dt # 캐릭터 좌표에 대입
  character_y_pos += to_y * dt
  
  #캐릭터를 화면 가로 경계값 안으로 조정
  if character_x_pos < 0:
    character_x_pos = 0
  elif character_x_pos > (screen_width - character_width):
    character_x_pos = screen_width - character_width

  #캐릭터를 화면 세로 경계값 안으로 조정
  if character_y_pos < 0:
    character_y_pos = 0
  elif character_y_pos > screen_height - character_height:
    character_y_pos = screen_height - character_height

  # 4. 충돌처리
  #충돌처리를 위한 rect 정보 업데이트
  character_rect  = character.get_rect()
  character_rect.left = character_x_pos
  character_rect.top = character_y_pos

  enemy_rect = enemy.get_rect()
  enemy_rect.left = enemy_x_pos
  enemy_rect.top = enemy_y_pos

  # 충돌체크
  if character_rect.colliderect(enemy_rect):
    print("충돌했어요")
    running = False

  # 5. 화면에 그리기
  screen.blit(background, (0,0)) # 배경 그리기
  screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
  screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기

  # 타이머 집어넣기 #경과 시간 계사하기
  elasped_time = (pygame.time.get_ticks() - start_ticks)/1000 # 초로 환산하기 위해 1000으로 나눔
  timer = game_font.render(str(int(total_time - elasped_time)), True, (255,255,255))
  screen.blit(timer, (10,10))

  #만약 시간이 0이하이면 게임 종료
  if total_time - elasped_time < 0:
    print("타임아웃")
    running = False

  
  pygame.display.update() # 반드시 게임화면을 다시 그리기!!!

#종료 직전 잠시 대기
pygame.time.delay(2000) #2초 정도 대기

# pygame 종료
pygame.quit()
